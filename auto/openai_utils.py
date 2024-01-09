import os
from openai import OpenAI


# TODO: 这个函数有无必要
# 同历史的session_id进行对比，相同则说明仍处于同一对话，如果为初次使用，则判断返回值是否为“OK”
def check_is_ok(steam):
    for chunk in steam:
        steam_id = chunk.id
        if chunk.choices[0].delta.content is not None:
            if chunk.choices[0].delta.content == "OK":
                return True

    with open(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".session_id"))
    ) as f:
        cache_session_id = f.read()
        if cache_session_id == steam_id:
            return True

        return False


def read_response(stream):
    full_res = ""
    session_id = ""
    for chunk in stream:
        session_id = chunk.id
        if chunk.choices[0].delta.content is not None:
            full_res = "".join([full_res, chunk.choices[0].delta.content])

    with open(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".session_id")), "w"
    ) as f:
        f.write(session_id)

    return full_res.strip()


def conversation(prompt, conversation_id=""):
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
