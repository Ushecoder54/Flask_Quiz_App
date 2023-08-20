from flask import Flask, jsonify, render_template
from questions import get_questions
from quiz import create_quiz

app = Flask(__name__)

quiz_instance = create_quiz()

@app.route("/")
def index():
    return "Welcome to AfricAI Quiz App!"

@app.route("/get_question")
def get_question():
    if not quiz_instance.is_finished():
        current_question = quiz_instance.get_current_question()
        return jsonify({
            "question_text": current_question.question_text,
            "answer_choices": current_question.answer_choices
        })
    else:
        return "Quiz is finished."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
