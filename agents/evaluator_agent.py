from services.llm_service import analyze_text

def evaluate_answer(answer):

    score = analyze_text(answer)

    return {
        "score": score
    }
