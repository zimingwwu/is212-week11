class Electronics:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def apply_discount(self):
        discount = 0.10  # 10% discount
        discounted_price = self.price - (self.price * discount)
        print(f"Discounted price for {self.name} (Electronics): {discounted_price}")
        return discounted_price
    
    def calculate_tax(self):
        tax_rate = 0.15  # 15% tax
        tax = self.price * tax_rate
        print(f"Tax for {self.name} (Electronics): {tax}")
        return tax

class Clothing:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        discount = 0.20  # 20% discount
        discounted_price = self.price - (self.price * discount)
        print(f"Discounted price for {self.name} (Clothing): {discounted_price}")
        return discounted_price
    
    def calculate_tax(self):
        tax_rate = 0.08  # 8% tax
        tax = self.price * tax_rate
        print(f"Tax for {self.name} (Clothing): {tax}")
        return tax

class Grocery:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def apply_discount(self):
        discount = 0.05  # 5% discount
        discounted_price = self.price - (self.price * discount)
        print(f"Discounted price for {self.name} (Grocery): {discounted_price}")
        return discounted_price
    
    def calculate_tax(self):
        tax_rate = 0.02  # 2% tax
        tax = self.price * tax_rate
        print(f"Tax for {self.name} (Grocery): {tax}")
        return tax
