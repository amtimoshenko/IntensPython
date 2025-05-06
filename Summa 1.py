import math

n_max = 10
sum_value = 0.0
for i in range(3, n_max + 1):
    sum_value += (1.0 / (4 * i * i - 1))

print("Summa:", sum_value)
