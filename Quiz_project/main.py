from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for que in question_data:
    question = Question(que["text"], que["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
