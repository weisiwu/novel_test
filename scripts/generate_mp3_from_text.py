import os
import pyttsx3
from gtts import gTTS, lang
from config_loader import get_mp3_config


def generate_by_gTTs(text, speed, volumn, save_path):
    tts = gTTS(text, lang="zh-CN")
    tts.save(save_path)
    print(lang.tts_langs())

    pass


def generate_by_pyttsx3(text, speed, volumn, save_path):
    engine = pyttsx3.init()
    engine.setProperty("voice", "zh")  # 设置引擎为中文
    engine.setProperty("rate", speed)  # 设置语速
    engine.setProperty("volume", volumn)  # 设置音量

    engine.save_to_file(text, save_path)
    engine.runAndWait()
    # 长文本转换，需要分段执行
    # while "output.mp3" not in os.listdir(save_path):
    #     socketio.sleep(1)


def generate_by_ibm_watson_tts():
    pass


def generate_by_ms_azure_tts():
    pass


if __name__ == "__main__":
    input_text, speed, volumn, save_path = get_mp3_config()
    # generate_by_pyttsx3(input_text, speed, volumn, save_path)
    generate_by_gTTs(input_text, speed, volumn, save_path)
