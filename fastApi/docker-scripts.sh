#!/bin/bash

# Docker管理脚本
# 用法: ./docker-scripts.sh [command]

set -e

PROJECT_NAME="fastapi"
DEV_COMPOSE_FILE="docker-compose.yml"
PROD_COMPOSE_FILE="docker-compose.prod.yml"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 日志函数
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 帮助信息
show_help() {
    echo "FastAPI Docker 管理脚本"
    echo ""
    echo "用法: $0 [command]"
    echo ""
    echo "命令:"
    echo "  build-dev     构建开发环境镜像"
    echo "  build-prod    构建生产环境镜像"
    echo "  up-dev        启动开发环境"
    echo "  up-prod       启动生产环境"
    echo "  down          停止并删除容器"
    echo "  logs          查看日志"
    echo "  shell         进入容器shell"
    echo "  test          运行测试"
    echo "  clean         清理Docker资源"
    echo "  help          显示此帮助信息"
    echo ""
}

# 构建开发镜像
build_dev() {
    log_info "构建开发环境镜像..."
    docker-compose -f $DEV_COMPOSE_FILE build
    log_success "开发环境镜像构建完成"
}

# 构建生产镜像
build_prod() {
    log_info "构建生产环境镜像..."
    docker-compose -f $PROD_COMPOSE_FILE build
    log_success "生产环境镜像构建完成"
}

# 启动开发环境
up_dev() {
    log_info "启动开发环境..."
    docker-compose -f $DEV_COMPOSE_FILE up -d
    log_success "开发环境已启动"
    log_info "应用地址: http://localhost:8001"
    log_info "API文档: http://localhost:8001/docs"
}

# 启动生产环境
up_prod() {
    log_info "启动生产环境..."
    docker-compose -f $PROD_COMPOSE_FILE up -d
    log_success "生产环境已启动"
    log_info "应用地址: http://localhost:8001"
}

# 停止服务
down() {
    log_info "停止服务..."
    docker-compose -f $DEV_COMPOSE_FILE down 2>/dev/null || true
    docker-compose -f $PROD_COMPOSE_FILE down 2>/dev/null || true
    log_success "服务已停止"
}

# 查看日志
logs() {
    log_info "查看应用日志..."
    if docker-compose -f $DEV_COMPOSE_FILE ps | grep -q "fastapi-dev"; then
        docker-compose -f $DEV_COMPOSE_FILE logs -f fastapi-app
    elif docker-compose -f $PROD_COMPOSE_FILE ps | grep -q "fastapi-prod"; then
        docker-compose -f $PROD_COMPOSE_FILE logs -f fastapi-app
    else
        log_error "没有运行的容器"
    fi
}

# 进入容器shell
shell() {
    log_info "进入容器shell..."
    if docker-compose -f $DEV_COMPOSE_FILE ps | grep -q "fastapi-dev"; then
        docker-compose -f $DEV_COMPOSE_FILE exec fastapi-app bash
    elif docker-compose -f $PROD_COMPOSE_FILE ps | grep -q "fastapi-prod"; then
        docker-compose -f $PROD_COMPOSE_FILE exec fastapi-app bash
    else
        log_error "没有运行的容器"
    fi
}

# 运行测试
run_test() {
    log_info "运行测试..."
    docker-compose -f $DEV_COMPOSE_FILE exec fastapi-app python -m pytest
}

# 清理Docker资源
clean() {
    log_warning "清理Docker资源..."
    read -p "确定要清理所有未使用的Docker资源吗? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        docker system prune -f
        docker volume prune -f
        log_success "Docker资源清理完成"
    else
        log_info "取消清理操作"
    fi
}

# 主函数
main() {
    case "${1:-}" in
        build-dev)
            build_dev
            ;;
        build-prod)
            build_prod
            ;;
        up-dev)
            build_dev
            up_dev
            ;;
        up-prod)
            build_prod
            up_prod
            ;;
        down)
            down
            ;;
        logs)
            logs
            ;;
        shell)
            shell
            ;;
        test)
            run_test
            ;;
        clean)
            clean
            ;;
        help|--help|-h)
            show_help
            ;;
        *)
            log_error "未知命令: ${1:-}"
            echo ""
            show_help
            exit 1
            ;;
    esac
}

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    log_error "Docker未安装，请先安装Docker"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    log_error "Docker Compose未安装，请先安装Docker Compose"
    exit 1
fi

# 运行主函数
main "$@"
