class Airlines:
    airlines ='Spice Jet'
    flights = 0
    def __init__(self):
        print('All Airlines information')
        self.airlines = 'goair'
        self.flights = 12
        print(self.airlines,self.flights)

    @staticmethod
    def type(self,typ):
        print(self, typ)

Airlines.type('Indigo','Domestic')  # invoking the static method direct through the class not through the object
al=Airlines()
print(al.airlines) # invoking the instance method