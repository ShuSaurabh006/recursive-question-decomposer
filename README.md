# 🧠 Recursive Question Decomposer – LangGraph + LLM + CSV Analyzer

This project is a CLI-based system that takes complex natural language questions about store sales data and recursively decomposes them into smaller sub-questions using LangGraph, then resolves them with pandas over real CSV data.

Built as part of the **Python Internship Task at Grassroots Lab**.

---

## ✅ Features

- ✅ Detects if the input question is atomic or complex
- 🔁 Recursively breaks down complex questions into simpler sub-questions
- 📊 Answers questions using real transactional sales data (`pandas`)
- 🧩 Uses LangGraph nodes for orchestration (decision → decomposition → resolution → aggregation)
- 💬 Logs every step with full traceability
- 🧾 Outputs final result in structured JSON
- 🖥️ Simple command-line interface using `typer`

---

## 💻 Example Questions Supported

```bash
python main.py ask "Which product category had the highest revenue in Q1 2023?"
python main.py ask "Which store had the highest average basket size in March 2023?"
python main.py ask "Did sales increase or decrease for beverages from January to June 2023?"

📁 Project Structure
recursive-question-decomposer/
├── main.py               # CLI entry point
├── graph.py              # LangGraph definition
├── state.py              # Graph state class
├── utils.py              # Optional helpers
├── nodes/
│   ├── complexity.py     # Decides if a question is complex
│   ├── decompose.py      # Breaks complex questions into sub-questions
│   ├── resolver.py       # Answers atomic questions using pandas
│   └── aggregator.py     # Combines sub-answers into a final result
├── data/
│   └── Master_Sales.csv  # CSV file with store sales data
└── README.md             # Project documentation

⚙️ Installation
git clone https://github.com/ShuSaurabh006/recursive-question-decomposer.git
cd recursive-question-decomposer
pip install -r requirements.txt

🚀 How to Use
python main.py ask "YOUR COMPLEX QUESTION HERE"


📦 Requirements
pip install -r requirements.txt


👨‍💻 Author
Name: Saurabh Shukla

Email: shusaurabh006@gmail.com

GitHub: ShuSaurabh006

This project was built as part of the Python Internship Task at Grassroots Lab, supporting the Hi Market business analytics initiative.