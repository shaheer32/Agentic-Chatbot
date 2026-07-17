# 🤖 LangGraph AgenticAI Chatbot

A conversational AI chatbot built with **LangGraph**, **Groq LLM**, and **Streamlit** — featuring a clean web UI, a graph-based conversation flow, and optional real-time web search powered by **Tavily**.

---

## 🚀 Getting Started

**1. Install dependencies:**

```
pip install streamlit langchain-core langchain-groq langgraph typing-extensions tavily-python
```

**2. Run the app:**

```
streamlit run app.py
```

**3. Enter your Groq API key in the sidebar.**
> Get your free key at [console.groq.com/keys](https://console.groq.com/keys)

**4. Enter your Tavily API key in the sidebar to enable web search.**
> Get a free key at [tavily.com](https://tavily.com)
> Without this key, the chatbot still works normally — it just won't be able to search the web for current information.

---

## 🗂️ Project Structure

```
├── app.py                              # App entry point
├── src/LanggraphAgenticAI/
│   ├── state/state.py                  # Message history
│   ├── nodes/
│   │   ├── basic_chatbot_node.py       # AI response logic
│   │   └── chatbotwithtools.py         # AI + Tavily web search tool node
│   ├── graph/graph_builder.py          # LangGraph flow (chat / chat + tools)
│   └── LLMS/groqllm.py                 # Groq LLM setup
└── UI/Streamlit/
    ├── loadUI.py                       # Sidebar UI (Groq + Tavily keys, mode select)
    └── display_result.py               # Chat display
```

---

## 🧠 Supported Models

| Model ID                  | Speed    | Notes           |
| ------------------------- | -------- | --------------- |
| `llama-3.3-70b-versatile` | 280 t/s  | Best quality    |
| `llama-3.1-8b-instant`    | 560 t/s  | Fastest         |
| `openai/gpt-oss-120b`     | 500 t/s  | Most capable    |
| `openai/gpt-oss-20b`      | 1000 t/s | Speed + quality |

---

## 🔎 Web Search (Tavily)

When a Tavily API key is provided, the chatbot can use the **"Chat with Web Search"** mode. In this mode, the graph routes through a tool-calling node (`chatbotwithtools.py`) that lets the LLM decide when a query needs current information from the web, calls the Tavily search tool, and folds the results back into its response.

If no Tavily key is entered, the chatbot falls back to standard chat (`basic_chatbot_node.py`) using only the model's own knowledge.

---

## 🐛 Common Errors

| Error                          | Fix                                                        |
| ------------------------------- | ----------------------------------------------------------- |
| `'GROQ_API_KEY'` KeyError       | Enter your API key in the sidebar                          |
| `AIMessage not subscriptable`   | Already fixed — update `display_result.py`                 |
| `Edge not found`                | Node names must match exactly (case-sensitive)              |
| Web search not triggering       | Confirm Tavily key is entered and "Chat with Web Search" mode is selected |
| `'TAVILY_API_KEY'` KeyError     | Enter your Tavily key in the sidebar, or leave it blank to use the app without web search |

---

## 🛠️ Tech Stack

- **LangGraph** — manages conversation flow as a graph
- **Groq** — ultra-fast LLM inference
- **Tavily** — real-time web search for up-to-date answers
- **Streamlit** — web UI
- **LangChain** — LLM tooling and message types
