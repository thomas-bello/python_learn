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

## 项目结构

```text
fastApi/
├── main.py                 # 主应用文件
├── start_server.py         # 自动端口检测启动脚本
├── test_port_manager.py    # 端口管理工具测试
├── api/                    # API模块
│   ├── __init__.py
│   ├── routes.py          # 路由定义
│   ├── models.py          # 数据模型
│   └── ...
├── utils/                  # 工具模块
│   ├── __init__.py
│   └── port_manager.py    # 端口管理工具
└── .vscode/
    └── launch.json        # VS Code调试配置
```

运行 FastAPI 应用

```bash
# 方式1：使用uvicorn (固定端口)
uvicorn main:app --reload

# 方式2：直接运行main.py (自动查找可用端口)
python main.py

# 方式3：使用启动脚本 (自动查找可用端口)
python start_server.py --reload

# 方式4：指定起始端口
python start_server.py --reload --start-port 9000
```

**自动端口检测功能：**

- 如果端口8001被占用，会自动尝试8002、8003...直到找到可用端口
- 最多尝试100个端口
- 启动时会显示实际使用的端口号和访问链接

[http://127.0.0.1:8000](http://127.0.0.1:8000) (默认端口)
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (API文档)

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

