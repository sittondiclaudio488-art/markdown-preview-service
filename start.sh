#!/bin/bash

echo "========================================"
echo "🚀 准备启动 HUST Markdown 实时预览服务..."
echo "========================================"

# 1. 检查虚拟环境目录是否存在
if [ ! -d "venv" ]; then
    echo "❌ 错误: 未找到 venv 虚拟环境目录！请先阅读 README.md 进行安装。"
    exit 1
fi

# 2. 激活虚拟环境
echo "-> 正在激活虚拟环境..."
source venv/bin/activate

# 3. 启动 FastAPI 服务
echo "-> 正在启动后端解析引擎..."
uvicorn main:app --host 0.0.0.0 --port 8000
