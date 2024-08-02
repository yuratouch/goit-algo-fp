import random
import matplotlib.pyplot as plt

# Кількість ітерацій симуляції
num_simulations = 1_000_000

# Словник для підрахунку випадінь кожної суми
sums_count = {i: 0 for i in range(2, 13)}

# Симуляція кидків кубиків
for _ in range(num_simulations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    sums_count[dice_sum] += 1

# Розрахунок ймовірностей для кожної суми
sums_probabilities = {k: v / num_simulations * 100 for k, v in sums_count.items()}

# Аналітичні ймовірності
analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Виведення результатів
print("Результати симуляції (Метод Монте-Карло):")
for sum_, probability in sums_probabilities.items():
    print(f"Сума: {sum_}, Ймовірність: {probability:.2f}%")

print("\nАналітичні ймовірності:")
for sum_, probability in analytical_probabilities.items():
    print(f"Сума: {sum_}, Ймовірність: {probability:.2f}%")

# Побудова графіка
sums = list(sums_probabilities.keys())
monte_carlo_probs = list(sums_probabilities.values())
analytical_probs = [analytical_probabilities[sum_] for sum_ in sums]

plt.figure(figsize=(10, 5))
plt.plot(sums, monte_carlo_probs, marker='o', label='Метод Монте-Карло')
plt.plot(sums, analytical_probs, marker='x', label='Аналітичні ймовірності')
plt.xlabel('Сума')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірності сум при киданні двох кубиків')
plt.legend()
plt.grid(True)
plt.savefig('probability_comparison.png')
plt.show()
