import random


class QuizBrain:

    def __init__(self, question_list):
        self.number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[random.randint(
            0, len(self.question_list)-1)]
        self.number += 1
        user_answer = input(
            f"Q{self.number}. {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your score is {self.score}/{self.number}")
        else:
            print("That's Wrong.")
            print(f"Your score is {self.score}/{self.number}")
        print(f"Correct answer is {correct_answer}")
        print("\n")
