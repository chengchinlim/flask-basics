class Student: 
    def __init__(self): # constructor
        self.name = "Cheng"
        self.numbers = (1, 2, 3, 4, 5)

    def __str__(self): # toString()
        return f"Name: {self.name}, Numbers: {self.numbers}"

    def average(self):
        return sum(self.numbers) / len(self.numbers)

student = Student()
print(student.average())
print(student)