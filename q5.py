from openai import OpenAI
import json

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm_studio"
)

def main():
    models = client.models.list()
    for m in models.data:
        print(m)

    response = client.chat.completions.create(
        model="qwen3-0.6b",
        messages=[
            {"role": "system","content": "You are helpful assistant."}, #typical  system prompt
            {"role":"user","content":"What did you think of the movie Dune?"}
        ]

    )

    print("Review:")
    print(response.choices[0].message.content)