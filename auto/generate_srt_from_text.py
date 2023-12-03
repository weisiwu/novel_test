import os
import re
import spacy
import pyttsx3
import pysrt
from pysrt import SubRipTime, SubRipItem
import jieba
import asyncio
import time
from pydub import AudioSegment
from spacy.tokens import Doc

# 加载 spaCy 模型
nlp = spacy.load("en_core_web_sm")
output_path = os.path.join(os.path.dirname(__file__), "output")
output_srt_path = os.path.join(os.path.dirname(__file__), "output", "output.srt")
novel_path = r"C:\Users\Administrator\Desktop\github\novel_test\file.txt"


def jieba_tokenizer(text):
    words = list(jieba.cut(text))
    return Doc(nlp.vocab, words=words)


nlp.tokenizer = jieba_tokenizer


# 异步语音合成函数
async def async_text_to_speech(text, filename):
    engine = pyttsx3.init()
    engine.setProperty(
        "voice",
        "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0",
    )
    engine.save_to_file(text, filename)
    engine.runAndWait()


# 异步遍历 spaCy 处理后的文本
async def process_text(novel_text, subs, output_path):
    async_tasks = []

    # 将文本按段落分割
    paragraphs = re.split(r"\n+", novel_text)

    for paragraph in paragraphs:
        # 使用jieba分词
        words = jieba.cut(paragraph)
        # 将分词结果连接起来形成句子
        sentence = "".join(words)
        # 将句子按标点符号分割
        sentences = re.split(r"[。！？；]", sentence)
        # 过滤空字符串
        sentences = [s.strip() for s in sentences if s.strip()]
        sentences = sentences[0] if sentences else None

        index = len(subs) + 1
        filename = os.path.join(output_path, f"output_{index}.mp3")

        # 异步语音合成
        async_tasks.append(
            asyncio.create_task(async_text_to_speech(sentences, filename))
        )

        audio = AudioSegment.from_file(filename)
        audio_duration = len(audio) / 1000  # 转换为秒

        # 设置字幕开始和结束时间
        start_time = pysrt.srttime.SubRipTime(milliseconds=0)
        end_time = SubRipTime(seconds=audio_duration)

        # 如果已有字幕，取上一个字幕的结束时间作为当前字幕的开始时间
        if subs:
            start_time = subs[-1].end
            end_time = SubRipTime(
                seconds=((subs[-1].end.ordinal / 1000) + audio_duration)
            )

        print(f"index: {index} start_time: {start_time} end_time: {end_time}")
        # 添加字幕
        subs.append(
            SubRipItem(
                index=len(subs) + 1, start=start_time, end=end_time, text=sentences
            )
        )

    # 等待所有异步任务完成
    await asyncio.gather(*async_tasks)


with open(
    os.path.join(os.path.dirname(__file__), novel_path), "r", encoding="utf-8"
) as file:
    novel_text = file.read()
    # 初始化 SRT 字幕对象
    subs = pysrt.SubRipFile()

    # 运行异步程序
    asyncio.run(process_text(novel_text, subs, output_path))

    time.sleep(5)

    combined_audio = AudioSegment.silent()
    # audio_segments = []

    for index in range(1, len(subs) + 1):
        filename = os.path.join(output_path, f"output_{index}.mp3").replace("\\", "/")
        segment = AudioSegment.from_file(filename)
        combined_audio += segment

    # 保存合并后的音频文件
    combined_audio.export(
        os.path.join(output_path, "output_combined.mp3"), format="mp3"
    )

    # 保存字幕文件为 SRT 格式
    subs.save(output_srt_path)
