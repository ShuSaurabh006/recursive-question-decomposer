import pandas as pd

DATA_PATH = "./data/Master_Sales.csv"
df = pd.read_csv(DATA_PATH)

def resolve_atomic_question(state):
    for sq in state.sub_questions:
        if sq["status"] == "pending":
            q = sq["question"].lower()
            if "product category" in q or "department" in q:
                result = df.groupby("Department")["Total Retail"].sum().sort_values(ascending=False)
                top_category = result.idxmax()
                sq["answer"] = f"Top category: {top_category} with revenue {result.max():.2f}"
            else:
                sq["answer"] = "Mock answer for now."
            sq["status"] = "answered"
    state.log.append("Resolved atomic questions using data.")
    return state
