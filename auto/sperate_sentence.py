import os
import jieba
import re

novel_path = os.path.join(os.path.dirname(__file__), "file.txt")


def segment_chinese_novel(text):
    # 将文本按段落分割
    paragraphs = re.split(r"\n+", text)

    segmented_text = []

    for paragraph in paragraphs:
        # 使用jieba分词
        words = jieba.cut(paragraph)
        # 将分词结果连接起来形成句子
        sentence = "".join(words)
        # 将句子按标点符号分割
        sentences = re.split(r"[。！？；]", sentence)
        # 过滤空字符串
        sentences = [s.strip() for s in sentences if s.strip()]
        # 将分好的句子加入结果列表
        segmented_text.extend(sentences)

    return segmented_text


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(__file__), novel_path), "r", encoding="utf-8"
    ) as file:
        novel_text = file.read()
        # 对示例文本进行分段和分句
        result = segment_chinese_novel(novel_text)
        # 打印结果
        for idx, sentence in enumerate(result, 1):
            print(f"句子 {idx}: {sentence}")
