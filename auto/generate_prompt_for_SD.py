import os
from split_sentence_from_file import split_sentence
from generate_response_from_chatgpt import conversation_openai

prompt_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "..", "documents", "sd_prompt_generate.prompt"
    )
)


def generate_prompt():
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_preset = f.read()

    # 设置上下文对话环境
    conversation_openai(prompt_preset)

    sentences = split_sentence()
    # 对每一句生成sd prompt

    final_desc = [f"{prompt_preset}{sentence}" for sentence in sentences]
    print(final_desc)


generate_prompt()
