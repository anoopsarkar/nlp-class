from transformers import pipeline
import torch
import os
import sys

#check for gpu
device="cpu"
if torch.backends.mps.is_available():
    device = torch.device("mps")

access_token=os.environ.get("HF_ACCESS_TOKEN")
model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
#model_id = "Qwen/Qwen2-1.5B-Instruct"
pipe = pipeline(
    "text-generation",
    device=device,
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    token=access_token,
)
prompt = 'Computers will never'
full_prompt = f"Finish this reassuring parable about the superiority of humans over computers in a short sentence: {prompt} ____."
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

for _ in range(10):
    outputs = pipe(
        messages,
        temperature=0.9,
        max_new_tokens=64,
        do_sample=True,
    )
    print(prompt, outputs[0]["generated_text"][-1]["content"].split("\n", 1)[0])
