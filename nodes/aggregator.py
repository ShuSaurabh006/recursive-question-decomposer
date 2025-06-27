def aggregate_answers(state):
    final = " | ".join([sq["answer"] for sq in state.sub_questions])
    state.final_answer = final
    state.log.append("Aggregated final answer.")
    return state
