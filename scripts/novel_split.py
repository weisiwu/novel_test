# 输入小说文本拆分为分句
import re
import zhon
from config_loader import loader_config


def novel_split():
    config = loader_config()
    novel = config.get("input", {}).get("input_text", "")
    sentences = re.findall(zhon.hanzi.sentence, novel)

    return [sentence.strip("”") for index, sentence in enumerate(sentences)]
