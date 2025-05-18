# AINurse - AI Chat Demo using OpenAI API
# Copyright © 2025 Sara Ghalib Al-Harbi – All Rights Reserved

import openai

# Insert your own API key securely (never share it in public repos)
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

print("AINurse AI Chat – powered by OpenAI")
print("Type your question below (or type 'exit' to quit):")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an intelligent and compassionate AI nurse assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response['choices'][0]['message']['content']
    print("AINurse:", reply)
