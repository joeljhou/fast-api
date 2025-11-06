FROM mcr.microsoft.com/devcontainers/python:3.11

# 设置工作目录
WORKDIR /app

# 更快的容器启动与日志输出
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 预先安装依赖
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY app /app/app

# 暴露端口
EXPOSE 8000

# 启动命令：在容器内运行 uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]