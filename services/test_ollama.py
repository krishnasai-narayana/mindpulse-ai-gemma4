import ollama

response = ollama.chat(
    model="gemma4:e4b",
    messages=[
        {
            "role": "user",
            "content": "What is 2+2?"
        }
    ]
)

print(response)
print("\n")
print(response.message.content)