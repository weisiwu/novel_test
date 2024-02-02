import os
from pysrt import srttime, SubRipFile, SubRipTime, SubRipItem
from novel_split import novel_split
from config_loader import loader_config


def generate_srt_from_text(segment_times, output_path):
    subs = SubRipFile()
    paragraphs = novel_split()
    print("paragraphs===>", len(paragraphs), paragraphs)
    print("segment_times===>", segment_times)

    # # 获取时间
    for index, sgement_time in enumerate(segment_times):
        sgement_time = sgement_time / 1000  # 转换为秒
        print(f"{index}===> {sgement_time}秒")

        # 设置字幕开始和结束时间
        start_time = srttime.SubRipTime(milliseconds=0)
        end_time = SubRipTime(seconds=sgement_time)

        # 如果已有字幕，取上一个字幕的结束时间作为当前字幕的开始时间
        if subs:
            start_time = subs[-1].end
            end_time = SubRipTime(
                seconds=((subs[-1].end.ordinal / 1000) + sgement_time)
            )

        print(f"index: {index} start_time: {start_time} end_time: {end_time}")
        # 添加字幕
        subs.append(
            SubRipItem(
                index=len(subs) + 1,
                start=start_time,
                end=end_time,
                text=paragraphs[index],
            )
        )

    # 保存字幕文件为 SRT 格式
    subs.save(output_path)


if __name__ == "__main__":
    config = loader_config()
    output_path = config.get("output", {}).get("srt_path", "")

    # demo数据
    segment_times = []
    generate_srt_from_text(segment_times, output_path)
