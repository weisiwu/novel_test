# novel_test主入口
from pathlib import *
from config_loader import loader_config
from generate_mp3_from_text import generate_by_coqui_TTS
from generate_srt_from_text import generate_srt_from_text

if __name__ == "__main__":
    config = loader_config()
    mp3_path = config.get("output", {}).get("mp3_path", "")
    srt_path = config.get("output", {}).get("srt_path", "")
    speaker_path = config.get("output", {}).get("speaker_path", "")

    segment_times = generate_by_coqui_TTS(mp3_path, speaker_path)
    generate_srt_from_text(segment_times, srt_path)
