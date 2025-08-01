from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    question_obj = Question(question['question'], question['correct_answer'])
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    
print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")