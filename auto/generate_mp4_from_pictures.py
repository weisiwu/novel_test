from moviepy.editor import (
    ImageSequenceClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
    ColorClip,
)
from moviepy.video.tools.subtitles import SubtitlesClip

# 创建视频剪辑
# clip = ImageSequenceClip(image_files, fps=1)  # 每秒帧数 fps

# # 写入文件（输出为 MP4）
# clip.write_videofile("output_video.mp4")

if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from config_loader import loader_config

    config = loader_config()

    audio_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        config["output"]["save_path"],
        config["output"]["combine_file"],
    )
    srt_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        config["output"]["save_path"],
        config["output"]["srt_file_name"],
    )
    img_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), config["output"]["save_path"], "img"
    )
    image_files = [
        os.path.abspath(os.path.join(img_path, img)) for img in os.listdir(img_path)
    ]
    video_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        config["output"]["save_path"],
        f"{config['output']['name']}.{config['output']['file_type']}",
    )
    print("image_files", image_files)

    audio_clip = AudioFileClip(audio_path)

    # 创建一个背景视频剪辑（黑色背景）
    bg_clip = ColorClip(
        size=(1920, 1080), color=(0, 0, 0), duration=audio_clip.duration
    )
    # bg_clip = ImageSequenceClip(image_files, fps=1)  # 每秒帧数 fps

    # 创建字幕剪辑
    def make_textclip(txt):
        return TextClip(txt, font="Arial", fontsize=24, color="white")

    with open(srt_path, "r", encoding="utf-8") as srt_file:
        subtitles = srt_file.read()

    subtitles_clip = SubtitlesClip(subtitles, make_textclip)

    # 将字幕和背景组合
    video = CompositeVideoClip([bg_clip, subtitles_clip.set_pos(("center", "bottom"))])

    # 设置视频的音频
    video = video.set_audio(audio_clip)

    # 写入文件（输出为 MP4）
    video.write_videofile(video_path, fps=24)
