from typing import List
from questions import Question, get_questions


class Quiz:
    def __init__(self, questions: List[Question]):
        self.questions = questions
        self.current_question = 0
        self.score = 0

    def get_current_question(self) -> Question:
        return self.questions[self.current_question]

    def is_answer_correct(self, answer: str) -> bool:
        return self.get_current_question().is_answer_correct(answer)

    def answer_question(self, answer: str) -> bool:
        if self.is_answer_correct(answer):
            self.score += 1
            self.current_question += 1
            return True
        else:
            return False

    def is_finished(self) -> bool:
        return self.current_question >= len(self.questions)

    def get_score(self) -> int:
        return self.score

def create_quiz() -> Quiz:
    questions = get_questions()
    return Quiz(questions)
