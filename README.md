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
uvicorn main:app1 --reload --port 2345
```
