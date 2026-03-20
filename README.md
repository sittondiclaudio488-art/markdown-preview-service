# 🚀 HUST Markdown 实时预览服务

本项目是一个轻量、高效的前后端分离 Markdown 实时渲染引擎。实现了浏览器端输入与右侧 HTML 页面的毫秒级同步渲染，并支持代码高亮、MathJax 数学公式以及核心的**元素级精准同步对齐滚动**。

## 🎯 面向小白的快速部署指南

哪怕你完全不懂 Python 或是没有任何编程基础，只需按照以下步骤在一台纯净的 Ubuntu 服务器上操作，即可一键启动属于你的 Markdown 预览服务！

### 第一步：获取代码
首先，将本项目克隆到你的服务器中：
`bash
git clone https://github.com/sittondiclaudio488-art/markdown-preview-service.git
cd markdown-preview-service
`

### 第二步：准备运行环境
> **技术选型说明**：针对轻量级云服务器的资源限制，本项目优化了环境隔离方案，采用 Python 原生的 `venv` 替代了体积庞大的 Anaconda/Miniconda，不仅极大降低了内存和磁盘开销，且部署速度更快。

Ubuntu 系统通常自带 Python3。你只需要一行命令安装虚拟环境支持包即可：
`bash
sudo apt update
sudo apt install python3-venv -y
`

### 第三步：一键启动服务
[cite_start]我们为你准备了全自动化的启动脚本 [cite: 49]。你完全不需要手动配置复杂的环境，只需赋予权限并运行：
`bash
chmod +x start.sh
./start.sh
`
[cite_start]*(这个脚本会自动为你创建虚拟环境、安装 requirements.txt 中的所需依赖，并启动后端的 FastAPI 解析引擎 [cite: 48, 49]。)*

### 第四步：在浏览器中体验
当你在终端看到类似 `Uvicorn running on http://0.0.0.0:8000` 的提示时，说明服务已经成功运行！
现在，打开你的浏览器，访问：
`http://你的服务器公网IP:8000/`

即可开始体验丝滑的实时预览、公式渲染与精准的同步滚动！
