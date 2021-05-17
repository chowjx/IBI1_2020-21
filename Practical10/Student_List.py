# Create a class called Student
class Student:
    def __init__(self, name, programme):
        self.name = name
        self.programme = programme

    def introduce_student(self):
        print('Student Name: ' + self.name, 'Undergrad Programme: ' + self.programme)

# Set object with given student name and programme as attributes
i = Student('Yang Min Mei', 'BMS') # Example
ii = Student('Mason Leong Jie Ming', 'BMI') #Example

# call function in class on objects for output
i.introduce_student()
ii.introduce_student()
