import os
import time
import httpx
import yaml
from openai import OpenAI

def wait_server(base_url: str, api_key: str, timeout_s: int = 120) -> None:
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
    t0 = time.time()
    root = base_url.rstrip("/v1")
    while time.time() - t0 < timeout_s:
        try:
            ok0 = httpx.get(f"{root}/health", timeout=2.0).status_code == 200
            ok1 = httpx.get(f"{base_url}/models", headers=headers, timeout=3.0).status_code == 200
            if ok0 and ok1:
                return
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError("Server not ready; check network, base_url, or api key.")

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    server_config = config["server"]
    base_url = server_config["base_url"]
    api_key  = server_config["api_key"]
    model    = server_config["model"]
    
    review_text = "الطعام لذيذ والشيش افضل شيش ذقته روعه ويحتاج فقط اعاده تأهيل المبنى والتوسعه"
    
    prompt = config["prompt"]    
    prompt = prompt + "\n" + f"Review: {review_text}"


    wait_server(base_url, api_key)

    client = OpenAI(base_url=base_url, api_key=api_key)

    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=3,
        # temperature=0,
    )
    rating = resp.choices[0].message.content.strip()
    print("Predicted rating:", rating)

if __name__ == "__main__":
    main()
