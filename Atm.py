class Atm:
    def __init__(self, cardNom, pinNom):
        self.cardNom=cardNom
        self.pinNom=pinNom
    def cashWithdrawl(self):
        print("cash withdrawl for "+self.cardNom+". Your pin is "+self.pinNom)
    def balanceEnquiry(self):
        print("balance enquiry for "+self.cardNom+". Your pin is "+self.pinNom)

atmOne=Atm("Ann", "1234")
atmOne.cashWithdrawl()