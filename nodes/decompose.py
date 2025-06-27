def decompose_question(state):
    q = state.original_question.lower()
    if "category" in q and "highest revenue" in q:
        state.sub_questions = [
            {"question": "What was the total revenue of each product category in Q1 2023?", "status": "pending", "answer": None}
        ]
    else:
        state.sub_questions = [{"question": state.original_question, "status": "pending", "answer": None}]
    state.log.append(f"Decomposed into {len(state.sub_questions)} sub-questions.")
    return state
