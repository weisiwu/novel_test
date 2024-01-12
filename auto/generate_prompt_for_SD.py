import os
from split_sentence_from_file import split_sentence
from openai_utils import conversation
from generate_picture_by_sd_webui import call_txt2img_api

prompt_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "..", "documents", "sd_prompt_generate.prompt"
    )
)


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
    # TODO: 这里处理后，返回的prompt数量不对
    print("tset", len(filter(None, response.strip().split("\n"))))
    print("xx", len(prompt_res))
    positive_prompt = prompt_res[:-1]
    negtive_prompt = [prompt_res[-1]]

    return {"positive_prompt": positive_prompt, "negtive_prompt": negtive_prompt}


if __name__ == "__main__":
    raw_prompts = generate_sd_prompt()

    positive_prompts = raw_prompts.get("positive_prompt", "")
    negative_prompt = str(raw_prompts.get("negtive_prompt", ""))

    print(len(positive_prompts))
    for prompt in positive_prompts:
        print("prompt")
        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "seed": 1,
            "width": 512,
            "height": 512,
            "cfg_scale": 7,
            "sampler_name": "DPM++ 2M Karras",
            "n_iter": 1,
            "batch_size": 1,
        }

        print("开始生成")
        # call_txt2img_api(**payload)
        print("生成完毕")
