import math

n_max = 10
sum_value = 0.0
for i in range(1, n_max + 1):
    sum_value += (1.0 / (49 * i * i +7*i-12))

print("Summa:", sum_value)
