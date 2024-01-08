import os
from hanlp import hanlp
from config_loader import loader_config

config = loader_config()

file_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    config["input"]["save_path"],
    config["input"]["file_name"],
)

with open(file_path, "r", encoding="utf8") as f:
    file_text = f.read()

split_sent = hanlp.load(hanlp.pretrained.eos.UD_CTB_EOS_MUL)


# 从配置文件中读取分句
def split_sentence():
    return split_sent(file_text)
