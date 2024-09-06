class Money:
    def __init__(self,qur,dim,nik,pen,cof):
        self.qur = qur
        self.dim = dim
        self.nik = nik
        self.pen = pen
        self.cof = cof

    def calculation(self):
        self.qur *= 0.25
        self.dim *= 0.1
        self.nik *= 0.05
        self.pen *= 0.01
        return self.qur+self.dim+self.nik+self.pen
    def check_amount(self):
        global amount
        if self.cof == 'latte':
            amount = 2.5
        elif self.cof == 'cappuccino':
            amount = 3.0
        elif self.cof == 'cappuccino':
            amount = 1.5
        balance = self.calculation()-amount
        if balance>=0:
            print(f'You have enough money.Your balance is ${balance:2f}')
            print('Enjoy your coffee')
            return True
        else:
            print("You haven't enough money\n Please enter enough money")
            return False





