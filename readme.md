# 1、配置项目
打开 project.yml，在里面按照自己实际情况，进行配置。

# 2、安装环境
整体迁移到 docker 中，为解决这些问题:
1、chatgpt 需要有 secret-key 设置在环境变量中、不同机器要同步一次，过于麻烦
2、目前使用moviepy，生成mp4，并添加字幕，需要基于imagemagick，各个环境需要安装一次，并将imagemagick指向执行路径
3、后续要支持stable-diffustion，需要兼容pytorch,xform等等，环境复杂，跨机器无法运行
4、moviepy执行srtclip读取字幕文件时，编码使用系统默认，跨机器存在严重不同。（windows默认gbk）
5、例如hanlp之类的需要下载模型，现在是每个机器都需要安装一份。 

# 3、核心函数
[WIP]1、拆句子，读取文档内容，拆分句子list
    hanlp
[WIP]2、控制节奏
    视频的语速、背景音乐的高低、语气
3、生成srt: generate_srt_from_text.py
4、生成语音mp3: generate_mp3_from_text.py
[WIP]5、生成srt和mp3，对齐并封装为mkv: 
6、添加背景音乐: add_background_music_to_mp3.py
[WIP]7、chatgpt prompt 助理: generate_prompt_for_SD.py
    利用 chatgpt api，生成 sd prompt
[WIP]8、请求封装
    错误重试，直至成功
9、由图片生成视频: generate_mp4_from_pictures.py
10、DALL-E3模型生成图片: generate_pictures_from_chatgpt.py
    暂时因为收费价格和安全策略弃用。目前DALL-E-2/3生成单图价格范围在1毛-8毛之间，且调用API有时间限制，每分钟5条。

# 4、核心流程
![流程](./assets/novel_test.png)

1、构建镜像
docker build --no-cache -t novel_test .
2、运行镜像

向docker hub推送镜像
docker login
docker tag local-image:tag yourhubusername/repo-name:new-tag
docker push yourhubusername/repo-name:new-tag

在后台运行容器
docker run -d --name my-running-app my-python-app

接入容器
docker exec -it my-running-app bash

