from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random
question_bank = [Question(data['question'], data["correct_answer"], data["type"], data["incorrect_answers"]) for data in question_data]
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}. ")


