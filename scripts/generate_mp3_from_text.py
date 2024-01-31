import torch
from TTS.api import TTS
from config_loader import get_mp3_config


# https://github.com/coqui-ai/TTS
def generate_by_coqui_TTS(text, output, speaker_path):
    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # List available 🐸TTS models
    print(TTS().list_models())

    # Init TTS
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    print("speaker_path: ", speaker_path)
    # Run TTS
    # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
    # Text to speech list of amplitude values as output
    # Text to speech to a file
    tts.tts_to_file(
        text=text, speaker_wav=speaker_path, language="zh", file_path=output
    )


if __name__ == "__main__":
    input_text, speed, volumn, save_path, speaker_path = get_mp3_config()
    print(input_text)
    print(save_path)
    print(speaker_path)
    generate_by_coqui_TTS(input_text, save_path, speaker_path)
