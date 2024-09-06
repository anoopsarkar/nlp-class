from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
from fuzzyfinder import fuzzyfinder
from transformers import pipeline
import click
import torch
import os
import sys

pager_size = 8000

#check for gpu
device="cpu"
if torch.backends.mps.is_available():
    device = torch.device("mps")

access_token=os.environ.get("HF_ACCESS_TOKEN")
model_ids = ["meta-llama/Meta-Llama-3.1-8B-Instruct", "Qwen/Qwen2-1.5B-Instruct"]
pipe = pipeline(
    "text-generation",
    device=device,
    model=model_ids[0] if len(model_ids) >= 1 else "",
    model_kwargs={"torch_dtype": torch.bfloat16},
    token=access_token,
)

keywords = ['quit']

class completer(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        matches = fuzzyfinder(word_before_cursor, keywords)
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))

while True:
    user_prompt = prompt(u'> ',
                        history=FileHistory('history.txt'),
                        auto_suggest=AutoSuggestFromHistory(),
                        completer=completer(),
                        )
    if user_prompt == "quit":
        sys.exit(0)
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that provides useful answers without too much extra output.",
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ]
    outputs = pipe(
        messages,
        temperature=0.9,
        max_new_tokens=8096,
        do_sample=True,
    )
    llm_output = outputs[0]["generated_text"][-1]["content"]
    if (len(llm_output) > pager_size):
        click.echo_via_pager(llm_output)
    else:
        print(llm_output)
