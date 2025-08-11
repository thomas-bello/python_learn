"""
端口管理工具模块
提供端口检测和管理相关的功能
"""
import socket
import sys


def find_free_port(start_port=8001, max_attempts=100):
    """
    查找可用端口，从start_port开始，最多尝试max_attempts次
    
    Args:
        start_port (int): 起始端口号，默认8001
        max_attempts (int): 最大尝试次数，默认100
    
    Returns:
        int: 可用的端口号
    
    Raises:
        SystemExit: 如果无法找到可用端口
    """
    for port in range(start_port, start_port + max_attempts):
        try:
            # 尝试绑定端口
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('0.0.0.0', port))
                print(f"✓ 找到可用端口: {port}")
                return port
        except OSError:
            print(f"✗ 端口 {port} 被占用，尝试下一个...")
            continue
    
    # 如果所有端口都被占用
    print(f"❌ 无法找到可用端口 (尝试范围: {start_port}-{start_port + max_attempts - 1})")
    sys.exit(1)


def is_port_available(port):
    """
    检查指定端口是否可用
    
    Args:
        port (int): 要检查的端口号
    
    Returns:
        bool: 端口是否可用
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', port))
            return True
    except OSError:
        return False


def print_server_info(port, app_name="FastAPI"):
    """
    打印服务器启动信息
    
    Args:
        port (int): 端口号
        app_name (str): 应用名称
    """
    print(f"🚀 启动 {app_name} 应用在端口 {port}")
    print(f"📖 API 文档: http://localhost:{port}/docs")
    print(f"🌐 应用地址: http://localhost:{port}")
