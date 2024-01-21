import yaml


# 读取yml内容，并导出
def loader_config():
    with open("../project.yml", "r", encoding="utf8") as f:
        return yaml.load(f.read(), Loader=yaml.Loader)
