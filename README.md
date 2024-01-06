
# GPT-powered-conversational-bot
This project leverages Llama v2 Chat models for a Chatbot Application
# Web ChatGPT

## Instructions

Create a Python environment including `scrapy`, `langchain`, `gradio`, `openai`, `chromadb`, `html2text`, `tiktoken`. Pip-install other possible missing dependencies.

1) Run terminal. At `hfcrawl` dir level, type `scrapy crawl huggingface`. Go back one level to `webchatgpt` and type `python index.py`.

WARNING: you need an API key from OpenAI site (see https://platform.openai.com/account/api-keys). Once the key is generated:

[Linux] copy it and type `export OPENAI_API_KEY="`*INSERT_KEY_HERE*`"` or

[Windows] add a new environment variable named  OPENAI_API_KEY and set the generated key as the value. 

2) After setting the key, type `python bot.py`, go to http://127.0.0.1:7860 and ask some question about diffusers.

