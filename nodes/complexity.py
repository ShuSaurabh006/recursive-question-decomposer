def is_complex_question(state):
    q = state.original_question.lower()
    if any(w in q for w in ["compare", "trend", "top", "each", "highest"]):
        state.log.append("Detected as complex question.")
        return "decompose"
    else:
        state.log.append("Detected as atomic question.")
        return "resolve"
