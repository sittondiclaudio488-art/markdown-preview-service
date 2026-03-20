from fastapi import FastAPI
from pydantic import BaseModel
import markdown

app = FastAPI()

# 定义一个“数据模型”，告诉服务器我们会发什么样的文字过来
class MarkdownInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Markdown Parser is running!"}

# 这是今天的核心：POST 接口
@app.post("/convert")
def convert_markdown(data: MarkdownInput):
    # 使用 markdown 库将纯文本转换为 HTML
    html_content = markdown.markdown(data.text)
    return {
        "status": "success",
        "html": html_content
    }
