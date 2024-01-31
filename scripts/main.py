# novel_test主入口
from pathlib import *
from scripts.config_loader import loader_config


# 从配置读取小说文本
def read_novel_from_file():
    pass


# 切分小说为分句
def novel_split():
    pass


def generate_mp3_from_text():
    pass


def generate_srt_from_text():
    pass


# 对所有分句创建mp3、srt
def generate_mp3_srt():
    srt = []
    mp3 = []
    # 向空序列附加
    for part in parts:
        generate_mp3_from_text()
        generate_srt_from_text()
    pass


if __name__ == "__main__":
    parts = []
    generate_mp3_srt(parts)
