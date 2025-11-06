from fastapi import FastAPI
import uvicorn

from app.models.cobo_dto import CoboSignReq
from app.utils.cobo_sign import calculate_signature

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/cobo/sign")
def cobo_sign(req: CoboSignReq):
    signature_hex = calculate_signature(
        req.method,
        req.path,
        req.timestamp_ms,
        req.params_str,
        req.body_str,
        req.api_secret_hex,
    )
    return {"signature": signature_hex}


if __name__ == "__main__":
    # 启动 FastAPI 服务
    uvicorn.run("main:app", host="127.0.0.1", port=2345, reload=True)

