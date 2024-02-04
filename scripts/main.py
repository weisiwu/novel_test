# novel_test主入口
import os
import shutil
from pathlib import *
from pydub import AudioSegment
from novel_split import novel_split
from config_loader import loader_config
from generate_mp3_from_text import generate_by_coqui_TTS
from generate_srt_from_text import generate_srt_from_text

if __name__ == "__main__":
    config = loader_config()
    tmp_wav_path = Path(__file__).parent / "tmp_wav"
    mp3_path = config.get("output", {}).get("mp3_path", "")
    srt_path = config.get("output", {}).get("srt_path", "")
    speaker_path = config.get("output", {}).get("speaker_path", "")
    not os.path.isdir(tmp_wav_path) and os.makedirs(tmp_wav_path)
    srt_current_time = 0  # 当前字幕时间

    # 断句后依次对每句生成语音和字幕
    sentences = novel_split()
    for index, sentence in enumerate(sentences):
        tmp_file_path = tmp_wav_path / f"tmp_{index}.wav"
        generate_by_coqui_TTS(
            text=sentence,
            output=tmp_file_path,
            speaker_path=speaker_path,
        )
        segment_len = len(AudioSegment.from_wav(tmp_file_path))
        srt_current_time += segment_len
        print("segment_len: ", segment_len, "srt_current_time: ", srt_current_time)
        # 追加字幕
        generate_srt_from_text(text=sentence, time=srt_current_time, srt_path=srt_path)

    # 合并音频文件
    for file_path in os.listdir(tmp_file_path):
        combined_audio = combined_audio + AudioSegment.from_wav(file_path)
    combined_audio.export(mp3_path, format="mp3")

    # 拼接完毕后，删除临时wav文件
    shutil.rmtree(tmp_wav_path)

    segment_times = generate_by_coqui_TTS(mp3_path, speaker_path)
    generate_srt_from_text(srt_path)
