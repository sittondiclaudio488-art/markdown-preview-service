from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "HUSTer", "Status": "Success"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
