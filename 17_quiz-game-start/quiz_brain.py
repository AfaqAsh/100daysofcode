class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(answer, question.answer)
        return answer
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        
    def check_answer(self, answer, correct_answer):
        if (answer.lower() == correct_answer.lower()):
            self.score +=1
            print(f"Your answer is correct.")
        else:
            print("That is wrong.")
        
        
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n\n")