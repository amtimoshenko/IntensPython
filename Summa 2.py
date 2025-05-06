import math

n_max = 10
sum_value = 0.0
for i in range(1, n_max + 1):
    sum_value += (1.0 / ( i * i - 4))

print("Summa:", sum_value)
