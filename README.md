# 🤖 Building an AI-Powered Stock Analysis Agent with Google ADK

Welcome to this hands-on guide to building intelligent, production-ready agents using **Google's Agent Development Kit (ADK)**.

In this project, you'll learn how to build a simple agent that:
- Fetches real-time stock data using `yfinance`
- Calculates **technical indicators** like SMA (Simple Moving Average) and RSI (Relative Strength Index)
- Provides actionable insights using an LLM-powered agent
- Runs on a local ADK-powered web interface

> 🚀 No heavy infra, just powerful logic with modular AI components.

## 🧠 What is Google ADK?

Google's **Agent Development Kit (ADK)** is an open-source framework for building intelligent multi-agent systems. It simplifies everything from building and debugging agents to running them in production.

### Key Features:
- **Modular agent design**
- **Tool and LLM integration**
- **Web-based UI for testing**
- **Cloud-ready deployments with Vertex AI Agent Builder**

## 📁 Project Structure

```
stock-analysis-adk/ 
├── stock_analysis_agent/
    ├── .env
    ├── __init__.py 
    └── agent.py
```

## 🚀 Getting Started

### 1. Clone this repository
```bash
git clone https://github.com/yourusername/stock-analysis-adk.git
cd stock-analysis-adk
```

### 2. Set up a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install google-adk yfinance pandas pandas_ta python-dotenv
```

### 4. Create .env file
Inside `stock_analysis_agent/`, add your API keys:
```
GOOGLE_GENAI_USE_VERTEXAI="False"
GEMINI_API_KEY=your_gemini_api_key
```

> 🔒 Make sure to keep your `.env` file secret.

## 🧪 Run the Agent Locally

Start the ADK web server:
```bash
cd stock_analysis_adk
adk web
```

Open your browser:
```
http://localhost:8000
```

Select `stock_analysis_agent` from the agent list and start querying!
