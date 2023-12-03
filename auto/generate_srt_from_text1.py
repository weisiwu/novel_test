import os
import spacy
import jieba
import pyttsx3
from gtts import gTTS
from spacy.tokens import Doc

nlp = spacy.load("en_core_web_sm")


def jieba_tokenizer(text):
    words = list(jieba.cut(text))
    return Doc(nlp.vocab, words=words)


nlp.tokenizer = jieba_tokenizer


def parse_text_to_subtitles(text):
    """
    从纯文本中解析字幕数据。

    Parameters:
    - text: 包含字幕信息的文本。

    Returns:
    - subtitles: 一个包含字幕信息的列表，每个字幕信息为一个字典，包含 'text' 键。
    """
    doc = nlp(text)

    subtitles = []
    for i, sentence in enumerate(doc.sents, start=1):
        subtitles.append({"text": sentence.text.strip()})

    return subtitles


def generate_srt_with_speed(subtitles, output_file, speed=1.5):
    """
    生成带有语速参数的SRT格式的字幕文件

    Parameters:
    - subtitles: 一个包含字幕信息的列表，每个字幕信息为一个字典，包含 'text' 键。
    - output_file: 要保存的SRT文件路径。
    - speed: 语速参数，可以调整为合适的值，默认为1.5。
    """
    with open(output_file, "w", encoding="utf-8") as f:
        for i, subtitle in enumerate(subtitles, start=1):
            # 使用gTTS生成音频文件
            tts = gTTS(text=subtitle["text"], lang="zh", slow=False)
            tts.speed = speed
            audio_file_path = f"temp_audio_{i}.mp3"
            tts.save(audio_file_path)

            # 输出字幕文本到文件
            f.write(f"{i}\n")

            # 输出时间戳和结束时间
            start_time = (i - 1) * 3
            end_time = i * 3
            f.write(f"{start_time:02d}:00:00,000 --> {end_time:02d}:00:00,000\n")

            # 输出字幕文件路径
            f.write(f"{subtitle['text']}\n\n")


def generate_srt_from_text(text, output_file):
    """
    从纯文本中生成SRT格式的字幕文件。

    Parameters:
    - text: 包含字幕信息的文本。
    - output_file: 要保存的SRT文件路径。
    """
    subtitles = parse_text_to_subtitles(text)
    generate_srt_with_speed(subtitles, output_file)


# 生成SRT文件
output_file_path = os.path.join(os.path.dirname(__file__), "output.srt")
text_file_path = r"C:\Users\Administrator\Desktop\github\novel_test\file.txt"

with open(
    os.path.join(os.path.dirname(__file__), text_file_path), "r", encoding="utf-8"
) as file:
    text = file.read()
    generate_srt_from_text(text, output_file_path)
