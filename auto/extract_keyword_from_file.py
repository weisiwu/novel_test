import os
import re
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

text_file_path = os.path.join(os.path.dirname(__file__), "..", "file.txt")
stop_words_file_path = os.path.join(os.path.dirname(__file__), "baidu_stopwords.txt")


# 词频-逆文档频率 TF-IDF
def extract_keywords_tfidf(words):
    text_for_tfidf = " ".join(words)
    # 使用TF-IDF向量化
    vectorizer = TfidfVectorizer()

    # 对分词后的文本进行 TF-IDF 计算
    vectorizer.fit_transform([text_for_tfidf])

    # 获取词汇表
    feature_names = vectorizer.get_feature_names_out()

    return feature_names


def chinese_sentence_split(text):
    # 使用正则表达式匹配中文句子
    pattern = r"[^！。？\n]+[！。？\n]"
    sentences = re.findall(pattern, text)

    return list(sentences)


def extract_keywords_sentence_tfidf(documents):
    # 创建 TF-IDF 向量化器
    vectorizer = TfidfVectorizer()

    # 存储每一句的关键词列表
    keywords_per_sentence = []

    for document in documents:
        # 中文分词
        words = jieba.cut(document)

        # 将分词结果转为空格分隔的字符串
        text_for_tfidf = " ".join(words)

        # 对每一句文本进行 TF-IDF 计算
        tfidf_matrix = vectorizer.fit_transform([text_for_tfidf])

        # 获取词汇表
        feature_names = vectorizer.get_feature_names_out()

        # 获取每一句的关键词
        keywords = [feature_names[i] for i in tfidf_matrix.nonzero()[1]]

        # 将关键词列表存储在 keywords_per_sentence 中
        keywords_per_sentence.append(keywords)

    return keywords_per_sentence


with open(
    os.path.join(os.path.dirname(__file__), text_file_path), "r", encoding="utf-8"
) as file:
    text = file.read()
    # 全文关键词按照文字顺序排列
    original_words_order = list(jieba.cut(text))
    keywords_tfidf = extract_keywords_tfidf(original_words_order)

    # 过滤并按照原始文档中的顺序重排 feature_names
    filtered_feature_names = [
        word for word in original_words_order if word in keywords_tfidf
    ]
    # print(filtered_feature_names)

    # 每句都抽取关键词
    # documents = chinese_sentence_split(text)
    # keywords_per_sentence = extract_keywords_sentence_tfidf(documents)

    # print(keywords_per_sentence)

    # // TODO:(wsw) 全文生成关键词，然后按照所在句子，进行二次排列
    # 寻找生成 sd prompt的方法，包括关键词映射
