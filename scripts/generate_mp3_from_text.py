import os
import pyttsx3
from pydub import AudioSegment
from config_loader import loader_config

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

engine.setProperty("rate", 150)


def generate_text_mp3(text, wav_path, mp3_path):
    engine.say(text)

    engine.save_to_file(text, wav_path)
    engine.runAndWait()

    sound = AudioSegment.from_wav(wav_path)
    sound.export(mp3_path, format="mp3")

# 上面的都是之前的实现。现在将市面上知名度较高的tts库全部调用一次，再决定使用什么？

def generate_by_gTTs():
    pass

def generate_by_pyttsx3():
    pass

def generate_by_ibm_watson_tts():
    pass

def generate_by_ms_azure_tts():
    pass

if __name__ == "__main__":
    config = loader_config()

    file_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        config["input"]["save_path"],
        config["input"]["file_name"],
    )
    wav_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        config["output"]["save_path"],
        f"{config['output']['name']}.wav",
    )
    mp3_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        config["output"]["save_path"],
        f"{config['output']['name']}.mp3",
    )

    with open(file_path, "r", encoding="utf8") as f:
        generate_text_mp3(f.read(), wav_path, mp3_path)
