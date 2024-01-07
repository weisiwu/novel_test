import json
import time
import requests
from datetime import datetime
from hanlp import hanlp
from requests.exceptions import RequestException

split_sent = hanlp.load(hanlp.pretrained.eos.UD_CTB_EOS_MUL)


def generate_picture(prompt):
    try:
        # https://platform.openai.com/docs/api-reference/images/create
        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            data=json.dumps(
                {
                    "model": "dall-e-3",
                    "prompt": prompt,
                    "n": 1,
                    "quality": "hd",
                    "size": "1024x1024",
                }
            ),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer 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",
            },
        )

        if response.status_code == 200:
            picture_obj = response.json()
            picture_url = picture_obj.get("data", [])[0].get("url", None)
            print("picture_url", picture_url)
            return picture_url
        else:
            print("chatgpt返回错误信息: ", response.content)
    except RequestException as e:
        print(f"请求出错: {e}")


def save_image_from_url(url, file_path):
    # 发送 GET 请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 打开文件以写入二进制数据
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"图片已保存到 {file_path}")
    else:
        print(f"无法获取图片，状态码：{response.status_code}")


def group_sentence(sentences, n_groups):
    # 计算每组的句子数量
    per_group = len(sentences) // n_groups
    remainder = len(sentences) % n_groups

    # 初始化组
    groups = [[] for _ in range(n_groups)]

    # 分配句子到各组
    current_group = 0
    for i, sentence in enumerate(sentences):
        groups[current_group].append(sentence)

        # 检查是否需要转移到下一组
        if i < remainder * (per_group + 1) - 1:
            if (i + 1) % (per_group + 1) == 0:
                current_group += 1
        else:
            if (i + 1 - remainder) % per_group == 0:
                current_group += 1

    # return groups
    return ["".join(group) for group in groups]


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from config_loader import loader_config

    config = loader_config()

    file_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        config["input"]["save_path"],
        config["input"]["file_name"],
    )
    img_target_num = config["output"]["img_target_num"]

    with open(file_path, "r", encoding="utf8") as f:
        # 按照中文进行分句，统计出总句数再分组
        sentences = split_sent(f.read())
        sentences_group = group_sentence(sentences, img_target_num)

        print(sentences_group, len(sentences_group))

        for group in sentences_group:
            picture_url = generate_picture(group)
            picture_path = os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                config["output"]["save_img_path"],
                f"{datetime.now().strftime('%Y%m%d%H%M%S')}.png",
            )
            save_image_from_url(picture_url, picture_path)
            # 当前limit是每分钟5张图
            # https://platform.openai.com/account/limits
            time.sleep(20)  # 60 / 5 = 12，需要大于12
