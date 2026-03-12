# AI Interview Coach Agent

AI Interview Coach Agent is an intelligent system that simulates a mock interview and evaluates candidate answers.

The system uses multiple AI agents to perform different tasks such as asking questions, evaluating answers, and generating feedback.

---

## Features

- Interview question generation
- Answer evaluation
- Communication score calculation
- Feedback generation
- REST API interface

---

## Architecture

User  
↓  
API Server  
↓  
Interviewer Agent → Generates interview questions  
↓  
Evaluator Agent → Scores the answer  
↓  
Feedback Agent → Generates improvement suggestions  
↓  
Response returned to user

---

## Project Structure

AI-Interview-Coach-Agent

agents  
interviewer_agent.py  
evaluator_agent.py  
feedback_agent.py  

services  
llm_service.py  

api  
app.py  

data  
questions.py  

requirements.txt  
README.md  

---

## Installation

Clone repository

git clone https://github.com/YOUR_USERNAME/AI-Interview-Coach-Agent.git

Install dependencies

pip install -r requirements.txt

Run server

python api/app.py

---

## Example API Usage

Get Interview Question

GET /question

Example Response

{
 "question": "Tell me about yourself"
}

Evaluate Answer

POST /evaluate

Request

{
 "answer": "I am a computer science student passionate about AI and problem solving."
}

Response

{
 "score": 78,
 "feedback": "Good answer but you can improve clarity and add more examples.",
 "suggestion": "Practice structured responses using the STAR method."
}

---

## Future Improvements

- Integrate OpenAI or Groq API
- Add conversation memory
- Add speech based interview practice
- Build a web interface

---

## Author

Srivyshnavi Kuppili
