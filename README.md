# python_learn

python_learn

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
pip install --upgrade pip
pip install -r requirements.txt
```