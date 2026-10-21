class Calculator:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero!"

calc = Calculator()
print(calc.divide(10, 2))
print(calc.divide(5, 0))
