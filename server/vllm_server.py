#!/usr/bin/env python3
import argparse, os

def main():
    ap = argparse.ArgumentParser(description="Tiny vLLM server launcher")
    ap.add_argument("--model", default="meta-llama/Llama-3.2-1B-Instruct")
    ap.add_argument("--host",  default="172.20.70.56")
    ap.add_argument("--port",  type=int, default=8000)
    ap.add_argument("--api-key", default="")
    args = ap.parse_args()

    cmd = [
        "vllm", "serve", args.model,
        "--host", args.host,
        "--port", str(args.port),
        "--dtype", "auto",
        # baked-in safety for T4/Colab stacks:
        "--enable-chunked-prefill=False",
        "--max-model-len", "8192",
        "--enforce-eager",
    ]
    if args.api_key:
        cmd += ["--api-key", args.api_key]

    # replace this process with vLLM so Ctrl+C etc. work naturally
    os.execvp(cmd[0], cmd)

if __name__ == "__main__":
    main()