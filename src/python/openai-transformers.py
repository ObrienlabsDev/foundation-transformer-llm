from transformers import pipeline
 
generator = pipeline(
    "text-generation",
    model="openai/gpt-oss-20b",
    torch_dtype="auto",
    device_map="cuda"  # Automatically place on available GPUs
)
 
messages = [
    {"role": "user", "content": "Explain what MXFP4 quantization is."},
]
 
result = generator(
    messages,
    max_new_tokens=200,
    temperature=1.0,
)
 
print(result[0]["generated_text"])