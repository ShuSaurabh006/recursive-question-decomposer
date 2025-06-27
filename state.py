import json
from typing import List

class GraphState:
    def __init__(self, original_question, sub_questions=None, final_answer=None, log=None):
        self.original_question = original_question
        self.sub_questions = sub_questions or []
        self.final_answer = final_answer
        self.log = log or []

    @staticmethod
    def initialize(question):
        return GraphState(original_question=question)

    def to_json(self):
        return json.dumps({
            "original_question": self.original_question,
            "sub_questions": self.sub_questions,
            "final_answer": self.final_answer,
            "log": self.log
        }, indent=2)
