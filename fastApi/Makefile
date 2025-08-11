# FastAPI 项目 Makefile

.PHONY: help install run test clean docker-build docker-run docker-stop lint format

# 默认目标
help:
	@echo "FastAPI 项目管理命令"
	@echo ""
	@echo "可用命令:"
	@echo "  install         安装依赖"
	@echo "  run             运行开发服务器"
	@echo "  test            运行测试"
	@echo "  lint            代码检查"
	@echo "  format          格式化代码"
	@echo "  clean           清理缓存文件"
	@echo ""
	@echo "Docker 命令:"
	@echo "  docker-dev      启动Docker开发环境"
	@echo "  docker-prod     启动Docker生产环境"
	@echo "  docker-build    构建Docker镜像"
	@echo "  docker-stop     停止Docker服务"
	@echo "  docker-logs     查看Docker日志"
	@echo "  docker-shell    进入Docker容器"
	@echo ""

# 本地开发命令
install:
	@echo "安装Python依赖..."
	pip install -r requirements.txt

run:
	@echo "启动开发服务器..."
	python main.py

run-script:
	@echo "使用启动脚本启动服务器..."
	python start_server.py --reload

test:
	@echo "运行测试..."
	python -m pytest -v

lint:
	@echo "运行代码检查..."
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	@echo "格式化代码..."
	black .
	isort .

clean:
	@echo "清理缓存文件..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +

# Docker 命令
docker-dev:
	@echo "启动Docker开发环境..."
	./docker-scripts.sh up-dev

docker-prod:
	@echo "启动Docker生产环境..."
	./docker-scripts.sh up-prod

docker-build:
	@echo "构建Docker镜像..."
	./docker-scripts.sh build-dev

docker-stop:
	@echo "停止Docker服务..."
	./docker-scripts.sh down

docker-logs:
	@echo "查看Docker日志..."
	./docker-scripts.sh logs

docker-shell:
	@echo "进入Docker容器..."
	./docker-scripts.sh shell

# 生成requirements.txt
requirements:
	@echo "生成requirements.txt..."
	pip freeze > requirements.txt

# 检查Docker是否可用
check-docker:
	@docker --version >/dev/null 2>&1 || (echo "Docker未安装" && exit 1)
	@docker-compose --version >/dev/null 2>&1 || (echo "Docker Compose未安装" && exit 1)
	@echo "Docker环境正常"
