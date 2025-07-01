# NetGPT

This project leverages OpenAI’s GPT-3.5 model to translate complex Cisco network device configurations into simple, clear explanations. It is designed to help junior network engineers understand configuration files quickly by generating human-readable bullet-point summaries.
This project is like a smart translator: You paste the tehnical text, and it talks to a GenAI model behind the scenes to get a plain English explanation.It helps new learners understand complex network configs.  Engineers can use it to double-check what a config is doing.

## Features

- CLI-based tool to paste or upload Cisco configs for instant AI-driven explanations  
- Uses OpenAI API securely via environment variables or a JSON config file  
- Supports customization of AI model, prompt, and output format  
- Lightweight Python implementation with minimal dependencies

## How to Use

1. Clone the repo and create a virtual environment.  
2. Add your OpenAI API key in `config.json` (not tracked by Git).  
3. Run `python main.py`, paste your Cisco config, and get an easy-to-understand explanation.  
 

## Skills Highlighted

- Python scripting and automation  
- Generative AI integration (OpenAI API)  
- Network engineering basics and config parsing  
- Secure API key management 