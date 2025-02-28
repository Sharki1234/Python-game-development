import random
class Question:
    def __init__(self,text,options,answer):
        self.text = text
        self.options = options
        self.answer = answer

    def check(self,answ):
        tex = self.options[answ-1]
        if tex == self.answer:
            return 1
        else:
            return 0

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        random.shuffle(self.questions)
    
    def begin(self):
        score = 0
        for num in self.questions:
            print(num.text)
            for i in range(len(num.options)):
                print(f"{i+1} {num.options[i]}")

            user = int(input("What is your answer?"))
            score+=num.check(user)
        print(f"your score is {score}/{len(self.questions)}")

    



questions_list = [
        Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
        Question("Which language is primarily used for web development?", ["Python", "Java", "JavaScript", "C++"], "JavaScript"),
        Question("Who developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"], "Albert Einstein"),
        Question("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
        Question("Which element has the chemical symbol 'O'?", ["Oxygen", "Gold", "Osmium", "Hydrogen"], "Oxygen")]


example = Quiz(questions_list)
example.begin()

