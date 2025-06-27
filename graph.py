from langgraph.graph import StateGraph
from state import GraphState
from nodes.complexity import is_complex_question
from nodes.decompose import decompose_question
from nodes.resolver import resolve_atomic_question
from nodes.aggregator import aggregate_answers


def run_question_graph(input_question):
    state = GraphState.initialize(input_question)

    graph = StateGraph(GraphState)
    graph.add_node("complexity", is_complex_question)
    graph.add_node("decompose", decompose_question)
    graph.add_node("resolve", resolve_atomic_question)
    graph.add_node("aggregate", aggregate_answers)

    graph.set_entry_point("complexity")
    graph.add_edge("complexity", "decompose")
    graph.add_edge("decompose", "resolve")
    graph.add_edge("resolve", "aggregate")
    graph.add_edge("aggregate", "__end__")

    executable_graph = graph.compile()
    final_state = executable_graph.invoke(state)

    return final_state.to_json()