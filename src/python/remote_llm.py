import os
import re

# rest call to remote LLM service
import requests


# call the remote LLM service
def call_remote_llm(prompt, model="deepseek-R1:70b"):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True,  # Set to True for streaming responses
        "temperature": 0.7,  # Adjust temperature for creativity
        "top_p": 0.9,  # Adjust top_p for diversity
        "max_tokens": 2048,  # Limit the response length
        "stop": ["\n", "<|endoftext|>"]  # Define
    }
    try:
        response = requests.post(REMOTE_LLM_URL, json=payload)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling remote LLM: {e}")
        return None


SERVER_LLM = os.getenv("SERVER_LLM", "localhost")
REMOTE_LLM_URL = f"http://{SERVER_LLM}:11434/api/generate"
print("REMOTE_LLM_URL: ", REMOTE_LLM_URL)
call_remote_llm("Describe the relativistic effects of heavy elements like gold - in terms of why the color of the metal arises from the outer electrons moving at a large fraction of the speed of light")


#curl http://server:11434/api/generate -d '{
#  "model": "deepseek-R1:70b",
#  "prompt":"Describe the relativistic effects of heavy elements like gold - in terms of why the color of the metal arises from the outer electrons moving at a large fraction of the speed of light"
#}'

