
from openai import OpenAI
import os
from dotenv import load_dotenv
from lesson_2_prompt import build_prompt2
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def get_completion(prompt, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content


user_input = input("Ask anything: ")
prompt = build_prompt2(user_input)
response = get_completion(prompt)

print(response)
