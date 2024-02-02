# 输入文字，生成srt
import os
import pysrt
from pysrt import SubRipTime, SubRipItem
from pydub import AudioSegment
from scripts.config_loader import loader_config


def process_text(paragraphs, subs):
    async_tasks = []

    # 获取时间
    for index, paragraph in enumerate(paragraphs):
        audio = AudioSegment.from_file(filename)
        audio_duration = len(audio) / 1000  # 转换为秒

        # 设置字幕开始和结束时间
        start_time = pysrt.srttime.SubRipTime(milliseconds=0)
        end_time = SubRipTime(seconds=audio_duration)

        # 如果已有字幕，取上一个字幕的结束时间作为当前字幕的开始时间
        if subs:
            start_time = subs[-1].end
            end_time = SubRipTime(
                seconds=((subs[-1].end.ordinal / 1000) + audio_duration)
            )

        print(f"index: {index} start_time: {start_time} end_time: {end_time}")
        # 添加字幕
        subs.append(
            SubRipItem(
                index=len(subs) + 1, start=start_time, end=end_time, text=paragraph
            )
        )


if __name__ == "__main__":
    config = loader_config()
    input_path = config.get("input", {}).get("input_path", "")
    novel_text = config.get("input", {}).get("input_text", "")
    output_path = config.get("output", {}).get("srt_path", "")

    # 初始化 SRT 字幕对象
    subs = pysrt.SubRipFile()
    combined_audio = AudioSegment.silent()

    # 运行异步程序
    process_text(novel_text, subs, output_path)

    for index in range(len(subs)):
        filename = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            config["output"]["save_path"],
            f"{config['output']['name']}_{index}.mp3",
        )
        segment = AudioSegment.from_file(filename)
        combined_audio += segment

    # 保存字幕文件为 SRT 格式
    subs.save(output_path)
