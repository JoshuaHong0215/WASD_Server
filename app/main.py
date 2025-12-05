from fastapi import FastAPI

# 서버 객체 생성
app = FastAPI()

# 기본주소로 접속했을때 실행될 기능 (http://localhost:8080)
@app.get("/")
def read_root():
    return "ROBOT CONTROL SYSTEM"