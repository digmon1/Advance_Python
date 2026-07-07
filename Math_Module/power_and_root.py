import math
import time

base = 5
exponent = 3
perfect_square = 16
non_perfect_square = 20

print("--- 1. Power Operations (5 raised to the power of 3) ---")
pow_float = math.pow(base, exponent)
print(f"math.pow({base}, {exponent}): {pow_float}")

pow_builtin = pow(base, exponent)
print(f"pow({base}, {exponent}): {pow_builtin}")

pow_operator = base ** exponent
print(f"** operator ({base}**{exponent}): {pow_operator}")

print("\n--- 2. Square Root Operations ---")

sqrt_perfect = math.sqrt(perfect_square)
sqrt_non_perfect = math.sqrt(non_perfect_square)
print(f"math.sqrt({perfect_square}): {sqrt_perfect}")
print(f"math.sqrt({non_perfect_square}): {sqrt_non_perfect}")

isqrt_perfect = math.isqrt(perfect_square)
isqrt_non_perfect = math.isqrt(non_perfect_square)
print(f"math.isqrt ({perfect_square}): {isqrt_perfect}")
print(f"math.isqrt({non_perfect_square}): {isqrt_non_perfect}")
