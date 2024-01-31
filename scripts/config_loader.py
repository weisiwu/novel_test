import os
import yaml
from pathlib import *

base_path = Path(__file__).parent.parent
config_path = base_path / "project.yml"
input_path = base_path / "input.txt"
output_path = base_path / "output"
print("base_path", input_path)


# # 读取yml内容，并导出
def loader_config():
    config = {}

    if os.path.isfile(config_path):
        with open(config_path, "r", encoding="utf8") as f:
            config = yaml.load(f.read(), Loader=yaml.Loader)
            filename = config["output"]["filename"]
            config["output"]["srt_path"] = output_path / f"{filename}.srt"
            config["output"]["mp3_path"] = output_path / f"{filename}.mp3"
            config["output"]["mkv_path"] = output_path / f"{filename}.mkv"

            with open(input_path, "r", encoding="utf8") as input_f:
                config["input"] = {
                    "input_path": input_path,
                    "input_text": input_f.read(),
                }

    return config


def get_mp3_config():
    config = loader_config()
    output = config.get("output", {})
    input = config.get("input", {})

    return [
        input.get("input_text"),
        output.get("speed"),
        output.get("volume"),
        output.get("mp3_path"),
    ]


def get_srt_config():
    config = loader_config()
    output = config.get("output", {})
    input = config.get("input", {})

    return [
        input.get("input_text"),
        output.get("srt_path"),
    ]
