import os
from pysrt import SubRipFile, SubRipTime, SubRipItem

subs = SubRipFile()


def add_text_to_srt(text, segment_len):
    print("generate_srt_from_text==text", text)
    print("generate_srt_from_text==segment_len", segment_len)

    # 设置字幕开始和结束时间
    start_time = SubRipTime(milliseconds=0)
    end_time = SubRipTime(seconds=segment_len)
    # 如果已有字幕，取上一个字幕的结束时间作为当前字幕的开始时间
    if subs:
        start_time = subs[-1].end
        end_time = SubRipTime(seconds=((subs[-1].end.ordinal / 1000) + segment_len))
    # 添加字幕
    subs.append(
        SubRipItem(
            index=len(subs) + 1,
            start=start_time,
            end=end_time,
            text=text,
        )
    )


def save_srt(srt_path):
    print("generate_srt_from_text==srt_path", srt_path)
    # 保存字幕文件为 SRT 格式
    subs.save(srt_path)
