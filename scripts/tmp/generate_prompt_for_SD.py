import os
from split_sentence_from_file import split_sentence
from openai_utils import conversation
from generate_picture_by_sd_webui import call_txt2img_api

prompt_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "..", "documents", "sd_prompt_generate.prompt"
    )
)


# TODO: 返回生成的prommpt不稳定
def generate_sd_prompt():
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_preset = f.read()

    conversation_messages = []
    # 组装生成prompt
    sentences = split_sentence()

    for sentence in sentences:
        conversation_messages.append(
            [
                {"role": "system", "content": prompt_preset},
                {"role": "user", "content": sentence},
            ]
        )

    combined_prompts = []

    for msg in conversation_messages:
        response = conversation(msg)
        response_arr = list(filter(None, response.strip().split("\n")))
        # print("======")
        # print(response_arr)
        # print("======")

        positive_prompt = response_arr[0]
        negative_prompt = response_arr[1]
        combined_prompts.append(
            {"positive_prompt": positive_prompt, "negative_prompt": negative_prompt}
        )

    print("======")
    print(positive_prompt)
    print(negative_prompt)
    # print("对话长度", len(conversation_messages), len(combined_prompts))
    print("======")

    return combined_prompts


if __name__ == "__main__":
    combined_prompts = generate_sd_prompt()

    print("combined_prompts===", combined_prompts)
    # for index, item in enumerate(combined_prompts):
    #     positive_prompt = item.get("positive_prompt", "")
    #     negative_prompt = item.get("negative_prompt", "")
    #     payload = {
    #         "prompt": positive_prompt,
    #         "negative_prompt": negative_prompt,
    #         "seed": 1,
    #         "width": 512,
    #         "height": 512,
    #         "cfg_scale": 7,
    #         "sampler_name": "DPM++ 2M Karras",
    #         "n_iter": 1,
    #         "batch_size": 1,
    #     }

    #     print("positive_prompt===", positive_prompt)
    #     print("negative_prompt===", negative_prompt)
    #     print("====================================")

    # print(
    #     f"第{index} 开始生成 {positive_prompt}",
    # )
    # call_txt2img_api(**payload)
