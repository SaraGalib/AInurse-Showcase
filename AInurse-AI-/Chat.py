# AINurse - AI Chat Demo using OpenAI API
# Copyright © 2025 Sara Ghalib Al-Harbi – All Rights Reserved

import openai
import os

# Read your API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY is not set.")
    exit()

openai.api_key = api_key

print("AINurse Chat – powered by OpenAI")
print("Ask a question (type 'exit' to quit):")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an intelligent AI nurse assistant that answers clearly and briefly."},
            {"role": "user", "content": user_input}
        ]
    )

    print("AINurse:", response['choices'][0]['message']['content'])
