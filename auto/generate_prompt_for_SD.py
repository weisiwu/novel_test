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

    # 设置上下文对话环境
    response = conversation(prompt_preset, role="system")

    # TODO: 后续将失败的response过滤，并终止
    prompt_list = []

    if response == "OK":
        # 开启完毕上下文后，开始逐一发送句子，生成prompt
        sentences = split_sentence()
        for sentence in sentences:
            response = conversation(sentence, role="user")
            prompt_res = list(filter(None, response.strip().split("\n")))
            positive_prompt = prompt_res[:2]
            negtive_prompt = prompt_res[2:]
            prompt_list.append(
                {"positive_prompt": positive_prompt, "negtive_prompt": negtive_prompt}
            )

    if not len(prompt_list):
        return None

    return prompt_list


# 测试
if __name__ == "__main__":
    positive_prompt, negtive_prompt = generate_sd_prompt()
    print("positive_prompt", positive_prompt)
    print("negtive_prompt", negtive_prompt)
