import os
import shutil
from pathlib import *
from pydub import AudioSegment
from novel_split import novel_split
from config_loader import loader_config
from generate_mp3_from_text import generate_by_coqui_TTS
from generate_srt_from_text import add_text_to_srt, save_srt

if __name__ == "__main__":
    config = loader_config()
    tmp_wav_path = Path(__file__).parent / "tmp_wav"
    mp3_path = config.get("output", {}).get("mp3_path", "")
    srt_path = config.get("output", {}).get("srt_path", "")
    speaker_path = config.get("output", {}).get("speaker_path", "")
    not os.path.isdir(tmp_wav_path) and os.makedirs(tmp_wav_path)

    # 断句后依次对每句生成语音和字幕
    sentences = novel_split()
    for index, sentence in enumerate(sentences):
        tmp_file_path = tmp_wav_path / f"{index}.wav"
        generate_by_coqui_TTS(
            text=sentence,
            output=tmp_file_path,
            speaker_path=speaker_path,
        )
        segment_len = len(AudioSegment.from_wav(tmp_file_path)) / 1000  # 转换为秒
        # 追加字幕
        add_text_to_srt(text=sentence, segment_len=segment_len)

    # 合并音频文件
    combined_audio = AudioSegment.silent(duration=0)
    for file_name in range(0, len(os.listdir(tmp_wav_path))):
        combined_audio = combined_audio + AudioSegment.from_wav(
            tmp_wav_path / f"{file_name}.wav"
        )
    combined_audio.export(mp3_path, format="wav")

    # 保存字幕文件
    save_srt(srt_path)

    # 拼接完毕后，删除临时wav文件
    shutil.rmtree(tmp_wav_path)
