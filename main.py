from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import markdown

app = FastAPI()

# 挂载 static 文件夹，让后端能伺服前端的静态页面
app.mount("/static", StaticFiles(directory="static"), name="static")

class MarkdownInput(BaseModel):
    text: str

# 当用户访问根目录时，直接返回 index.html
@app.get("/")
def read_root():
    return FileResponse('static/index.html')

@app.post("/convert")
def convert_markdown(data: MarkdownInput):
    # 开启扩展语法：fenced_code 用于代码块，tables 用于表格
    html_content = markdown.markdown(data.text, extensions=['fenced_code', 'tables'])
    return {"status": "success", "html": html_content}
