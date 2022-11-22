
class Cars:
    wheels = 4
    seats = 6
    make = 'BMW'
    def __init__(self):
        print('cars constructor')
    def comDetails(self):
        print(self.make,self.wheels,self.seats)

class Coupe(Cars):
    def __init__(self):
        self.Transmission = 'manual'
        self.type = 'SUV'
        print('Trnsmission is {}, Type is {}'.format(self.Transmission,self.type))




