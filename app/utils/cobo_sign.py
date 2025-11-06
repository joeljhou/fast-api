import hashlib
import time
from urllib.parse import urlencode

import requests
from nacl.signing import SigningKey

def calculate_signature(method: str,
                        path: str,
                        timestamp_ms: str,
                        params_str: str,
                        body_str: str,
                        api_secret_hex: str) -> str:
    # 1) 拼接待签名字符串
    str_to_sign = f"{method}|{path}|{timestamp_ms}|{params_str}|{body_str}"
    print(f"1.str_to_sign: {str_to_sign}")

    # 2) 双重 SHA-256
    content_hash = hashlib.sha256(hashlib.sha256(str_to_sign.encode("utf-8")).digest()).digest()
    print(f"2.content_hash: {content_hash.hex()}")

    # 3) Ed25519 签名（API_SECRET 为 Ed25519 私钥，十六进制）
    sk = SigningKey(bytes.fromhex(api_secret_hex))
    signature = sk.sign(content_hash).signature  # 仅取签名部分
    print(f"3.signature: {signature.hex()}")

    return signature.hex()


def main():
    # 环境与认证配置
    host = "https://api.dev.cobo.com"
    method = "GET"
    path = "/v2/wallets/chains"

    # 用你的 API Key（公钥 hex）
    API_KEY = "831175afdab7741b87acbf71b92412d38f789fd964a46fc279492c321a33c287"
    # 用你的 API Secret（私钥 hex，务必替换为你自己的私钥）
    API_SECRET = "40180ebb1d39f44a1eef29fa90aaf8cbbd37f5ded83615f4cbad5d015c80b100"

    # 与 curl 示例一致的查询参数顺序与内容
    params = [
        ("wallet_type", "Custodial"),
        ("wallet_subtype", ""),
        ("chain_ids", ""),
        ("limit", "10"),
        ("before", ""),
        ("after", "")
    ]
    params_str = urlencode(params)  # 生成: wallet_type=Custodial&wallet_subtype=&chain_ids=&limit=10&before=&after=

    # GET 请求体为空
    body_str = ""

    # nonce/TIMESTAMP（毫秒）
    timestamp_ms = str(int(time.time() * 1000))

    # 计算签名
    signature_hex = calculate_signature(method, path, timestamp_ms, params_str, body_str, API_SECRET)

    # 构造请求
    url = f"{host}{path}?{params_str}"
    headers = {
        # 注意大小写：官方文档为 `Biz-Api-Key`
        "Biz-Api-Key": API_KEY,
        "Biz-Api-Nonce": timestamp_ms,
        "Biz-Api-Signature": signature_hex,
    }
    print(headers)

    # 发起请求
    resp = requests.get(url, headers=headers, timeout=10)
    print("Status:", resp.status_code)
    try:
        print(resp.json())
    except Exception:
        print(resp.text)


if __name__ == "__main__":
    main()
