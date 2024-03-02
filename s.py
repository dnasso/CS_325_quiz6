#Storing order details (customer info, items, shipping address)
#Calculating total order cost (including taxes and discounts)
#Validating order data (checking item availability, customer address etc.)
#Sending order confirmation emails to customers
#Updating inventory levels after order processing

class orderDetails:
    def __init__(self, data):
        self.data = data
        print("Data stored")
    def setData(self, data):
        self.data = data
        print("Data stored")
    def getData(self):
        print("Data grabbed")
        return self.data
class orderCost:
    def calculateCost(self, data):
        print("Cost calculated")
        return "<Placeholder String>"
class orderValidation:
    def checkData (self, data):
        print("Order checeked")
        return "<Placeholder String>"
class orderConfirmation:
    def confirmOrder (self, data):
        print("Confirmation email sent")
class inventory:
    def __init__(self):
        self.inventory = []
    def addItem(self, data):
        print("Data added")
    def removeItem(self, data):
        print("Data removed")