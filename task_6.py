import time

def greedy_algorithm(items, budget):
    # Розрахунок співвідношення калорій до вартості для кожної страви
    food_ratio = {
        name: item["calories"] / item["cost"]
        for name, item in items.items()
    }
    
    # Сортування страв за співвідношенням калорій до вартості
    sorted_food = sorted(
        food_ratio.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    # Вибір страв
    for food_name, _ in sorted_food:
        food_cost = items[food_name]["cost"]
        if total_cost + food_cost <= budget:
            selected_items.append(food_name)
            total_cost += food_cost
            total_calories += items[food_name]["calories"]
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    # Створення списків для зручності індексації
    food_names = list(items.keys())
    n = len(food_names)
    
    # Створення таблиці динамічного програмування
    # dp[i][j] - максимальна калорійність для перших i страв з бюджетом j
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнення таблиці
    for i in range(1, n + 1):
        food_name = food_names[i-1]
        food_cost = items[food_name]["cost"]
        food_calories = items[food_name]["calories"]
        
        for j in range(budget + 1):
            if food_cost <= j:
                dp[i][j] = max(
                    dp[i-1][j],  # Не беремо поточну страву
                    dp[i-1][j-food_cost] + food_calories  # Беремо поточну страву
                )
            else:
                dp[i][j] = dp[i-1][j]
    
    # Відновлення розв'язку
    selected_items = []
    total_cost = 0
    current_budget = budget
    
    for i in range(n, 0, -1):
        food_name = food_names[i-1]
        food_cost = items[food_name]["cost"]
        
        if dp[i][current_budget] != dp[i-1][current_budget]:
            selected_items.append(food_name)
            total_cost += food_cost
            current_budget -= food_cost
    
    selected_items.reverse()
    total_calories = dp[n][budget]
    
    return selected_items, total_cost, total_calories

def compare_algorithms(items, budget):
    print(f"Бюджет: {budget} грн\n")
    
    # Жадібний алгоритм
    start_time = time.time()
    greedy_items, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
    greedy_time = time.time() - start_time
    
    print("Жадібний алгоритм:")
    print(f"Вибрані страви: {', '.join(greedy_items)}")
    print(f"Загальна вартість: {greedy_cost} грн")
    print(f"Загальна калорійність: {greedy_calories} калорій")
    print(f"Час виконання: {greedy_time:.6f} секунд")
    print()
    
    # Динамічне програмування
    start_time = time.time()
    dp_items, dp_cost, dp_calories = dynamic_programming(items, budget)
    dp_time = time.time() - start_time
    
    print("Динамічне програмування:")
    print(f"Вибрані страви: {', '.join(dp_items)}")
    print(f"Загальна вартість: {dp_cost} грн")
    print(f"Загальна калорійність: {dp_calories} калорій")
    print(f"Час виконання: {dp_time:.6f} секунд")
    
    # Порівняння результатів
    calories_diff = dp_calories - greedy_calories
    if calories_diff > 0:
        print(f"\nДинамічне програмування знайшло рішення краще на {calories_diff} калорій")
    elif calories_diff < 0:
        print(f"\nЖадібний алгоритм знайшов рішення краще на {-calories_diff} калорій")
    else:
        print("\nОбидва алгоритми знайшли однаково оптимальне рішення")

def main():
    # Тестові дані
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    # Тестування з різними бюджетами
    budgets = [50, 100, 150]
    
    for budget in budgets:
        compare_algorithms(items, budget)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()