
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Bill:
    def __init__(self, products, tax_rate=0.05):
        self.products = products
        self.tax_rate = tax_rate

    def calculate_total(self):
        subtotal = sum(p.price * p.quantity for p in self.products)
        tax = subtotal * self.tax_rate
        total = subtotal + tax
        return subtotal, tax, total

    def display_bill(self):
        print("----- Final Bill -----")
        print(f"{'Product':10}{'Price':10}{'Qty':5}{'Total':10}")
        for p in self.products:
            print(f"{p.name:10}{p.price:<10}{p.quantity:<5}{p.price * p.quantity:<10}")
        subtotal, tax, total = self.calculate_total()
        print("----------------------")
        print(f"Subtotal: {subtotal}")
        print(f"Tax: {tax}")
        print(f"Grand Total: {total}")

# Example usage
products = [
    Product("Pen", 10, 2),
    Product("Notebook", 50, 3),
    Product("Bag", 500, 1)
]

bill = Bill(products)
bill.display_bill()
