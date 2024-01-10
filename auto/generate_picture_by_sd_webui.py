from datetime import datetime
import requests
import json
import base64
import time
import os

# 调用sdwebui接口代码参考: https://gist.github.com/w-e-w/0f37c04c18e14e4ee1482df5c4eb9f53
# 在阿里云PAI上调用webui接口，需要先行登录:
#   https://help.aliyun.com/zh/pai/user-guide/call-a-service-over-a-public-endpoint?spm=5176.2020520104.0.0.19973f1bHIdDef
# 如果需要登录，需要执行如下步骤步
# 在luanch命令中传入 --nowebui
webui_server_url = (
    "https://dsw-gateway-cn-shanghai.data.aliyun.com/dsw-298247/proxy/7861/"
)

# out_dir = "api_out"
out_dir = ""
out_dir_t2i = os.path.join(out_dir, "txt2img")
out_dir_i2i = os.path.join(out_dir, "img2img")
os.makedirs(out_dir_t2i, exist_ok=True)
os.makedirs(out_dir_i2i, exist_ok=True)


def timestamp():
    return datetime.fromtimestamp(time.time()).strftime("%Y%m%d-%H%M%S")


def encode_file_to_base64(path):
    with open(path, "rb") as file:
        # b64encode返回的是字节序列，需要解码为utf8字符串
        return base64.b64encode(file.read()).decode("utf-8")


def decode_and_save_base64(base64_str, save_path):
    with open(save_path, "wb") as file:
        file.write(base64.b64decode(base64_str))


def call_api(api_endpoint, **payload):
    # 词典转JSON，再转字符串
    data = json.dumps(payload).encode("utf-8")
    response = requests.post(
        f"{webui_server_url}/{api_endpoint}",
        headers={"Content-Type": "application/json"},
        data=data,
    )
    print(response.content)
    return response.json()


def call_txt2img_api(**payload):
    response = call_api("sdapi/v1/txt2img", **payload)
    print("response t2i", response)
    for index, image in enumerate(response.get("images")):
        save_path = os.path.join(out_dir_t2i, f"txt2img-{timestamp()}-{index}.png")
        print("t2i image", image)
        decode_and_save_base64(image, save_path=save_path)


def call_img2img_api(**payload):
    response = call_api("sdapi/v1/img2img", **payload)
    print("response i2i", response)
    for index, image in enumerate(response.get("images")):
        save_path = os.path.join(out_dir_i2i, f"img2img-{timestamp()}-{index}.png")
        print("i2i image", image)
        decode_and_save_base64(image, save_path=save_path)


if __name__ == "__main__":
    payload = {
        # "prompt": "masterpiece, (best quality:1.1), 1girl <lora:lora_model:1>"
        "prompt": "masterpiece, (best quality:1.1), 1girl ",
        "negative_prompt": "",
        "seed": 1,
        "width": 512,
        "height": 512,
        "cfg_scale": 7,
        "sampler_name": "DPM++ 2M Karras",
        "n_iter": 1,
        "batch_size": 1,
    }

    call_txt2img_api(**payload)

    # TODO: 试一下是否可以获取远程的url
    init_images = [
        encode_file_to_base64(r"B:\path\to\img_1.png"),
        # "https://image.can/also/be/a/http/url.png",
    ]

    batch_size = 2
    payload = {
        "prompt": "1girl, blue hair",
        "seed": 1,
        "steps": 20,
        "width": 512,
        "height": 512,
        "denoising_strength": 0.5,
        "n_iter": 1,
        "init_images": init_images,
        "batch_size": batch_size if len(init_images) == 1 else len(init_images),
    }
    # TODO: 暂不处理
    # call_img2img_api(**payload)
