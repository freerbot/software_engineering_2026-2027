class Student():
    def __init__(self, first_name, last_name, year, homeroom_teacher):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.homeroom_teacher = homeroom_teacher

    def describe(self):
        print(f"{self.first_name} {self.last_name} is in year {self.year} and is in {self.homeroom_teacher}'s homeroom.")

first_name = input("First name: ")
last_name = input("Last name: ")
year = input("Year: ")
homeroom_teacher = input("Homeroom teacher: ")

student1 = Student(first_name, last_name, year, homeroom_teacher)

student1.describe()