import os
import torch
import shutil
from pathlib import *
from pydub import AudioSegment
from TTS.api import TTS
from novel_split import novel_split
from config_loader import get_mp3_config


# https://github.com/coqui-ai/TTS
def generate_by_coqui_TTS(output, speaker_path):
    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # List available 🐸TTS models
    print(TTS().list_models())
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    tmp_wav_path = Path(__file__).parent / "tmp_wav"
    sentences = novel_split()
    segment_times = []

    not os.path.isdir(tmp_wav_path) and os.makedirs(tmp_wav_path)

    for index, sentence in enumerate(sentences):
        tts.tts_to_file(
            text=sentence,
            speaker_wav=speaker_path,
            language="zh",
            file_path=tmp_wav_path / f"tmp_{index}.wav",
        )

    # 生成完毕后，整体拼接
    combined_audio = AudioSegment.empty()
    audio_segments = [
        AudioSegment.from_wav(tmp_wav_path / file_path)
        for file_path in os.listdir(tmp_wav_path)
    ]
    for segment in audio_segments:
        combined_audio = combined_audio + segment
        segment_times.append(len(segment))

    combined_audio.export(output, format="mp3")

    # 拼接完毕后，删除临时wav文件
    shutil.rmtree(tmp_wav_path)

    print("segment_times==>", segment_times)
    return segment_times


if __name__ == "__main__":
    input_text, speed, volumn, save_path, speaker_path = get_mp3_config()
    generate_by_coqui_TTS(save_path, speaker_path)
