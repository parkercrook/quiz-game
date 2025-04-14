import question_model
import data
import quiz_brain

question_bank = []
for q in data.question_data:
    question_bank.append(question_model.Question(q["question"], q["correct_answer"]))

quiz_giver = quiz_brain.QuizBrain(question_bank)

while quiz_giver.still_has_questions():
    quiz_giver.next_question()

print("You've completed the quiz.")
print(f"Final score: {quiz_giver.score}/{quiz_giver.question_number}")