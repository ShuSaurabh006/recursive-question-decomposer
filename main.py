from typer import Typer
from graph import run_question_graph

app = Typer()

@app.command()
def ask(question: str):
    final_output = run_question_graph(question)
    print("\n Final Output:")
    print(final_output)

if __name__ == "__main__":
    app()