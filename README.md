# 🤖 DecoBot Rule-Based AI Chatbot

Built with pure Python. No libraries. No frameworks. Just logic.

Project 1 of my AI Industrial Training at **DecodeLabs** (Batch 2026).

---

## What It Does
- Runs in a continuous loop stays alive until you say quit
- Sanitizes messy input before processing
- Detects your mood and responds with empathy
- Remembers your name across the conversation
- Looks up answers using a dictionary O(1) speed
- Types responses character by character like a real person

## Run It
```bash
git clone https://github.com/Ptechsoft/Rule_Based_AI_Chatbot_with_Python.git
cd Rule_Based_AI_Chatbot_with_Python
python rule_base_ai_chatbot.py
```

## Key Insight
A dictionary lookup is O(1). A long if-elif chain is O(n).
That small decision changes everything at scale.

---

> *"Rule-based logic is the skeleton that holds the intelligence together."*