class Student:
    def __init__(self, name, section, age):
        self.name = name
        self._section = section #Protected
        self.__age = age #Private

    #getter method
    def get_age(self):
        return self.__age

    #setter method
    def set_age(self,age):
        self.__age = age

    #getter method
    def get_section(self):
        return self._section

    #setter method
    def set_section(self,section):
        self._section = section

stud = Student("Rose","Pink",21)

#retrieving age and section using getter
print("Name:", stud.name, stud.get_section(), stud.get_age())

#changing age and section using setter
stud.set_age(26)

stud.set_section("Blue")

#retrieving age and setter using getter
print("Name:", stud.name, stud.get_section(), stud.get_age())
    
