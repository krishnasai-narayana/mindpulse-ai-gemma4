import ollama

def ask_gemma(prompt):

    response = ollama.chat(
        model="gemma4:e4b",
        messages=[
            {
                "role": "system",
                "content": """
You are a mental wellness assistant.

Be empathetic.
Be concise.
Keep responses under 150 words.
Do not provide medical diagnosis.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content