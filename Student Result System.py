# Base Class
class Student:
    
    def __init__(self, name, mark1, mark2):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2

    def calculate_total(self):
        return self.mark1 + self.mark2

    def calculate_average(self):
        return self.calculate_total() / 2

    def display_result(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.calculate_total())
        print("Average Marks:", self.calculate_average())


# Child Class
class GradeStudent(Student):

    def display_result(self):   # Method Overriding
        total = self.calculate_total()
        avg = self.calculate_average()

        print("Student Name:", self.name)
        print("Total Marks:", total)
        print("Average Marks:", avg)

        if avg >= 90:
            print("Grade: A")
        elif avg >= 75:
            print("Grade: B")
        elif avg >= 50:
            print("Grade: C")
        else:
            print("Grade: Fail")


# Main Program
name = input("Enter student name: ")
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))

student = GradeStudent(name, m1, m2)
student.display_result()