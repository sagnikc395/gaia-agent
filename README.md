---
title: Gaia Agent
sdk: gradio
app_file: app.py
python_version: 3.13
hf_oauth: true
---

## gaia-agent

made as part of final project for the HuggingFace Agents Course.

Objective: Building a AI agent for the GAIA benchmark .It combines different LLM models and multimodal tools to reason over text , audio ,images and videos.


Inference is done using Groq and GPT OSS 120B model.

### Setup 

Take your API keys from Groq and set it up as 
```
GROQ_API_KEY="<api-key>"
```

For image questions, also set an OpenAI key:
```
OPENAI_API_KEY="<api-key>"
```
