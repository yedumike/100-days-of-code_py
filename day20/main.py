from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score is {quiz.score}/{quiz.number}")