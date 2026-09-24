class Payement:
    def process_payement(self):
        print("Payement processing")
class UPI(Payement):
    def process_payement(self):
        print("Processing UPI payement")
class creditcard(Payement):
    def process_payement(self):
        print("Processing credit card payement")
        
payements=[UPI(),creditcard()]
for p in payements:
    p.process_payement()
        
