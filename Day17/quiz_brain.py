import random


class QuizBrain:
    import random
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    def next_question(self):
        question = self.question_list[self.question_number]
        random.shuffle(question.choices)
        self.question_number += 1
        self.answer = input(f"Q.{self.question_number}:{question.question}. \nOptions: {tuple(question.choices)}: ")
        self.check_answer(self.answer, question.answer)
    def still_has_questions(self):
        return(self.question_number < len(self.question_list))
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print("That's Wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")