import os
import pyttsx3
from pydub import AudioSegment

text_file_path = os.path.join(os.path.dirname(__file__), "..", "file.txt")
output_file_path = os.path.join(os.path.dirname(__file__), "output.mp3")
wav_path = os.path.join(os.path.dirname(__file__), "output.wav")

engine = pyttsx3.init()
voices = engine.getProperty("voices")

for voice in voices:
    print("ID:", voice.id, "Name:", voice.name, "Lang:", voice.languages)

engine.setProperty(
    "voice",
    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0",
)

engine.setProperty("rate", 150)

with open(
    os.path.join(os.path.dirname(__file__), text_file_path), "r", encoding="utf-8"
) as file:
    text = file.read()
    engine.say(text)

engine.save_to_file(text, wav_path)
engine.runAndWait()

sound = AudioSegment.from_wav(wav_path)
sound.export(output_file_path, format="mp3")
