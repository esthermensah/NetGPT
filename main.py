

# import openai
# import json


# def load_api_key():
#     with open("config.json", "r") as f:
#         config = json.load(f)
#     return config.get("OPENAI_API_KEY")

# openai.api_key = load_api_key()

# client = openai.OpenAI(api_key=openai.api_key)

# def explain_config(config_text):
#     prompt = f"""Explain the following Cisco config in simple terms, like you're helping a junior network engineer:

# {config_text}

# Respond in bullet points."""

#     response = client.chat.completions.create(
#         model="gpt-4",
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=500,
#         temperature=0.3
#     )
#     return response.choices[0].message.content



# if __name__ == "__main__":
#     print("Paste your Cisco config below. Press Enter twice to finish:\n")
#     lines = []
#     while True:
#         line = input()
#         if line == "":
#             break
#         lines.append(line)
#     config_text = "\n".join(lines)

#     explanation = explain_config(config_text)
#     print("\n===== Explanation =====\n")
#     print(explanation)


import openai
import json

# Load API key from config file
with open("config.json") as f:
    key_data = json.load(f)
openai.api_key = key_data["OPENAI_API_KEY"]

client = openai.OpenAI(api_key=openai.api_key)

def explain_config(config_text):
    prompt = f"""Explain the following Cisco config in simple terms, like you're helping a junior network engineer:

{config_text}

Respond in bullet points."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.3
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print("Paste your Cisco config below. Press Enter twice to finish:\n")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    config_text = "\n".join(lines)

    explanation = explain_config(config_text)
    print("\n===== Explanation =====\n")
    print(explanation)
