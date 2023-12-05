import os
import jieba
from collections import Counter

text_file_path = os.path.join(os.path.dirname(__file__), "..", "file.txt")
stop_words_file_path = os.path.join(os.path.dirname(__file__), "baidu_stopwords.txt")


# 1、生成基准图像，获取seed
# 2、每句话抽取2-3个关键词
# 3、对这2-3个关键词进行生成。记录seed。不断炼金
# 4、记录下这些图片，设定展示方式，要避免幻灯片的感觉
def extract_keywords_chinese(text):
    # 分词
    words = jieba.cut(text)

    # 去除停用词，自定义中文停用词列表
    # 中文停用词: https://github.com/goto456/stopwords
    with open(
        os.path.join(os.path.dirname(__file__), stop_words_file_path),
        "r",
        encoding="utf-8",
    ) as _file:
        stop_words_text = _file.read()
        stop_words = set(stop_words_text.split())
        words = [
            word.lower()
            for word in words
            if word.isalpha() and word.lower() not in stop_words
        ]

    # 计算词频
    freq_dist = Counter(words)

    # 获取前 N 个关键词
    top_keywords = freq_dist.most_common(100)  # 选择前5个关键词
    return [keyword for keyword, freq in top_keywords]


with open(
    os.path.join(os.path.dirname(__file__), text_file_path), "r", encoding="utf-8"
) as file:
    text = file.read()
    keywords = extract_keywords_chinese(text)
    print("关键词:", keywords)
