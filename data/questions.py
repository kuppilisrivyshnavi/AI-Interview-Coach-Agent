import random

interview_questions = [

"Tell me about yourself",

"What are your strengths?",

"What are your weaknesses?",

"Why do you want to work at this company?",

"Describe a challenging project you worked on",

"Where do you see yourself in five years?",

"Why should we hire you?",

"Explain a technical concept you recently learned",

"Describe a situation where you solved a problem",

"How do you handle deadlines and pressure?"

]

def get_question():

    return random.choice(interview_questions)
