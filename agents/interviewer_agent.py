from data.questions import get_question

def ask_question():

    question = get_question()

    return {
        "question": question
    }
