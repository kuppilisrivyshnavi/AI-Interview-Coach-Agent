def generate_feedback(score):

    if score > 80:

        feedback = "Excellent answer. Your communication is clear and well structured."

    elif score > 60:

        feedback = "Good answer but you can improve clarity and add more examples."

    elif score > 40:

        feedback = "Your answer needs better structure and clearer explanation."

    else:

        feedback = "Try to organize your answer with clear sentences and examples."

    suggestion = "Practice structured responses using the STAR method."

    return {
        "feedback": feedback,
        "suggestion": suggestion
    }
