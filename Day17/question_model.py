class Question:
    def __init__(self, question, answer, type, wrong_ans):
        self.question = question
        self.answer = answer
        self.type = type
        self.choices = wrong_ans + [self.answer]