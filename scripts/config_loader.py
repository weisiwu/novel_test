import os
import yaml

config_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../", "project.yml")
)
input_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../", "input.txt")
)


# 读取yml内容，并导出
def loader_config():
    config = {}

    if os.path.isfile(config_path):
        with open(config_path, "r", encoding="utf8") as f:
            config = yaml.load(f.read(), Loader=yaml.Loader)
            filename = config["output"]["filename"]
            output_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "../", filename)
            )
            output_srt_path = os.path.abspath(output_path, "srt")
            output_mp3_path = os.path.abspath(output_path, "mp3")
            output_mkv_path = os.path.abspath(output_path, "mkv")
            config["output"]["srt_path"] = output_srt_path
            config["output"]["mp3_path"] = output_mp3_path
            config["output"]["mkv_path"] = output_mkv_path

            with open(input_path, "r", encoding="utf8") as input_f:
                config["input"] = {
                    "input_path": input_path,
                    "input_text": input_f.read(),
                }

    return config


def get_common_config():
    config = loader_config()
    output = config.get("output", {})
    input = config.get("input", {})

    return [
        input.get("input_text"),
        output.get("speed"),
        output.get("volume"),
        output.get("background_music"),
    ]
