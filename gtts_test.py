# from gtts import gTTS

# text = """
# “啊！”

#     潜行者冰冷尖利如钢铁般坚硬的触手穿透身体的刹那，让叶钟鸣不可抑制地喊了出来。

#     朦胧间，入手处却是一片温润滑腻。

#     叶钟鸣的视线渐渐有了焦点，他看见了一张曾经熟悉的美丽脸庞。

#     她？

#     她不是很久前就死了吗？

#     仿佛要确认什么似的，叶钟鸣想要从这具无比熟悉的身体上挺起，可却被女人用四肢紧紧地环住。

#     叶钟鸣有些茫然得停止了动作，只是在目光扫视中，恍然明白了一些事情。

#     画着卡通图案的水杯、夜光的电子闹钟、素色花纹的窗帘、还有怀中的女人，都把叶钟鸣带到了一个曾经经历过的场景。

#     2020年，9月10日下午。

#     那场旷世之灾发生的一个小时前。

#     不应该是出任务了吗？之后被那些该死的虫子袭击，好不容易冲了出去却被潜伏者偷袭，从地下伸出的触手刺穿了身体，以自己的经验那绝对是致命伤。

#     可是现在······这场记忆深处的白日激情，一切仿佛都回到了十年前，那个灾难来临前最后的美丽下午。

#     常年养成的冷静让叶钟鸣迅速地思考着，只用了十秒钟，他就确定了，这不是什么仿佛回到十年前，而就是回到了十年前！

#     看了一眼闹钟上的时间，2020年9月10日，15点35分钟，距离那个刻骨铭心的时间，还有一个小时零5分钟。

#     2020年9月10日16点40分，一件恐怖的事情将会发生，之后，地球就彻底陷入了冰冷的末世。

#     叶钟鸣呆滞半响，心中只有一个念头——这是上天给的眷顾，还是对自己的另一次惩罚？
# """
# language = 'zh-cn'

# tts = gTTS(text=text, lang=language, slow=False)
# tts.save("output.mp3")


# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# # Print available voices
# for voice in voices:
#     print("ID:", voice.id, "Name:", voice.name, "Lang:", voice.languages)

# engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0')

# # Set the speaking rate (optional)
# engine.setProperty('rate', 150)

# # Say something
# engine.say("""
# “啊！”

#     潜行者冰冷尖利如钢铁般坚硬的触手穿透身体的刹那，让叶钟鸣不可抑制地喊了出来。

#     朦胧间，入手处却是一片温润滑腻。

#     叶钟鸣的视线渐渐有了焦点，他看见了一张曾经熟悉的美丽脸庞。

#     她？

#     她不是很久前就死了吗？

#     仿佛要确认什么似的，叶钟鸣想要从这具无比熟悉的身体上挺起，可却被女人用四肢紧紧地环住。

#     叶钟鸣有些茫然得停止了动作，只是在目光扫视中，恍然明白了一些事情。

#     画着卡通图案的水杯、夜光的电子闹钟、素色花纹的窗帘、还有怀中的女人，都把叶钟鸣带到了一个曾经经历过的场景。

#     2020年，9月10日下午。

#     那场旷世之灾发生的一个小时前。

#     不应该是出任务了吗？之后被那些该死的虫子袭击，好不容易冲了出去却被潜伏者偷袭，从地下伸出的触手刺穿了身体，以自己的经验那绝对是致命伤。

#     可是现在······这场记忆深处的白日激情，一切仿佛都回到了十年前，那个灾难来临前最后的美丽下午。

#     常年养成的冷静让叶钟鸣迅速地思考着，只用了十秒钟，他就确定了，这不是什么仿佛回到十年前，而就是回到了十年前！

#     看了一眼闹钟上的时间，2020年9月10日，15点35分钟，距离那个刻骨铭心的时间，还有一个小时零5分钟。

#     2020年9月10日16点40分，一件恐怖的事情将会发生，之后，地球就彻底陷入了冰冷的末世。

#     叶钟鸣呆滞半响，心中只有一个念头——这是上天给的眷顾，还是对自己的另一次惩罚？
#            """)

# # Wait for the speech to finish
# engine.runAndWait()

# 声音文档 https://cloud.google.com/text-to-speech/docs/voices
# from google.cloud import texttospeech

# client = texttospeech.TextToSpeechClient()

# input_text = texttospeech.SynthesisInput(text="Hello, this is a test.")
# voice = texttospeech.VoiceSelectionParams(
#     language_code="en-US", name="en-US-Wavenet-D",
# )

# audio_config = texttospeech.AudioConfig(
#     audio_encoding=texttospeech.AudioEncoding.LINEAR16
# )

# response = client.synthesize_speech(
#     input=input_text, voice=voice, audio_config=audio_config
# )

# with open("output.wav", "wb") as out_file:
#     out_file.write(response.audio_content)
