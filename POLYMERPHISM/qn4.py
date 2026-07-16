class Calculator:
    def multiply(self, a, b, c=None, d=None):
        result = a * b

        if c is not None:
            result *= c

        if d is not None:
            result *= d

        return result


calc = Calculator()

print(calc.multiply(2, 3))
print(calc.multiply(2, 3, 4))
print(calc.multiply(2, 3, 4, 5))