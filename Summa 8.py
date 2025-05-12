import math

def calculate_sum(x, max_iterations):
    total_sum = 0.0
    for n in range(1, max_iterations + 1):
        total_sum += (math.pow(x + 2, 2 * n)) / (n * math.pow(4, n))
    return total_sum

x = float(input("Vvedite x: "))
max_iterations = int(input("Vvedite maxIterations: "))

result = calculate_sum(x, max_iterations)
print("Summa:", result)

