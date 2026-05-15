"""OneAI API Demo — Quick start examples"""

import os
from openai import OpenAI

# Configuration
BASE_URL = "https://loyueai.com/api/v1"
API_KEY = os.getenv("ONEAI_API_KEY", "your-api-key-here")

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


def chat_example():
    """Basic chat with DeepSeek V3"""
    print("=" * 50)
    print("💬 Chat: DeepSeek V3 ($0.50/1M)")
    print("=" * 50)
    
    response = client.chat.completions.create(
        model="deepseek-v3",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What's the capital of France?"}
        ],
        temperature=0.7,
        max_tokens=100
    )
    
    print(response.choices[0].message.content)
    print(f"\nTokens: {response.usage.total_tokens}")
    print(f"Cost: ~${response.usage.total_tokens * 0.50 / 1_000_000:.6f}")


def reasoning_example():
    """Deep reasoning with DeepSeek R1"""
    print("\n" + "=" * 50)
    print("🧠 Reasoning: DeepSeek R1 ($3.00/1M)")
    print("=" * 50)
    
    response = client.chat.completions.create(
        model="deepseek-r1",
        messages=[
            {"role": "user", "content": "If a shirt costs $97 and I borrow $50 from mom and $50 from dad, buy it and get $3 change. I give $1 back to each parent and keep $1. But $49 + $49 + $1 = $99. Where's the missing dollar?"}
        ],
        max_tokens=500
    )
    
    print(response.choices[0].message.content)


def budget_example():
    """Ultra-cheap: GLM-4-Flash at $0.10/1M"""
    print("\n" + "=" * 50)
    print("💸 Budget: GLM-4-Flash ($0.10/1M)")
    print("=" * 50)
    
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[
            {"role": "user", "content": "Write a haiku about coding."}
        ]
    )
    
    print(response.choices[0].message.content)
    print(f"\nCost: ~${response.usage.total_tokens * 0.10 / 1_000_000:.6f}")


if __name__ == "__main__":
    if API_KEY == "your-api-key-here":
        print("⚠️  Set your API key: export ONEAI_API_KEY=your-key")
        print("    Get one at: https://loyueai.com")
    else:
        chat_example()
        budget_example()
