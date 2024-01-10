[33mcommit 3ccb6d6bcf44f7091fef42446fa06ee07129ddf0[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: weisiwu <siwu.wsw@autonavi.com>
Date:   Wed Jan 10 14:32:42 2024 +0800

    chore: 调用webui接口生图 - debuging

[1mdiff --git a/auto/generate_picture_by_sd_webui.py b/auto/generate_picture_by_sd_webui.py[m
[1mnew file mode 100644[m
[1mindex 0000000..7715e16[m
[1m--- /dev/null[m
[1m+++ b/auto/generate_picture_by_sd_webui.py[m
[36m@@ -0,0 +1,105 @@[m
[32m+[m[32mfrom datetime import datetime[m
[32m+[m[32mimport requests[m
[32m+[m[32mimport json[m
[32m+[m[32mimport base64[m
[32m+[m[32mimport time[m
[32m+[m[32mimport os[m
[32m+[m
[32m+[m[32m# 调用sdwebui接口代码参考: https://gist.github.com/w-e-w/0f37c04c18e14e4ee1482df5c4eb9f53[m
[32m+[m[32m# 在阿里云PAI上调用webui接口，需要先行登录:[m
[32m+[m[32m#   https://help.aliyun.com/zh/pai/user-guide/call-a-service-over-a-public-endpoint?spm=5176.2020520104.0.0.19973f1bHIdDef[m
[32m+[m[32m# 如果需要登录，需要执行如下步骤步[m
[32m+[m[32m# 在luanch命令中传入 --nowebui[m
[32m+[m[32mwebui_server_url = ([m
[32m+[m[32m    "https://dsw-gateway-cn-shanghai.data.aliyun.com/dsw-298247/proxy/7861/"[m
[32m+[m[32m)[m
[32m+[m
[32m+[m[32m# out_dir = "api_out"[m
[32m+[m[32mout_dir = ""[m
[32m+[m[32mout_dir_t2i = os.path.join(out_dir, "txt2img")[m
[32m+[m[32mout_dir_i2i = os.path.join(out_dir, "img2img")[m
[32m+[m[32mos.makedirs(out_dir_t2i, exist_ok=True)[m
[32m+[m[32mos.makedirs(out_dir_i2i, exist_ok=True)[m
[32m+[m
[32m+[m
[32m+[m[32mdef timestamp():[m
[32m+[m[32m    return datetime.fromtimestamp(time.time()).strftime("%Y%m%d-%H%M%S")[m
[32m+[m
[32m+[m
[32m+[m[32mdef encode_file_to_base64(path):[m
[32m+[m[32m    with open(path, "rb") as file:[m
[32m+[m[32m        # b64encode返回的是字节序列，需要解码为utf8字符串[m
[32m+[m[32m        return base64.b64encode(file.read()).decode("utf-8")[m
[32m+[m
[32m+[m
[32m+[m[32mdef decode_and_save_base64(base64_str, save_path):[m
[32m+[m[32m    with open(save_path, "wb") as file:[m
[32m+[m[32m        file.write(base64.b64decode(base64_str))[m
[32m+[m
[32m+[m
[32m+[m[32mdef call_api(api_endpoint, **payload):[m
[32m+[m[32m    # 词典转JSON，再转字符串[m
[32m+[m[32m    data = json.dumps(payload).encode("utf-8")[m
[32m+[m[32m    response = requests.post([m
[32m+[m[32m        f"{webui_server_url}/{api_endpoint}",[m
[32m+[m[32m        headers={"Content-Type": "application/json"},[m
[32m+[m[32m        data=data,[m
[32m+[m[32m    )[m
[32m+[m[32m    print(response.content)[m
[32m+[m[32m    return response.json()[m
[32m+[m
[32m+[m
[32m+[m[32mdef call_txt2img_api(**payload):[m
[32m+[m[32m    response = call_api("sdapi/v1/txt2img", **payload)[m
[32m+[m[32m    print("response t2i", response)[m
[32m+[m[32m    for index, image in enumerate(response.get("images")):[m
[32m+[m[32m        save_path = os.path.join(out_dir_t2i, f"txt2img-{timestamp()}-{index}.png")[m
[32m+[m[32m        print("t2i image", image)[m
[32m+[m[32m        decode_and_save_base64(image, save_path=save_path)[m
[32m+[m
[32m+[m
[32m+[m[32mdef call_img2img_api(**payload):[m
[32m+[m[32m    response = call_api("sdapi/v1/img2img", **payload)[m
[32m+[m[32m    print("response i2i", response)[m
[32m+[m[32m    for index, image in enumerate(response.get("images")):[m
[32m+[m[32m        save_path = os.path.join(out_dir_i2i, f"img2img-{timestamp()}-{index}.png")[m
[32m+[m[32m        print("i2i image", image)[m
[32m+[m[32m        decode_and_save_base64(image, save_path=save_path)[m
[32m+[m
[32m+[m
[32m+[m[32mif __name__ == "__main__":[m
[32m+[m[32m    payload = {[m
[32m+[m[32m        # "prompt": "masterpiece, (best quality:1.1), 1girl <lora:lora_model:1>"[m
[32m+[m[32m        "prompt": "masterpiece, (best quality:1.1), 1girl ",[m
[32m+[m[32m        "negative_prompt": "",[m
[32m+[m[32m        "seed": 1,[m
[32m+[m[32m        "width": 512,[m
[32m+[m[32m        "height": 512,[m
[32m+[m[32m        "cfg_scale": 7,[m
[32m+[m[32m        "sampler_name": "DPM++ 2M Karras",[m
[32m+[m[32m        "n_iter": 1,[m
[32m+[m[32m        "batch_size": 1,[m
[32m+[m[32m    }[m
[32m+[m
[32m+[m[32m    call_txt2img_api(**payload)[m
[32m+[m
[32m+[m[32m    # TODO: 试一下是否可以获取远程的url[m
[32m+[m[32m    init_images = [[m
[32m+[m[32m        encode_file_to_base64(r"B:\path\to\img_1.png"),[m
[32m+[m[32m        # "https://image.can/also/be/a/http/url.png",[m
[32m+[m[32m    ][m
[32m+[m
[32m+[m[32m    batch_size = 2[m
[32m+[m[32m    payload = {[m
[32m+[m[32m        "prompt": "1girl, blue hair",[m
[32m+[m[32m        "seed": 1,[m
[32m+[m[32m        "steps": 20,[m
[32m+[m[32m        "width": 512,[m
[32m+[m[32m        "height": 512,[m
[32m+[m[32m        "denoising_strength": 0.5,[m
[32m+[m[32m        "n_iter": 1,[m
[32m+[m[32m        "init_images": init_images,[m
[32m+[m[32m        "batch_size": batch_size if len(init_images) == 1 else len(init_images),[m
[32m+[m[32m    }[m
[32m+[m[32m    # TODO: 暂不处理[m
[32m+[m[32m    # call_img2img_api(**payload)[m
