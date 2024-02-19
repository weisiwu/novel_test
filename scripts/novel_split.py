# 输入小说文本拆分为分句
import re
import zhon
from config_loader import loader_config


def novel_split():
    config = loader_config()
    novel = config.get("input", {}).get("input_text", "")
    print("入参是什么", novel)
    sentences = re.findall(zhon.hanzi.sentence, novel)
    print("分句的时候，是否缺少最后一局", sentences)

    return [sentence.strip("”") for index, sentence in enumerate(sentences)]
