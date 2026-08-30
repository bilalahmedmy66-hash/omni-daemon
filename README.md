# ⚡ Omni-Daemon

**The Universal JIT Multi-Language Code Execution Engine.**

Omni-Daemon is a paradigm shift in software architecture. Instead of writing static APIs or manual logic, developers send a plain-English intent to the daemon. The engine synthesizes the optimal code on the fly, executes it in a secure Native Python Sandbox, and instantly returns the result.

**Built by Bilal Ahmed**

---

## 🚀 How It Works
1. **The Brain:** Intercepts an HTTP request with a plain-text intent.
2. **The Synthesizer:** Uses Google Gemini to write flawless, executable Python code in milliseconds.
3. **The Sandbox:** Executes the code in a strictly controlled local environment using Python's `subprocess`.
4. **The Output:** Returns the calculated JSON output back to the client.

## 💻 Quick Start

**Start the Server:**
`python daemon.py`

**Execute an Intent (Python Client):**
```python
from client import Omni
result = Omni.run("Generate a secure 16-character password")
print(result)