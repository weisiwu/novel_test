做视频的时候配音和字幕生成太慢，又没找合适的配音工具，所以写了这个工具。  
产物是mkv文件，其中音轨和字幕都可以拆出来，方便二次编辑。  
效果参考视频。  

或者可以在线体验一下。  

# 1、下载安装
先下载这个镜像: [**镜像主页**](https://hub.docker.com/repository/docker/weisiwu/novel_test/general)    
```shell
# 下载
docker push weisiwu/novel_test:latest
```
然后开始编辑本地需要转化的文件，比如叫做`input.txt`  
准备就绪后，运行镜像，将`input.txt`挂载到`novel_test/input.txt`路径下。（直接用下面的命令，将`INPUT_PATH`替换为本地`input.txt`的绝对路径）

```shell
# 挂载input.txt
docker run -d -v INPUT_PATH:/novel_test/utils -v --name novel_test novel_test
```

TODO 输出位置没指定
-----------TODO-----------------------------------------------
## 2、构建/更新镜像
```shell
# 进入容器
docker exec -it novel_test bash
# 从Dockerfile构建镜像
docker build --no-cache -t novel_test .
# 保存运行中的容器为新镜像
docker commit 12345abcde novel_test:latest
docker login
# 推送镜像
docker tag novel_test:latest weisiwu/novel_test:0.0.1
docker push weisiwu/novel_test:0.0.1
```

# 2、配置使用
打开 project.yml，在里面按照自己实际情况，进行配置。字段含义如下
``` yaml
output:
  background_music: 'take me higher.mp3' # 背景音乐
  speed: 120 # 语速
  volume: 10 # 音量
```