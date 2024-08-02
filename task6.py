def greedy_algorithm(items, budget):
    # Розрахунок співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return selected_items, total_calories, total_cost

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
selected_items, total_calories, total_cost = greedy_algorithm(items, budget)
print(f"Selected items (greedy): {selected_items}, Total calories: {total_calories}, Total cost: {total_cost}")

def dynamic_programming(items, budget):
    # Ініціалізація таблиці DP
    n = len(items)
    item_list = list(items.items())
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнення таблиці DP
    for i in range(1, n + 1):
        item, info = item_list[i - 1]
        cost = info['cost']
        calories = info['calories']
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення вибраних елементів
    total_calories = dp[n][budget]
    total_cost = 0
    selected_items = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, info = item_list[i - 1]
            selected_items.append(item)
            total_cost += info['cost']
            w -= info['cost']

    selected_items.reverse()
    return selected_items, total_calories, total_cost

# Приклад використання
budget = 100
selected_items, total_calories, total_cost = dynamic_programming(items, budget)
print(f"Selected items (dynamic programming): {selected_items}, Total calories: {total_calories}, Total cost: {total_cost}")
