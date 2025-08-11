# python learn fastApi

python learn fastApi

`FastAPI` 是一个现代、高性能的 Python Web 框架，特别适合构建 RESTful API。
`uvicorn` 是一个轻量级的 ASGI 服务器，用于运行 FastAPI 应用。
`pydantic` 用于数据验证和序列化，确保请求和响应的数据格式正确。

`ASGI` （Asynchronous Server Gateway Interface）是一个用于 Python Web 应用的标准接口，支持异步编程。

## Setup

使用 `pyenv` 切换 `python` 版本到 `3.8.20`

```bash
pyenv versions
pyenv install 3.8.20 # 如果没有安装
pyenv local 3.8.20 # 切换到 3.8.20
python --version # 确认版本
```

使用 `venv` 构建 `python` 虚拟环境

```bash
python -m venv .venv # 创建虚拟环境
source .venv/bin/activate # 激活虚拟环境

pip install fastapi uvicorn
```

创建 [main.py](./main.py)

运行 FastAPI 应用

```bash
uvicorn main:app --reload
```

[http://127.0.0.1:8000](http://127.0.0.1:8000)
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 核心概念

| 概念 | 示例代码 |
| ---- | -------------------------------------------------------------- |
| 路径参数 | `@app.get("/items/{item_id}")` |
| 查询参数 | `@app.get("/items/")` 接收 `?q=xxx` |
| 请求体 | `@app.post("/items/")` 接收 JSON 数据（用 Pydantic 模型验证） |
| 响应模型 | `response_model=ItemOut` |
| 异常处理 | `raise HTTPException(status_code=400, detail="Invalid input")` |
| 异步支持 | `async def read_root(): ...` |
| 后台任务 | `BackgroundTasks` 用于日志、邮件等非阻塞任务 |

