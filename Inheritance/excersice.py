class Person:
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def printstudentinfo(self):
        print(f'''
Firstname: {self.firstname}
LastName: {self.lastname}
Age: {self.age}
Gender: {self.gender}
''')
        

class Student(Person):
    def __init__(self, firstname, lastname, age, gender, course, department):
        super().__init__(firstname, lastname, age, gender)
        self.department = department
        self.course = course

    def welcome(self):
        print(f"welcome {self.lastname} your department is {self.department} and course is {self.course}")


faith = Student("Jacob", "Daniel", 27, "male", "Science", "Biochemistry")

faith.welcome()