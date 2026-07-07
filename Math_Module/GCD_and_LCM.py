import math

num1 = 12
num2 = 18
print(f"Numbers: {num1} and {num2}\n")
# 1. math.gcd(*integers)
# Finds the largest number that divides both numbers perfectly.
gcd_result = math.gcd(num1, num2)
print(f"math.gcd({num1}, {num2}) -> {gcd_result}")

# 2. math.lcm(*integers)
# Finds the smallest non-zero number that is a multiple of both numbers.
lcm_result = math.lcm(num1, num2)
print(f"math.lcm({num1}, {num2}) -> {lcm_result}")

