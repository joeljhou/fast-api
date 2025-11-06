from pydantic import BaseModel


class CoboSignReq(BaseModel):
    method: str
    path: str
    timestamp_ms: str
    params_str: str
    body_str: str
    api_secret_hex: str