import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print("device", device)

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# Text to speech to a file
tts.tts_to_file(
    # text="你好，我的阿斯顿发发啊!",
    text="""""",
    speaker_wav="sample.wav",
    language="zh",
    file_path="output.wav",
)
