class Student():
    def __init__(self, first_name, last_name, year, homeroom_teacher, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.homeroom_teacher = homeroom_teacher
        self.gender = gender

    def describe(self):
        if self.gender == "female":
            pronoun = "her"
        elif self.gender == "male":
            pronoun = "his"
        else:
            pronoun = "their"
        print(f"{self.first_name} {self.last_name} is in year {self.year} and {pronoun} homeroom teacher is {self.homeroom_teacher}")

first_name = input("First name: ")
last_name = input("Last name: ")
year = input("Year: ")
homeroom_teacher = input("Homeroom teacher: ")
gender = input("Gender (male/female/non-binary): ")
student1 = Student(first_name, last_name, year, homeroom_teacher, gender)

student1.describe()