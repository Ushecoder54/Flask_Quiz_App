from typing import List

class Question:
    def __init__(self, question_text: str, answer_choices: List[str], correct_answer: str):
        self.question_text = question_text
        self.answer_choices = answer_choices
        self.correct_answer = correct_answer

    def is_answer_correct(self, answer: str) -> bool:
        """Returns True if the given answer is correct for this question, False otherwise."""
        return answer == self.correct_answer

def get_questions() -> List[Question]:
    """
    Returns a list of Question objects.
    """
    questions_data = [
        {
            "question": "Which large mammal is known for its distinctive tusks and is native to African savannas?",
            "options": ["Giraffe", "Lion", "Elephant", "Zebra"],
            "answer": "Elephant"
        },
        {
                "question": "Which large mammal is known for its distinctive tusks and is native to African savannas?",
                "options": ["Giraffe", "Lion", "Elephant", "Zebra"],
                "answer": "Elephant"
            },
            {
                "question": "What is the fastest land animal and is found in the grasslands of Africa?",
                "options": ["Cheetah", "Hippopotamus", "Gorilla", "Leopard"],
                "answer": "Cheetah"
            },
            {
                "question": "Which large mammal is known for its distinctive tusks and is native to African savannas?",
                "options": ["Giraffe", "Lion", "Elephant", "Zebra"],
                "answer": "Elephant"
            },
            {
                "question": "What is the fastest land animal and is found in the grasslands of Africa?",
                "options": ["Cheetah", "Hippopotamus", "Gorilla", "Leopard"],
                "answer": "Cheetah"
            },
            {
                "question": "Which species of ape is found in the forests of Central and West Africa, known for its intelligence and tool-making abilities?",
                "options": ["Baboon", "Chimpanzee", "Orangutan", "Gorilla"],
                "answer": "Chimpanzee"
            },
            {
                "question": "What is the national bird of Kenya, known for its vibrant red and blue plumage?",
                "options": ["Secretary Bird", "African Grey Parrot", "Lilac-breasted Roller", "Ostrich"],
                "answer": "Lilac-breasted Roller"
            },
            {
                "question": "Which large carnivore is known for its distinctive black mane and is often referred to as the 'King of the Jungle'?",
                "options": ["Leopard", "Cheetah", "Hyena", "Lion"],
                "answer": "Lion"
            },
            {
                "question": "Which animal, known for its unique stripes, is native to African grasslands and is often associated with the Serengeti?",
                "options": ["Giraffe", "Zebra", "Elephant", "Rhino"],
                "answer": "Zebra"
            },
            {
                "question": "What is the largest land animal on Earth, characterized by its long neck and legs?",
                "options": ["Giraffe", "Hippopotamus", "African Elephant", "Gorilla"],
                "answer": "Giraffe"
            },
            {
                "question": "Which aquatic mammal is found in African rivers, is known for its aggressive nature, and has large jaws and teeth?",
                "options": ["Dolphin", "Manatee", "Hippopotamus", "Seal"],
                "answer": "Hippopotamus"
            },
            {
                "question": "What is the fastest marine animal and is known for its powerful jumps and acrobatics?",
                "options": ["Shark", "Dolphin", "Sea Turtle", "Sailfish"],
                "answer": "Dolphin"
            },
            {
                "question": "Which large herbivore is known for its distinctive hump and is adapted to desert life?",
                "options": ["Buffalo", "Camel", "Giraffe", "Rhinoceros"],
                "answer": "Camel"
            },
        ]
    
    questions = []
    for qdata in questions_data:
        question = Question(qdata["question"], qdata["options"], qdata["answer"])
        questions.append(question)
    
    return questions
