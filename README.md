# vllm-hf

## Get Strated
### Server side
1. Build the image:
```bash
docker build -t vll:latest_vllm server\dockerfile
```

2. Run the image:
```bash
docker run -it --gpus all -p 8000:8000 vll:latest_vllm
```

3. Login at HuggingFace account to access LLM:
```bash
hf auth login
```

4. Enter your HuggingFace Access Token

5. Run the server script:
```bash
python server\vllm_server.py
```
Note adjust server arugment if needed

6. Open another terminal

### Client side
7. Create a new env:
```bash
conda create -n vllm python=3.12
```
```bash
conda activate cllm
```
8. Install Libraries
```bash
pip install -r requirements.txt
```

9. Modify the configeration parameter at config.yaml

10. Run the code
```bash
python main.py
```