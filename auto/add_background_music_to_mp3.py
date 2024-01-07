from pydub import AudioSegment


def add_background_music(
    original_audio_path,
    background_music_path,
    output_path,
    background_volume_percentage=15,
):
    # 读取原始音频和背景音乐
    original_audio = AudioSegment.from_file(original_audio_path)
    background_music = AudioSegment.from_file(background_music_path)

    # 计算背景音乐的目标音量
    target_volume = original_audio.dBFS - background_volume_percentage

    # 调整背景音乐的音量
    adjusted_background_music = background_music - (
        background_music.dBFS - target_volume
    )

    # 计算需要重复背景音乐的次数
    repeat_times = len(original_audio) // len(background_music)

    # 循环叠加背景音乐
    combined_audio = AudioSegment.silent(duration=0)
    for _ in range(repeat_times + 1):
        combined_audio = combined_audio + adjusted_background_music

    # 调整背景音乐长度，使其与原始音频一致
    combined_audio = combined_audio[: len(original_audio)]

    # 将背景音乐混合到原始音频中
    final_audio = original_audio.overlay(combined_audio)

    # 导出合成后的音频
    final_audio.export(output_path, format="mp3")


if __name__ == "__main__":
    # 示例调用
    original_audio_path = r"C:\Users\Administrator\Desktop\github\novel_test\auto\output\output_combined.mp3"
    background_music_path = (
        r"C:\Users\Administrator\Desktop\github\novel_test\music\take me higher.mp3"
    )
    output_path = r"C:\Users\Administrator\Desktop\github\novel_test\auto\output\output_background_combined.mp3"

    add_background_music(original_audio_path, background_music_path, output_path)
