import torch
from pathlib import *
from TTS.api import TTS
from pathlib import *
from config_loader import get_mp3_config

base_path = Path(__file__).parent.parent
modelPath = base_path / "models/xtts_v2/moyunxi_new_3960.pth"
configPath = base_path / "models/xtts_v2/config.json"

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
# 微调模型
tts = TTS(model_path=modelPath, config_path=configPath).to(device)


# https://github.com/coqui-ai/TTS
def generate_by_coqui_TTS(text, output):
    tts.tts_to_file(
        text=text,
        file_path=output,
    )


if __name__ == "__main__":
    input_text, speed, volumn, save_path, speaker_path = get_mp3_config()
    generate_by_coqui_TTS(input_text, save_path, speaker_path)
