class Grade_Calculator:
    def __init__(self, name, portfolio_grade, poster_grade, exam_grade):
        self.name = name
        self.portfolio_grade = portfolio_grade
        self.poster_grade = poster_grade
        self.exam_grade = exam_grade
        
    def get_user_input():

        global name
        global portfolio_grade
        global poster_grade
        global exam_grade

        name = str(input("What's your name?"))
        portfolio_grade = float(input("What's the % grade for your code portfolio?"))
        poster_grade = float(input("What's the % grade for your poster presentation?"))
        exam_grade = float(input("What's the % grade for your final exam?"))
        return name, portfolio_grade, poster_grade, exam_grade
    
    def grade_calculation():
        Final_Grade = (portfolio_grade/100)*40 + (poster_grade/100)*30 + (exam_grade/100)*30
        print("Student's Name: " + name, "Final Grade: " + str(Final_Grade))

def main():
    Grade_Calculator.get_user_input()
    Grade_Calculator.grade_calculation()

main()





