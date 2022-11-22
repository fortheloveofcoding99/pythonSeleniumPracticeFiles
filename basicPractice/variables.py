
bank ='HDFC' # global variable

class department:
    loanType = 'Home Loan' #class variables

    def loanInfo(self,name,loanNum):
        self.name = name    #local variable
        self.loanNum = loanNum  #local variable

        print('Name of the holder: {} with Loan # : {} is a {} from {} bank'.format(name,loanNum,self.loanType,bank))


d = department()
d.loanInfo('Ram','232')