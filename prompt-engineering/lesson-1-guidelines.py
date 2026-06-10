
from openai import OpenAI
import os
from dotenv import load_dotenv
import data
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
prompt = f"""
You must answer using ONLY the information \
inside the triple backticks. \

If the answer cannot be found in the context, \
say "I don't have enough information." \

Perform the following actions : \
1. summarize the following text in delimited.\
2. translate the summary into french. \



User Question:
{user_input}

```{data.text}```

Do not say "Based on the information provided". \

Return a concise answer. \

"""
response = get_completion(prompt)

print(response)
