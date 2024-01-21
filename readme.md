# 1、配置项目
打开 project.yml，在里面按照自己实际情况，进行配置。

# 2、安装环境
## 1、拉取镜像
[**镜像主页**](https://hub.docker.com/repository/docker/weisiwu/novel_test/general)

**1、拉取镜像**

```shell
docker push weisiwu/novel_test:tagname
```

**2、运行镜像**

```shell
# 常规启动镜像
docker run -d --name novel_test novel_test
# 指定 utils 对应本地的挂载目录启动
docker run -d -v C:\Users\Administrator\Desktop\github\novel_test\utils:/novel_test/utils --name novel_test novel_test
```

**3、接入到运行中的镜像**

```shell
docker exec -it novel_test bash
```

## 2、镜像打包和更新
**1、构建/更新镜像**

```shell
# 从Dockerfile构建镜像
docker build --no-cache -t novel_test .
# 保存运行中的容器为新镜像
docker commit 12345abcde novel_test:latest
```

**2、向docker hub推送镜像**

```shell
docker login
docker tag novel_test:latest weisiwu/novel_test:0.0.1
docker push weisiwu/novel_test:0.0.1
```

# 3、核心函数
1、拆句子
> 读取文档内容，拆分句子list

2、控制节奏  
> 视频的语速、背景音乐的高低、语气

3、生成srt
> generate_srt_from_text.py

4、生成语音mp3
> generate_mp3_from_text.py

5、生成srt和mp3，对齐并封装为mkv

6、添加背景音乐
> add_background_music_to_mp3.py

7、chatgpt prompt 助理
> 利用 chatgpt api，生成 sd prompt  
> generate_prompt_for_SD.py

8、请求封装
> 错误重试，直至成功

9、由图片生成视频
> generate_mp4_from_pictures.py

10、DALL-E3模型生成图片
> generate_pictures_from_chatgpt.py  
> 暂时因为收费价格和安全策略弃用。目前DALL-E-2/3生成单图价格范围在1毛-8毛之间，且调用API有时间限制，每分钟5条。

# 4、核心流程
![流程](./assets/images/novel_test.png)

# 5、文件路径
``` shell
├─assets 所有物料: 如readme引用的文件、背景音乐、字体文件等   
│  ├─background_music 背景音乐  
│  ├─font 字体文件  
│  └─images 图片  
├─documents prompts相关文档  
├─input 项目输入目录  
├─output 项目输出目录  
│  ├─img2img 图生图目录  
│  └─txt2img 文生图目录 
└─utils 所有功能代码  
```