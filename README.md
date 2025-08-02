# Abstract
Training a base non-recurrent transformer model using self attention to be used as a foundation model from first principles.  My base is generative pre-trained transformers in the model of the "Attention Is All You Need" paper 1706.03762 from Google 
- https://arxiv.org/abs/1706.03762
- https://github.com/ObrienlabsDev/machine-learning/issues/5

- see agentic serving work in https://github.com/ObrienlabsDev/distrbuted-agentic-ai/issues/1
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
### Pytorch for CUDA and Metal
```
pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
```
