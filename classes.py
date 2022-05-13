# A class is like a blueprint for creating objects. An object has
#properties and methods(functions) associated with it. Almost everything in python is an object

class User:
    def __init__(self,name, email,age):
       self.name=name
       self.email =email
       self.age=age
       
    def greeting(self):
        return f'My name is {self.name} and am {self.age} '
    def has_birthday(self):
           self.age +=1  
#init your object



#extends class
class Customer(User):
     def __init__(self,name, email,age):
      self.name=name
      self.email =email
      self.age=age
      self.balance =0
      
     def set_balance(self,balance):
        self.balance =balance
     def greeting(self):
        return f'My name is {self.name} and am {self.age} and my balance is {self.balance} '
#init a customer
brad = User('John Doe','brad@gmail.com',37)
janet = Customer('Janet Johnson','janet@yahoo.com',25)
#janet can still access the parent element it extended you get
"""print(type(brad))
print(brad.name)
print(brad.email)
print(brad.age)"""
brad.has_birthday()
print(brad.greeting())
print(type(User))
janet.set_balance(200)
print(janet.greeting)