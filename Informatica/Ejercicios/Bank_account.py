class BankAccount:
    def __init__(self, acc_num):
        self.acc_num = acc_num
        self.balance = 0
        
    def depositar(self, ammount):
        ammount = float (ammount)
        self.balance = self.balance + ammount
        return (f"El nuevo balance es {self.balance}€")

    def retirar(self, ammount):
        ammount = float (ammount)
        if self.balance >= ammount:
            self.balance = self.balance - ammount
            return (f"El nuevo balance es {self.balance}€")

        else:
            return ("no existe suficiente dinero en la cuenta")
    
    def cantidad(self):
        return (f"El balance es: {self.balance}€")