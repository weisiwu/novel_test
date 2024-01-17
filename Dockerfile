# 使用官方 Python 运行时作为父镜像
FROM alpine:3.19.0
FROM python:3.10-slim-bookworm

RUN echo 'weisiwu'

RUN echo $(ls -al /etc)

RUN echo 'http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.12/main/' > /etc/apk/repositories \
    && echo 'http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.12/community/' >> /etc/apk/repositories

RUN apt-get update && \
    apt-get install -y git

# 设置工作目录为 /app
WORKDIR /novel_test

# 将当前目录内容复制到位于 /app 的容器中
COPY . /novel_test

# 安装 requirements.txt 中指定的任何所需包
# 你可以取消这一行的注释并创建 requirements.txt 文件
RUN pip install --no-cache-dir -r requirements.txt

# 在容器启动时运行 test.py
CMD ["python", "./test.py"]
