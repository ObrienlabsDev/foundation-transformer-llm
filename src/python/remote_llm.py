import os
import re

# rest call to remote LLM service
import requests
import json


# call the remote LLM service
def call_remote_llm(prompt, model="deepseek-R1:70b"):
    SERVER_LLM = os.getenv("SERVER_LLM", "localhost")
    REMOTE_LLM_URL = f"http://{SERVER_LLM}:11434/api/generate"
    print("REMOTE_LLM_URL: ", REMOTE_LLM_URL)
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }
    # unused
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True, 
        "temperature": 0.7,  # creativity
        "top_p": 0.9,  # diversity
        "max_tokens": 2048,  
        "stop": ["\n", "<|endoftext|>"] 
    }
    try:
        with requests.post(REMOTE_LLM_URL, headers=headers, data=json.dumps(data), stream=True) as response:
            response.raise_for_status() 
            for packets in response.iter_lines():
                if packets:
                    try:
                        json_packet = json.loads(packets.decode('utf-8'))
                        if 'response' in json_packet:
                            # parse {'model': 'deepseek-R1:70b', 'created_at': '2025-07-24T02:56:41.585812Z', 'response': '<think>', 'done': False}
                            print(json_packet['response'], end='', flush=True)
                        elif 'error' in json_packet:
                            print(f"Error: {json_packet['error']}")
                            break
                    except json.JSONDecodeError:
                        pass # siliently ignore
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


call_remote_llm("Describe the relativistic effects of heavy elements like gold - in terms of why the color of the metal arises from the outer electrons moving at a large fraction of the speed of light")


#curl http://server:11434/api/generate -d '{
#  "model": "deepseek-R1:70b",
#  "prompt":"Describe the relativistic effects of heavy elements like gold - in terms of why the color of the metal arises from the outer electrons moving at a large fraction of the speed of light"
#}'

