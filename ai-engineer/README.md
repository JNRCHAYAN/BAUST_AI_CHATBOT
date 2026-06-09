## Overview

# 🤖 AI Engineer Team


**Working Folder:** `/ai-engineer/`

**Role:** Build the AI-powered chatbot assistant and intelligent features for the platform.

#### Responsibilities

- Build a conversational AI chatbot using LangChain and OpenAI API
- Create a FastAPI backend to expose chatbot as REST endpoints
- Answer student FAQs, course information, deadlines, teacher contacts, event suggestions
- Optionally implement RAG (Retrieval-Augmented Generation) for document-based answers

#### Tech Stack

| Category             | Tool            |
| -------------------- | --------------- |
| Language             | Python          |
| API Framework        | FastAPI / Flask |
| AI API               | OpenAI API      |
| AI Framework         | LangChain       |
| Vector DB (Optional) | ChromaDB        |
| Testing              | Postman         |
| IDE                  | VS Code         |
| Version Control      | Git & GitHub    |

#### Folder Structure (suggested)

```
ai-engineer/
├── app/
│   ├── main.py           # FastAPI entry point
│   ├── chatbot.py        # LangChain chatbot logic
│   ├── routes/
│   └── models/
├── data/                 # FAQs, course info (for RAG)
├── requirements.txt
└── README.md             # Setup instructions for your module
```

#### Example Chatbot Queries to Handle

- _"When is the software engineering assignment due?"_
- _"Who teaches DBMS?"_
- _"What events are upcoming this week?"_
- _"What is the contact email for the CS department?"_

#### Deliverables

- Working `/api/chatbot` POST endpoint
- Handles at least 10 FAQ categories
- Integrated with the backend API

#### Branch Naming

```bash
git checkout -b ai-engineer/chatbot-core
git checkout -b ai-engineer/rag-integration
```

---
