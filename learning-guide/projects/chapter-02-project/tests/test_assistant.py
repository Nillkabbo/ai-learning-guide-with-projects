import numpy as np

from chapter_02_project.solution.smart_troubleshooting import (
    count_tokens,
    estimate_cost,
    create_embedding,
    create_knowledge_base_embeddings,
    find_best_solution,
    manage_context,
)


def test_token_count_and_cost():
    text = "Hello AI"
    tokens = count_tokens(text)
    assert tokens > 0
    cost = estimate_cost(text, is_input=True)
    assert cost > 0.0


def test_embeddings_and_similarity():
    solutions = ["Restart router", "Replace battery"]
    embs = create_knowledge_base_embeddings(solutions)
    assert len(embs) == 2
    assert isinstance(embs[0], np.ndarray)

    best, score = find_best_solution("wifi issue", solutions, embs)
    assert best in solutions
    assert 0.0 <= score <= 1.0


def test_manage_context_trims_old_messages():
    messages = [{"role": "system", "content": "sys"}]
    for i in range(50):
        messages.append({"role": "user", "content": f"msg {i}"})
        messages.append({"role": "assistant", "content": f"reply {i}"})
    trimmed = manage_context(messages, max_tokens=300)
    # Should keep system + some recent messages
    assert any(m.get("role") == "system" for m in trimmed)
    assert len(trimmed) < len(messages)

