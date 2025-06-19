# Runnables in LangChain

This repository demonstrates how to use **Runnable components** in LangChain. Runnable primitives allow you to construct flexible, reusable, and powerful chains by composing components together — much like Lego blocks.  
This lets you control flow, apply branching, execute in parallel, or simply pass through data in sophisticated workflows.

## 📄 File Descriptions

- `RunnableSequence.py`  Shows how to execute components in **sequence**.

- `RunnablePassthrough.py`  Demonstrates a **passthrough** runnable.

- `RunnableLambda.py`  Allows you to apply custom **lambda** functions within a runnable pipeline.

- `RunnableParallel.py`  Shows how to execute components in **parallel**.

- `RunnableBranch.py`  Demonstrates **branching**, where different paths execute based on conditions.

## 🔐 Environment Variables

To use this project, you need to set API keys in a `.env` file in the root directory.

### 📄 .env file format

```env
OPENAI_API_KEY="your_openai_key"
ANTHROPIC_API_KEY="your_anthropic_key"
GOOGLE_API_KEY="your_google_key"
HUGGINGFACEHUB_API_KEY="your_huggingfacehub_key"
```

### Dont have closed-source API key ? 
Refer to the repo [**Models_in_LangChain**](https://github.com/yourusername/Models_in_LangChain) for using open-sourced Hugging Face chat models (via API or locally).
