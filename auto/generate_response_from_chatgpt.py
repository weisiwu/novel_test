from openai import OpenAI
from openai_utils import read_response


def conversation_openai(prompt):
    client = OpenAI()
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        stream=True,
    )

    return read_response(stream)
