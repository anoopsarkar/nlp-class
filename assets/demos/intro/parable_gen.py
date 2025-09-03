from transformers import pipeline
import torch
import os
import sys

#check for gpu
device="cpu"
if torch.backends.mps.is_available():
    device = torch.device("mps")

access_token=os.environ.get("HF_ACCESS_TOKEN")
model_id = "Qwen/Qwen3-4B-Instruct-2507"
#model_id = "meta-llama/Llama-3.2-3B-Instruct"

pipe = pipeline(
    "text-generation",
    device=device,
    model=model_id,
    model_kwargs={"dtype": torch.bfloat16},
    token=access_token,
)
prompt = 'Computers will never'
full_prompt = f"Finish this reassuring parable about the superiority of humans over computers in a sentence with 10 words using creativity and humor: {prompt} ____."
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant that provides useful answers without too much extra output.",
    },
    {
        "role": "user",
        "content": prompt,
    },
]

print(prompt)
for _ in range(10):
    outputs = pipe(
        messages,
        temperature=1.0,
        max_new_tokens=128,
        do_sample=True,
        pad_token_id=pipe.tokenizer.eos_token_id,
    )
    print(outputs[0]["generated_text"][-1]["content"].split("\n", 1)[0])
