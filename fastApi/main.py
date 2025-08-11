from fastapi import FastAPI
from api.routes import api_router
from utils.port_manager import find_free_port, print_server_info

app = FastAPI()

# 注册所有API路由
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


if __name__ == "__main__":
    import uvicorn
    
    # 自动查找可用端口
    available_port = find_free_port(8001)
    
    # 打印启动信息
    print_server_info(available_port)
    
    # 启动服务器
    uvicorn.run(app, host="0.0.0.0", port=available_port)