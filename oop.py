class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices= choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer
    
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.index = 0
    def getQuestion(self):
        return self.questions[self.index]
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.index+1}/{len(questions)}: {question.text}")
        for q in question.choices:
            print('-'+q)
        answer = input('Answer ')
        self.guess(answer)
        self.quitGame()
    def guess(self, answer):
        question= self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score +=1
        self.index +=1

        
    def quitGame(self):
        if len(questions)== self.index:
            self.showScore()
        else:
                        
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"Score: ", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.index+1

        if questionNumber>totalQuestion:
            print("Quiz Bitti.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,'*'))


q1 = Question('En iyi programlama dili hangisidir?', ['Java','Python','C#','Javascript'], 'Python')
q2 = Question('En popüler programlama dili hangisidir?', ['Python','Java','C#','Javascript'], 'Python')
q3 = Question('En çok kazandıran programlama dili hangisidir?', ['C#','Java','Python','Javascript'], 'Python')
questions=[q1,q2,q3]
quiz = Quiz(questions)
quiz.quitGame()
# print(question.text)
