#!/usr/bin/env python3
"""
启动脚本：自动查找可用端口并启动FastAPI服务器
支持uvicorn的所有参数
"""
import subprocess
import argparse
from utils.port_manager import find_free_port, print_server_info


def main():
    parser = argparse.ArgumentParser(description='启动FastAPI服务器并自动查找可用端口')
    parser.add_argument('--start-port', type=int, default=8001, help='起始端口号 (默认: 8001)')
    parser.add_argument('--max-attempts', type=int, default=100, help='最大尝试次数 (默认: 100)')
    parser.add_argument('--app', default='main:app', help='FastAPI应用 (默认: main:app)')
    parser.add_argument('--reload', action='store_true', help='启用自动重载')
    parser.add_argument('--host', default='0.0.0.0', help='绑定主机 (默认: 0.0.0.0)')
    
    args = parser.parse_args()
    
    # 查找可用端口
    available_port = find_free_port(args.start_port, args.max_attempts)
    
    # 打印启动信息
    print_server_info(available_port)
    
    # 构建uvicorn命令
    cmd = [
        'uvicorn', 
        args.app,
        '--host', args.host,
        '--port', str(available_port)
    ]
    
    if args.reload:
        cmd.append('--reload')
    
    # 启动uvicorn
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")


if __name__ == "__main__":
    main()
