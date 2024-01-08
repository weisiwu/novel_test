from moviepy.editor import (
    ImageSequenceClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
)
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings
from mutagen.mp3 import MP3
from config_loader import loader_config

# 创建视频剪辑
# clip = ImageSequenceClip(image_files, fps=1)  # 每秒帧数 fps

# # 写入文件（输出为 MP4）
# clip.write_videofile("output_video.mp4")

if __name__ == "__main__":
    change_settings(
        {
            "IMAGEMAGICK_BINARY": r"C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/magick.exe"
        }
    )
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

    audio_clip = AudioFileClip(audio_path)

    # 每张图片展示的时间
    duration_per_image = MP3(audio_path).info.length / len(image_files)
    print("duration_per_image", duration_per_image)

    # 创建视频剪辑
    clip = ImageSequenceClip(
        image_files, durations=[duration_per_image] * len(image_files)
    )

    # 设置视频的 fps
    clip = clip.set_fps(24)

    # 创建字幕剪辑
    def make_textclip(txt):
        return TextClip(
            txt, font="./From_Cartoon_Blocks.ttf", fontsize=24, color="white"
        )

    subtitles_clip = SubtitlesClip(srt_path, make_textclip)

    # 将字幕和背景组合
    video = CompositeVideoClip([clip, subtitles_clip.set_pos(("center", "bottom"))])

    # 设置视频的音频
    video = video.set_audio(audio_clip)

    # 写入文件（输出为 MP4）
    video.write_videofile(video_path, fps=24)
