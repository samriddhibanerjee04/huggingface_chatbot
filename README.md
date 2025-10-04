# 🧠 Local CLI Chatbot using Hugging Face

A simple **command-line chatbot** built in Python using a small Hugging Face text generation model.  
It maintains a short-term conversational memory using a **sliding window**, enabling coherent multi-turn conversations — all running **locally** without requiring a GPU.


## 🚀 Overview

This project demonstrates:
- Integration of a **Hugging Face model** into a local Python environment
- A **CLI interface** that supports continuous user input
- **Conversation memory** (last 3–5 turns)
- A clean, **modular codebase** for maintainability


## 🧩 Project Structure

├── model_loader.py # Handles model and tokenizer loading

├── chat_memory.py # Implements sliding window conversation memory

├── interface.py # CLI loop integrating model + memory

└── README.md #Documentation



## ⚙️ Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/samriddhibanerjee04/local-chatbot.git
cd local-chatbot
```

### 2. Create a Virtual Environment
```
python -m venv venv
```

### 3. Activate the Environment
Windows (PowerShell):
```
venv\Scripts\activate
```

### 4. Install Dependencies
```
pip install torch transformers
```

## Running the Chatbot
Once dependencies are installed, run:

```
python interface.py
```

## Example Interaction
Chatbot (type /exit to quit)

Loading model: google/flan-t5-base on CPU

You: Hi
Bot: Hello. How can I help you?

You: What is the capital of Japan?
Bot: The capital of Japan is Tokyo.

You: Thanks!
Bot: You’re welcome!

You: /exit
Exiting chatbot...
