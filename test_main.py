from fastapi.testclient import TestClient
from main import app

# 创建一个测试客户端，模拟浏览器行为
client = TestClient(app)

# 测试任务 1：检查首页是否正常
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Markdown Parser is running!"}

# 测试任务 2：检查 Markdown 转换功能是否正常
def test_convert_markdown():
    # 模拟发送一个 POST 请求
    test_data = {"text": "# Hello"}
    response = client.post("/convert", json=test_data)
    
    assert response.status_code == 200
    # 检查返回的内容是否包含正确的 HTML 标签
    assert "<h1>Hello</h1>" in response.json()["html"]

# 测试任务 3：检查发送空内容时的反应（边界测试）
def test_convert_empty():
    response = client.post("/convert", json={"text": ""})
    assert response.status_code == 200
    assert response.json()["html"] == ""
