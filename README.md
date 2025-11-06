# 搭建FastAPI服务

## 虚拟环境
1. **通过python内置的venv模块创建虚拟环境目录`.venv`**
    ```shell
    python3 -m venv .venv
    ```
2. **激活虚拟环境**
    ```shell
    source .venv/bin/activate
    ```
    ![激活](http://img.geekyspace.cn/pictures/2025/202511061422869.png)
3. **退出虚拟环境**
    ```shell
    deactivate
    ```
## 安装依赖
1. 安装fastapi/uvicorn依赖
    ```shell
    python -m pip install fastapi uvicorn
    ```
2. 使用`requirements.txt`管理项目
   ```shell
   touch requirements.txt
   echo -e "fastapi\nuvicorn" > requirements.txt
   ```
3. 获取依赖当前具体版本
   ```shell
   pip freeze
   ```

## 创建 FastAPI 应用

参考：`main.py`

**运行 FastAPI 服务**

```shell
uvicorn app.main:app --reload --port 2345
```

## 使用 Docker 本地运行

1. 构建镜像并启动服务（默认端口 `8000`）
   ```shell
   docker compose build
   docker compose up
   ```
2. 访问接口与文档
   - 根路径: `http://localhost:8000/`
   - 文档: `http://localhost:8000/docs`
3. 停止服务
   ```shell
   docker compose down
   ```

说明：`docker-compose.yml` 会将本地 `./app` 挂载为只读到容器中，便于开发时同步代码；如需热重载，可在 compose 中改用 `command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload` 并安装对应依赖。
