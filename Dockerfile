# 使用官方 Python 运行时作为父镜像
FROM python:3.11
FROM git

git clone git@github.com:weisiwu/novel_test.git

# 设置工作目录为 /app
WORKDIR /app

# 将当前目录内容复制到位于 /app 的容器中
COPY . /app

# 安装 requirements.txt 中指定的任何所需包
# 你可以取消这一行的注释并创建 requirements.txt 文件
RUN pip install --no-cache-dir -r requirements.txt

# 在容器启动时运行 app.py
# 例如，你可以创建一个 app.py 文件
# CMD ["python", "./app.py"]
