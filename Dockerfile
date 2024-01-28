# 使用官方 Python 运行时作为父镜像
FROM alpine:3.19
FROM python:3.10-slim-bookworm

LABEL maintainer="weisiwu <siwu.wsw@gmail.com>"

RUN mkdir -p /etc/apk

RUN echo 'http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.19/main/' > /etc/apk/repositories \
    && echo 'http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.19/community/' >> /etc/apk/repositories

RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y vim && \
    apt-get install -y wget && \
    apt-get install -y ffmpeg && \
    apt-get install -y espeak && \
    apt-get install -y libespeak1 && \
    apt-get install -y unzip


# 下载espeak中文语言资料包
RUN mkdir -p /usr/share/espeak-data/
RUN git clone 'https://github.com/caixxiong/espeak-data' /usr/share/espeak-data/
RUN cd /usr/share/espeak-data/espeak-data/ && unzip espeak-data.zip && mv espeak-data/* ..
RUN cp -r /usr/share/espeak-data/* /usr/lib/x86_64-linux-gnu/espeak-data

# 不知道是否可以这样执行？
# RUN ./init.py

# 设置工作目录为 /app
WORKDIR /novel_test

# 将当前目录内容复制到位于 /app 的容器中
COPY . /novel_test

# 安装 requirements.txt 中指定的任何所需包
RUN pip install --no-cache-dir -r requirements.txt

# 保持在后台持续运行
CMD ["sleep", "infinity"]
