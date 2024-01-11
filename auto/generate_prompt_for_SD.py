import os
from split_sentence_from_file import split_sentence
from openai_utils import conversation

prompt_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "..", "documents", "sd_prompt_generate.prompt"
    )
)


# TODO: 1、先每次都init，后面对init做缓存
def generate_sd_prompt():
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_preset = f.read()

    conversation_messages = []

    # 设置上下文对话环境
    conversation_messages.append({"role": "system", "content": prompt_preset})

    # 组装生成prompt
    sentences = split_sentence()
    for sentence in sentences:
        conversation_messages.append({"role": "user", "content": sentence})

    response = conversation(conversation_messages)
    prompt_res = list(filter(None, response.strip().split("\n")))
    positive_prompt = prompt_res[:-1]
    negtive_prompt = [prompt_res[-1]]

    return {"positive_prompt": positive_prompt, "negtive_prompt": negtive_prompt}


if __name__ == "__main__":
    positive_prompt, negtive_prompt = generate_sd_prompt()

    print("positive_prompt", positive_prompt)
    print("negtive_prompt", negtive_prompt)
