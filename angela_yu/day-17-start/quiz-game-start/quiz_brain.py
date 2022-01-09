class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    # def next_question(self):
    #     self.question_number += 1
    #     input(f"Q.{self.question_number}: {self.question_list[self.question_number].text}. (True or False)?: ")


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False)?: ")
        self.is_answer_correct(user_answer, current_question.answer)

    
    def is_answer_correct(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Current score: {self.score}/{self.question_number}")
        print("\n")