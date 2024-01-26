import os
import pyttsx3
from pydub import AudioSegment
from config_loader import get_common_config


def generate_by_gTTs():
    pass


def generate_by_pyttsx3(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    for voice in voices:
        print("ID:", voice.id, "Name:", voice.name, "Lang:", voice.languages)
        if "chinese" in voice.name.lower():  # 查找包含“chinese”的语音
            engine.setProperty("voice", voice.id)
            break

    engine.setProperty(
        "voice",
        "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0",
    )

    # engine.setProperty("rate", 150)
    # engine.say(text)
    # engine.save_to_file(text, wav_path)
    # engine.runAndWait()

    # sound = AudioSegment.from_wav(wav_path)
    # sound.export(mp3_path, format="mp3")
    pass


def generate_by_ibm_watson_tts():
    pass


def generate_by_ms_azure_tts():
    pass


if __name__ == "__main__":
    input_text, *rest_res = get_common_config()
    generate_by_pyttsx3(input_text)
