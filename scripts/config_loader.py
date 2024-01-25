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
            config["input"] = input_path

    return config
