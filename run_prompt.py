import requests

with open("prompt.txt", "r") as file:
    prompt_template = file.read()

user_input = input("Enter your question: ")

final_prompt = prompt_template.replace("{input}", user_input)

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": final_prompt,
        "stream": False
    }
)

print(response.json()["response"])