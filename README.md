# Abstract
Training a base non-recurrent transformer model using self attention to be used as a foundation model from first principles.  My base is generative pre-trained transformers in the model of the "Attention Is All You Need" paper 1706.03762 from Google 
- https://arxiv.org/abs/1706.03762
- see https://github.com/ObrienlabsDev/foundation-transformer-llm
- see https://github.com/ObrienlabsDev/doppler-radar-ml
- see https://github.com/ObrienlabsDev/machine-learning/issues/5

- see agentic serving work in https://github.com/ObrienlabsDev/distrbuted-agentic-ai/issues/1
## Requirements
### Training
### Fine Tuning
- https://modal.com/blog/how-much-vram-need-fine-tuning
- The maximum VRAM i have available is 72G on a base M3 Ultra (96G ram) or 48G on my RTX-A6000 or the base M2 Ultra - using the formula above be need 16x parameters forbhalf FP16 precision - which fits a 7B model
- 2026 update - make that 128g on an NVIDIA DGX Spark with 200gbps networking
- Thunderbolt 5 peaks at 66gbps between M3ultra, M4pro, M4max nodes
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
import torch
print("pytorch version:", version("torch"))
print(torch.backends.mps.is_available())
```


# Links
- 20260208 - circa Aug 2023 https://forum.effectivealtruism.org/posts/ErQdvzA9qqRA2gFBL/report-on-frontier-model-training
- 20260208 - Nanochat on 2 NVIDIA DGX Spark - https://forums.developer.nvidia.com/t/pretrain-nanochat-on-2-x-dgx-sparks/350564
