import random

def analyze_text(answer):

    word_count = len(answer.split())

    grammar_score = random.randint(20,30)

    clarity_score = random.randint(20,30)

    structure_score = min(word_count,40)

    score = grammar_score + clarity_score + structure_score

    if score > 100:
        score = 100

    return score
