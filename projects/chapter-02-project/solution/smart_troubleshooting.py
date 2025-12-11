"""
Solution code for the Chapter 2 project: Smart IoT Troubleshooting Assistant.

Design goals:
- Runnable without network access (deterministic pseudo-embeddings).
- Clear, testable functions for counting tokens, estimating cost,
  creating embeddings, semantic search, and context management.
- Easy to swap embedding backend: replace `create_embedding` with
  OpenAI/Ollama embeddings when desired.
"""

from __future__ import annotations

import hashlib
import math
from typing import List, Tuple, Dict

import numpy as np

try:
    import tiktoken
except ImportError:
    tiktoken = None


# --- Token counting and cost -------------------------------------------------

PRICING_PER_MILLION = {
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "default": {"input": 0.15, "output": 0.60},
}


def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    if tiktoken:
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    return max(1, math.ceil(len(text) / 4))


def estimate_cost(text: str, is_input: bool = True, model: str = "gpt-4o-mini") -> float:
    tokens = count_tokens(text, model)
    pricing = PRICING_PER_MILLION.get(model, PRICING_PER_MILLION["default"])
    rate = pricing["input"] if is_input else pricing["output"]
    return (tokens / 1_000_000) * rate


# --- Embeddings & semantic search -------------------------------------------

def create_embedding(text: str, dims: int = 96) -> np.ndarray:
    """Deterministic pseudo-embedding; swap with OpenAI/Ollama for production."""
    h = hashlib.sha256(text.encode("utf-8")).digest()
    raw = (h * ((dims // len(h)) + 1))[:dims]
    arr = np.frombuffer(raw, dtype=np.uint8).astype(np.float32) / 255.0
    norm = np.linalg.norm(arr) or 1.0
    return arr / norm


def create_knowledge_base_embeddings(solutions: List[str]) -> List[np.ndarray]:
    return [create_embedding(s) for s in solutions]


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    denom = (np.linalg.norm(a) * np.linalg.norm(b)) or 1.0
    return float(np.dot(a, b) / denom)


def find_best_solution(
    user_problem: str,
    solutions: List[str],
    embeddings: List[np.ndarray],
) -> Tuple[str, float]:
    problem_emb = create_embedding(user_problem)
    best_idx = -1
    best_score = -1.0
    for idx, emb in enumerate(embeddings):
        score = cosine_similarity(problem_emb, emb)
        if score > best_score:
            best_idx = idx
            best_score = score
    if best_idx == -1:
        return "No solution found.", 0.0
    return solutions[best_idx], best_score


# --- Context management ------------------------------------------------------

def manage_context(messages: List[Dict], max_tokens: int = 6000) -> List[Dict]:
    """Keep system message; trim oldest user/assistant messages to fit the limit."""
    if not messages:
        return messages

    system_msgs = [m for m in messages if m.get("role") == "system"]
    others = [m for m in messages if m.get("role") != "system"]

    def total_tokens(msgs: List[Dict]) -> int:
        return sum(count_tokens(m.get("content", "")) for m in msgs)

    trimmed = others[:]
    while total_tokens(system_msgs + trimmed) > max_tokens and trimmed:
        trimmed.pop(0)

    return system_msgs + trimmed


# --- CLI ---------------------------------------------------------------------

SOLUTIONS = [
    "Check for direct sunlight hitting the sensor; it can cause false high readings.",
    "Restart the device's WiFi router if connectivity issues persist.",
    "Recalibrate the sensor against a known temperature source to ensure accuracy.",
    "Replace the device's battery if power levels drop below 10%.",
    "Inspect wiring connections for loose or corroded contacts.",
    "Verify device firmware is up to date.",
    "Ensure the sensor is not blocked by obstructions.",
    "Factory reset the device if other steps fail.",
]


def run_cli():
    embeddings = create_knowledge_base_embeddings(SOLUTIONS)
    history: List[Dict] = [
        {"role": "system", "content": "You are a helpful IoT troubleshooting assistant."}
    ]

    print("Smart IoT Troubleshooting Assistant (solution)")
    print("Type 'quit' to exit.\n")
    while True:
        user = input("User: ").strip()
        if user.lower() in {"quit", "exit"}:
            break

        best_solution, score = find_best_solution(user, SOLUTIONS, embeddings)
        cost_estimate = estimate_cost(user, is_input=True)
        reply = (
            f"Suggested fix (similarity {score:.2f}): {best_solution}"
            f"\n(Est. input cost: ${cost_estimate:.6f})"
        )

        print(f"Assistant: {reply}\n")
        history.append({"role": "user", "content": user})
        history.append({"role": "assistant", "content": reply})
        history = manage_context(history)


if __name__ == "__main__":
    run_cli()

