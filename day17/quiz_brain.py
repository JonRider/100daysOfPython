class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, guess, answer):
        if guess.lower() == answer.lower():
            print("You're Right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer is: {answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(guess, question.answer)

    def quiz_completed(self):
        print("You've completed the quiz.")
        print(f"Your final score was {self.score}/{self.question_number}.")

