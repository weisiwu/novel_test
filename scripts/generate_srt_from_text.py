import os
from pysrt import SubRipFile, SubRipTime, SubRipItem

def generate_srt_from_text(text, segment_len, srt_path):
    subs = SubRipFile()
    print("generate_srt_from_text==text", text)
    print("generate_srt_from_text==segment_len", segment_len)
    print("generate_srt_from_text==srt_path", srt_path)

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

    # 保存字幕文件为 SRT 格式
    subs.save(srt_path)

# 这里的demo肯定不对
# if __name__ == "__main__":
#     config = loader_config()
#     srt_path = config.get("output", {}).get("srt_path", "")

#     print("srt_path==> ", srt_path)
#     # demo数据
#     segment_times = []
#     generate_srt_from_text(srt_path)
