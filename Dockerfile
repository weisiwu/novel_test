FROM ubuntu:18.04
FROM python:3.10-slim-bookworm

LABEL maintainer="weisiwu <siwu.wsw@gmail.com>"

RUN mkdir -p /etc/apk

RUN cp /etc/apt/sources.list.d/debian.sources /etc/apt/sources.list.d/debian.sources.bak
RUN sed -i 's|http://deb.debian.org/debian|http://mirrors.aliyun.com/debian|g' /etc/apt/sources.list.d/debian.sources

RUN apt-get update && \
    apt-get install -y git vim wget ffmpeg espeak libespeak1 unzip

# 本地存在model时，使用这个进行编译
RUN mkdir -p /root/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v2
COPY ./models/xtts_v2/* /root/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v2
# 本地没有model时，使用网络进行下载
# RUN wget https://hf-mirror.com/coqui/XTTS-v2/resolve/main/config.json?download=true 
# RUN wget https://hf-mirror.com/coqui/XTTS-v2/resolve/main/hash.md5?download=true
# RUN wget https://hf-mirror.com/coqui/XTTS-v2/resolve/main/vocab.json?download=true
# RUN wget https://hf-mirror.com/coqui/XTTS-v2/resolve/main/model.pth?download=true

# 设置工作目录为 /app
WORKDIR /novel_test

# 将当前目录内容复制到位于 /app 的容器中
COPY . /novel_test

# 安装 requirements.txt 中指定的任何所需包
RUN pip install --no-cache-dir -r requirements.txt

# 保持在后台持续运行
CMD ["sleep", "infinity"]
