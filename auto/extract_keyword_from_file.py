import os
import jieba.analyse

text_file_path = r"C:\Users\Administrator\Desktop\github\novel_test\file.txt"

with open(
    os.path.join(os.path.dirname(__file__), text_file_path), "r", encoding="utf-8"
) as file:
    text = file.read()
    # 使用 jieba 提取关键词
    keywords = jieba.analyse.extract_tags(text, topK=5)
    print("关键词:", keywords)
