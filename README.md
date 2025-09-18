# vLLM Local Deployment Guide

Learn how to deploy and interface with vLLM locally using Docker. This repository demonstrates vLLM's power through a practical Arabic sentiment analysis example.

## Why vLLM?

- **⚡ High Performance:** Up to 24x faster inference than standard transformers
- **🔧 Easy Integration:** OpenAI-compatible API - drop-in replacement
- **🚀 Production Ready:** Optimized for serving at scale
- **💾 Memory Efficient:** Advanced memory management and batching
- **🔄 Flexible:** Support for various model architectures and quantization

## What You'll Learn

- Deploy vLLM server with Docker and GPU support
- Interface with vLLM using OpenAI-compatible client
- Configure models and prompts via YAML
- Best practices for local LLM deployment

## Quick Start

### Server Setup

1. **Build and run the Docker container:**
   ```bash
   docker build -t vllm:latest server/dockerfile
   docker run -it --gpus all -p 8000:8000 vllm:latest
   ```

2. **Inside the container, authenticate with HuggingFace:**
   ```bash
   hf auth login
   # Enter your HF token when prompted
   ```

3. **Start the vLLM server:**
   ```bash
   python server/vllm_server.py
   ```

### Client Setup

1. **Create Python environment:**
   ```bash
   conda create -n vllm python=3.12
   conda activate vllm
   pip install -r requirements.txt
   ```

2. **Configure settings in `config.yaml`:**
   ```yaml
   server:
     base_url: "http://172.20.70.56:8000/v1"  # Update with your server IP
     model: "meta-llama/Llama-3.2-1B-Instruct"
   ```

3. **Run code:**
   ```bash
   python main.py
   ```
   
## Example Use Case: Arabic Sentiment Analysis

The included example demonstrates Arabic customer review sentiment scoring (1-10 scale):

**Input:** Arabic restaurant review  
**Output:** Numerical satisfaction score

This showcases vLLM's multilingual capabilities and structured output generation.

## Key Components

- **`server/`** - Dockerized vLLM server setup
- **`main.py`** - OpenAI-compatible client example  
- **`config.yaml`** - Easy configuration management
- **Jupyter notebook** - Interactive experimentation

## Server Configuration Options

```bash
python server/vllm_server.py \
  --model "your-model-name" \
  --host "0.0.0.0" \
  --port 8000
```

## Next Steps

1. Try different models (replace model name in config)
2. Experiment with various prompts and use cases
3. Scale to multiple GPUs or larger models
4. Integrate into your applications via the API

## Requirements

- CUDA-compatible GPU
- Docker with GPU support
- HuggingFace account (for gated models)

## Author
- Sameer Alsabea (Sameer-13), [LinkedIn](https://www.linkedin.com/in/sameer-alsabea-610291239/)
