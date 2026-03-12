from flask import Flask, jsonify, request

from agents.interviewer_agent import ask_question
from agents.evaluator_agent import evaluate_answer
from agents.feedback_agent import generate_feedback

app = Flask(__name__)

@app.route("/")
def home():

    return jsonify({
        "message": "AI Interview Coach Agent Running"
    })


@app.route("/question", methods=["GET"])
def get_question():

    question = ask_question()

    return jsonify(question)


@app.route("/evaluate", methods=["POST"])
def evaluate():

    data = request.json

    answer = data.get("answer")

    if not answer:

        return jsonify({
            "error": "Answer required"
        }),400

    evaluation = evaluate_answer(answer)

    feedback = generate_feedback(evaluation["score"])

    return jsonify({

        "score": evaluation["score"],
        "feedback": feedback["feedback"],
        "suggestion": feedback["suggestion"]

    })


if __name__ == "__main__":

    app.run(debug=True)
