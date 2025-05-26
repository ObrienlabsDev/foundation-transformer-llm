# foundation-transformer-llm
Training a base transformer model to be used as a foundation model from first principles.
see https://github.com/ObrienlabsDev/machine-learning/issues/5
## Requirements
### Training
### Fine Tuning
- https://modal.com/blog/how-much-vram-need-fine-tuning
- The maximum VRAM i have available is 72G on a base M3 Ultra (96G ram) or 48G on my RTX-A6000 or the base M2 Ultra - using the formula above be need 16x parameters forbhalf FP16 precision - which fits a 7B model
## Python
### Virtual Environment
- https://docs.python.org/3/library/venv.html

```
python3 -m venv virtenv         
source virtenv/bin/activate
deactivate           
 
```
