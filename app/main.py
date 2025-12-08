from fastapi import FastAPI

# 서버 객체 생성
app = FastAPI()

# 기본주소로 접속했을때 실행될 기능 (http://localhost:8081)
# uvicorn app.main:app --reload --port 8001로 실행
@app.get("/")
def read_root():
    return "ROBOT CONTROL SYSTEM"