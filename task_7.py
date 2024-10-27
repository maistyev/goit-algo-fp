import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import defaultdict

class DiceSimulation:
    def __init__(self):
        # Теоретичні ймовірності для кожної суми
        self.theoretical_probabilities = {
            2: 2.78,  # 1/36
            3: 5.56,  # 2/36
            4: 8.33,  # 3/36
            5: 11.11, # 4/36
            6: 13.89, # 5/36
            7: 16.67, # 6/36
            8: 13.89, # 5/36
            9: 11.11, # 4/36
            10: 8.33, # 3/36
            11: 5.56, # 2/36
            12: 2.78  # 1/36
        }
    
    def roll_dice(self, num_simulations):
        """
        Симулює кидки двох кубиків
        
        Args:
            num_simulations: Кількість симуляцій
            
        Returns:
            dict: Словник з кількістю випадань кожної суми
        """
        results = defaultdict(int)
        
        for _ in range(num_simulations):
            # Кидаємо два кубики
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total = dice1 + dice2
            results[total] += 1
            
        return results
    
    def calculate_probabilities(self, results, num_simulations):
        """
        Розраховує ймовірності для кожної суми
        
        Args:
            results: Словник з результатами симуляцій
            num_simulations: Кількість симуляцій
            
        Returns:
            dict: Словник з ймовірностями
        """
        probabilities = {}
        for total in range(2, 13):
            probability = (results[total] / num_simulations) * 100
            probabilities[total] = round(probability, 2)
        return probabilities
    
    def plot_results(self, experimental_probabilities):
        """
        Створює графік порівняння експериментальних та теоретичних ймовірностей
        
        Args:
            experimental_probabilities: Словник з експериментальними ймовірностями
        """
        sums = list(range(2, 13))
        
        exp_probs = [experimental_probabilities[s] for s in sums]
        theo_probs = [self.theoretical_probabilities[s] for s in sums]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Графік порівняння
        x = np.arange(len(sums))
        width = 0.35
        
        ax1.bar(x - width/2, exp_probs, width, label='Експериментальні')
        ax1.bar(x + width/2, theo_probs, width, label='Теоретичні')
        
        ax1.set_ylabel('Ймовірність (%)')
        ax1.set_title('Порівняння експериментальних та теоретичних ймовірностей')
        ax1.set_xticks(x)
        ax1.set_xticklabels(sums)
        ax1.legend()
        
        # Графік різниці
        differences = [exp - theo for exp, theo in zip(exp_probs, theo_probs)]
        ax2.bar(sums, differences)
        ax2.axhline(y=0, color='r', linestyle='-', alpha=0.3)
        ax2.set_xlabel('Сума')
        ax2.set_ylabel('Різниця (%)')
        ax2.set_title('Різниця між експериментальними та теоретичними ймовірностями')
        
        plt.tight_layout()
        plt.show()
    
    def create_comparison_table(self, experimental_probabilities):
        """
        Створює таблицю порівняння результатів
        
        Args:
            experimental_probabilities: Словник з експериментальними ймовірностями
            
        Returns:
            pd.DataFrame: Таблиця порівняння
        """
        data = {
            'Сума': list(range(2, 13)),
            'Експериментальна ймовірність (%)': [experimental_probabilities[s] for s in range(2, 13)],
            'Теоретична ймовірність (%)': [self.theoretical_probabilities[s] for s in range(2, 13)],
        }
        
        df = pd.DataFrame(data)
        df['Різниця'] = df['Експериментальна ймовірність (%)'] - df['Теоретична ймовірність (%)']
        return df
    
    def run_simulation(self, num_simulations=1000000):
        """
        Запускає повну симуляцію та виводить результати
        
        Args:
            num_simulations: Кількість симуляцій
        """
        print(f"Запуск симуляції з {num_simulations:,} кидків...")
        
        # Виконуємо симуляцію
        results = self.roll_dice(num_simulations)
        experimental_probabilities = self.calculate_probabilities(results, num_simulations)
        
        # Створюємо таблицю порівняння
        comparison_table = self.create_comparison_table(experimental_probabilities)
        print("\nРезультати симуляції:")
        print(comparison_table.to_string(index=False))
        
        # Візуалізуємо результати
        self.plot_results(experimental_probabilities)
        
        # Обчислюємо середню абсолютну похибку
        mae = np.mean(abs(comparison_table['Різниця']))
        print(f"\nСередня абсолютна похибка: {mae:.4f}%")

if __name__ == "__main__":
    # Створюємо об'єкт симуляції
    simulation = DiceSimulation()
    
    # Запускаємо симуляцію з мільйоном кидків
    simulation.run_simulation(1000000)