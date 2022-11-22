# class Emp:
#     eid = 0       # creating class variables
#     ename =''
#     esal = 0
#     company = 'Lancom'
#     def __init__(self,id,name,sal): # giving values to the class variables inside the constructor
#         self.eid = id
#         self.ename = name
#         self.esal = sal
#
#     def display(self):
#         print('Name des mitarbeiter: {} Ausweis nummer : {} Gehalt : {} Arbeit fur {}'.format(self.ename,self.eid,self.esal,self.company))
#
# e=Emp(2232,'desmond hayes',34545)
# e.display()

class Lib:
    def __init__(self,name,category,author,price):# creating the class variable inside the constructor
        self.category=category
        self.author=author
        self.price=price
        self.name=name

    def display(self):
        print('{} is the title of the book, written by {} the category is {}. The price of the book is {}'.format(self.name,self.author,self.category,self.price))




l=Lib('God Created Integers','Astronomy','Stephen Hawking',500.00)
l.display()