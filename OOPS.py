# ALL OOP CONCEPTS IN PYTHON

# 1. CLASS & OBJECT
class Student:
    
    # Constructor
    def __init__(self, name, age):
        self.name = name       
        self.age = age
    
    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating object
s1 = Student("Pratham", 22)
print("===== CLASS & OBJECT =====")
s1.display()

# 2. ENCAPSULATION
class BankAccount:
    
    def __init__(self, balance):
        self.__balance = balance   # Private variable
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

print("\n===== ENCAPSULATION =====")
acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

# 3. INHERITANCE
class Person:
    
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print("Name:", self.name)

class Teacher(Person):   # Inheriting Person
    
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    def show_teacher(self):
        print("Subject:", self.subject)

print("\n===== INHERITANCE =====")
t1 = Teacher("Rahul", "Data Science")
t1.show()
t1.show_teacher()

# 4. POLYMORPHISM
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

print("\n===== POLYMORPHISM =====")
for animal in (Dog(), Cat()):
    animal.sound()

# 5. METHOD OVERRIDING
class Animal:
    def speak(self):
        print("Animal makes sound")

class Cow(Animal):
    def speak(self):  # Overriding method
        print("Cow says Moo")

print("\n===== METHOD OVERRIDING =====")
c = Cow()
c.speak()

# 6. CLASS VARIABLE
class Company:
    company_name = "TechCorp"   # Class variable
    
    def __init__(self, employee):
        self.employee = employee

print("\n===== CLASS VARIABLE =====")
emp1 = Company("Amit")
emp2 = Company("Ravi")

print(emp1.employee, "-", Company.company_name)
print(emp2.employee, "-", Company.company_name)