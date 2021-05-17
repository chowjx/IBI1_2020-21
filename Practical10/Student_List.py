# Create a class called Student
class Student:
    def __init__(self, first_name, last_name, programme):
        self.first_name = first_name
        self.last_name = last_name
        self.programme = programme

    def introduce_student(self):
        print(self.first_name + " " + self.last_name + " " + self.programme)

# Set object with given student name and programme as attributes
i = Student('Min Mei', 'Yang', 'BMS') # Example
ii = Student('Jie Ming', 'Leong', 'BMI') #Example

# call function in class on objects for output
i.introduce_student()
ii.introduce_student()
