import os
import openai


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


# 回话补全返回结构如下
# {
#   "id": "chatcmpl-6p9XYPYSTTRi0xEviKjjilqrWU2Ve",
#   "object": "chat.completion",
#   "created": 1677649420,
#   "model": "gpt-3.5-turbo",
#   "usage": { "prompt_tokens": 56, "completion_tokens": 31, "total_tokens": 87 },
#   "choices": [
#     {
#       "message": {
#         "role": "assistant",
#         "content": "The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers."
#       },
#       "finish_reason": "stop",
#       "index": 0
#     }
#   ]
# }
def conversation(messages, model="gpt-4"):
    stream = openai.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    return read_response(stream)
