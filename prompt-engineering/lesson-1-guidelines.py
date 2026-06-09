
from openai import OpenAI
import os
from dotenv import load_dotenv

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
text = f"""
Making tea is easy, \
Boil water, place a tea bag in a cup,\
Pour hot water over the tea bag .\
let the tea steep \
Remove the bad and add sugar or milk if desired \


"""
text_2 = f"""
The sun is the center of our solar system. \
It contains most of the solar system's mass. \
"""


user_input = input("Ask anything: ")
prompt = f"""
You must answer using ONLY the information \
inside the triple backticks. \

If the answer cannot be found in the context, \
say "I don't have enough information." \

If the context contains steps, write step by step in, \
step 1: 
step 2:
step n:
      .\
if the there is no steps, \
write "No steps provided." \

User Question:
{user_input}

```{text_2}```

Do not say "Based on the information provided". \

Return a concise answer. \

"""
response = get_completion(prompt)

print(response)
