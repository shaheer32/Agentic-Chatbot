# 🤖 LangGraph AgenticAI Chatbot

A conversational AI chatbot built with **LangGraph**, **Groq LLM**, and **Streamlit** — featuring a clean web UI and a graph-based conversation flow.

---

## 🚀 Getting Started

**1. Install dependencies:**
```bash
pip install streamlit langchain-core langchain-groq langgraph typing-extensions
```

**2. Run the app:**
```bash
streamlit run app.py
```

**3. Enter your Groq API key in the sidebar.**
> Get your free key at [console.groq.com/keys](https://console.groq.com/keys)

---

## 🗂️ Project Structure

```
├── main.py                    # App entry point
├── state/state.py             # Message history
├── nodes/basic_chatbot_node.py  # AI response logic
├── graph/graph_builder.py     # LangGraph flow
├── LLMS/groqllm.py            # Groq LLM setup
└── UI/Streamlit/
    ├── loadUI.py              # Sidebar UI
    └── display_result.py      # Chat display
```

---

## 🧠 Supported Models

| Model ID | Speed | Notes |
|---|---|---|
| `llama-3.3-70b-versatile` | 280 t/s | Best quality |
| `llama-3.1-8b-instant` | 560 t/s | Fastest |
| `openai/gpt-oss-120b` | 500 t/s | Most capable |
| `openai/gpt-oss-20b` | 1000 t/s | Speed + quality |

---

## 🐛 Common Errors

| Error | Fix |
|---|---|
| `'GROQ_API_KEY'` KeyError | Enter your API key in the sidebar |
| `AIMessage not subscriptable` | Already fixed — update `display_result.py` |
| `Edge not found` | Node names must match exactly (case-sensitive) |

---

## 🛠️ Tech Stack

- **LangGraph** — manages conversation flow as a graph
- **Groq** — ultra-fast LLM inference
- **Streamlit** — web UI
- **LangChain** — LLM tooling and message types