class Grade_Calculator:      
    # create function to get user to input student's name & scores
    def get_user_input():
        # make variables accessible outside of the function as well
        global name
        global portfolio_grade
        global poster_grade
        global exam_grade

        name = str(input("What's your name?"))
        portfolio_grade = float(input("What's the % grade for your code portfolio?"))
        poster_grade = float(input("What's the % grade for your poster presentation?"))
        exam_grade = float(input("What's the % grade for your final exam?"))
        return name, portfolio_grade, poster_grade, exam_grade
    
    # Create function to calculate final grade from the weighted percentages and scores
    def grade_calculation():
        Final_Grade = (portfolio_grade/100)*40 + (poster_grade/100)*30 + (exam_grade/100)*30
        print("Student's Name: " + name, "Final Grade: " + str(Final_Grade))

# Create a function to call other functions in desired order
def main():
    Grade_Calculator.get_user_input()
    Grade_Calculator.grade_calculation()

# Call the main function that will call other functions to output entire program
main()





