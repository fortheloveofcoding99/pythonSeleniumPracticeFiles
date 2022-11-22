
engine = 'Motor Vehicle' # global variable

class MiniTruck:  # declaring class

    def __init__(self,manufacture): # constructor called at the time of object creation
        print('{} engine from manufacturer {}'.format(engine,manufacture)) #
    wheels = 6  #class variable

    def specification(self,gear):
        print('No of wheels: ',self.wheels) # calling the class variable
        print('Gear type is : ',gear) #local varibale



# mt = MiniTruck('Volvo')
# mt.specification('Auto')
#
# mt1 = MiniTruck('Tata')     #different objects of the same class
# mt1.specification('manual')

mt2 = MiniTruck('Ashok Leyland')
mt2.wheels=4        # have changed the value of the class variable
mt2.specification('Auto')