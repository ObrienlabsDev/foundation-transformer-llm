import os
import re

# rest call to remote LLM service
import requests

SERVER_LLM = os.getenv("SERVER_LLM", "localhost")

REMOTE_LLM_URL = f"http://{SERVER_LLM}:11434/generate"

print("REMOTE_LLM_URL: ", REMOTE_LLM_URL);

#curl http://server:11434/api/generate -d '{
#  "model": "deepseek-R1:70b",
#  "prompt":"Describe the relativistic effects of heavy elements like gold - in terms of why the color of the metal arises from the outer electrons moving at a large fraction of the speed of light"
#}'