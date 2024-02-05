import os
import torch
from pathlib import *
from TTS.api import TTS
from pydub import AudioSegment
from config_loader import get_mp3_config

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)


# https://github.com/coqui-ai/TTS
def generate_by_coqui_TTS(text, output, speaker_path):
    tts.tts_to_file(
        text=text, speaker_wav=speaker_path, language="zh", file_path=output
    )

    AudioSegment.from_wav(output).export(output, format="mp3")


if __name__ == "__main__":
    input_text, speed, volumn, save_path, speaker_path = get_mp3_config()
    generate_by_coqui_TTS(input_text, save_path, speaker_path)
