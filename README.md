# OneAI — Access China's Best LLMs with One API Key

[![Website](https://img.shields.io/badge/Website-loyueai.com-6366f1)](https://loyueai.com)
[![Docs](https://img.shields.io/badge/Docs-API%20Reference-4f46e5)](https://loyueai.com/docs.html)

OneAI is a unified API gateway that gives you access to **9 models from 5 Chinese LLM providers** through a single OpenAI-compatible endpoint — **10× cheaper than GPT-4o**.

## 🔥 Supported Models

| Model | Provider | Price (per 1M input) | Context | Tags |
|-------|----------|---------------------|---------|------|
| **DeepSeek V3** | DeepSeek | $0.50 | 128K | Flagship · HOT |
| **DeepSeek R1** | DeepSeek | $3.00 | 128K | Reasoning · CoT |
| **Qwen-Plus** | Alibaba | $1.00 | 128K | Multilingual |
| **Qwen-Turbo** | Alibaba | $0.15 | 128K | Budget · VALUE |
| **QwQ-32B** | Alibaba | $0.50 | 32K | Open-weight reasoning |
| **Kimi** | Moonshot | $3.00 | 128K | Long context |
| **MiniMax M1** | MiniMax | $3.00 | 128K | Multimodal |
| **GLM-4-Flash** | Zhipu | $0.10 | 128K | Fastest · FREE |
| **GLM-4V** | Zhipu | $1.50 | — | Vision · Image |

## ⚡ Quick Start

```bash
# Use OneAI just like OpenAI — change the base URL
export OPENAI_BASE_URL="https://loyueai.com/api/v1"
export OPENAI_API_KEY="your-oneai-key"

# Python
pip install openai
```

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://loyueai.com/api/v1",
    api_key="your-oneai-key"
)

# Chat with DeepSeek V3 — $0.50 per 1M tokens!
response = client.chat.completions.create(
    model="deepseek-v3",
    messages=[{"role": "user", "content": "Explain quantum computing in one sentence."}]
)

print(response.choices[0].message.content)
```

### cURL

```bash
curl https://loyueai.com/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-oneai-key" \
  -d '{
    "model": "deepseek-v3",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

## 💰 Pricing Comparison

| Model | OneAI | GPT-4o | Savings |
|-------|-------|--------|---------|
| DeepSeek V3 | **$0.50** | $5.00 | **10×** |
| GLM-4-Flash | **$0.10** | $10.00 | **100×** |
| Qwen-Turbo | **$0.15** | $2.50 | **16×** |
| QwQ-32B | **$0.50** | $10.00 | **20×** |

*GPT-4o comparison prices per 1M input tokens (approximate)*

## 🎯 Why OneAI?

- 🇨🇳 **Best Chinese LLMs** — DeepSeek, Qwen, Kimi, MiniMax, GLM-4
- 🔌 **OpenAI-compatible** — Drop-in replacement, no code changes
- 💸 **10-100× cheaper** — Serious savings over Western APIs
- 🔑 **One key fits all** — Single API key for 9+ models
- 📦 **Prepaid credits** — No subscription, credits never expire
- ⚡ **Instant setup** — Register, top up, start calling

## 🚀 Get Started

1. **[Register](https://loyueai.com)** for an account
2. **Top up** credits (Starter $10 / Pro $50 / Scale $200)
3. **Get your API key** from the console
4. **Start building!** Use the examples above

## 📚 Docs

Full API reference: [loyueai.com/docs.html](https://loyueai.com/docs.html)

## 📧 Support

- Email: support@loyueai.com

---

© 2026 OneAI · Shanghai Corporate Information Technology Co., Ltd.
