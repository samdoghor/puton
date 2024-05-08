"""src/ai.py

Keyword arguments:
argument -- description
Return: all ai configuration
"""

import google.generativeai as ai

import config

ai.configure(api_key=config.ai_api_key)
model = ai.GenerativeModel(config.ai_model)

response = model.generate_content("predict ")
# print(response.text)

#  test ai

try:
    with open("ai.md", "w", encoding="utf-8") as answer:
        answer.write(response.text)
    print("Prompt completed")

except Exception as e:
    print(e)
