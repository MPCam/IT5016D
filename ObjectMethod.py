class Person:
    def __init__ (self, age, gender):
        self.age = age
        self.gender = gender

harry = Person(36, "Male")
sarah = Person(34, "Female")

def myIntro(self):
    print("Hello my gender is " + self.gender)
    print("Hello my age is ", self.age)
   
myIntro(harry)
myIntro(sarah)
