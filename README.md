# Аналіз результатів симуляції кидків кубиків методом Монте-Карло

## Огляд експерименту

В рамках дослідження було проведено комп'ютерну симуляцію кидків двох гральних кубиків з метою визначення ймовірностей випадання різних сум та порівняння отриманих результатів з теоретичними розрахунками.

### Параметри експерименту:
- Кількість кидків: 1,000,000
- Діапазон можливих сум: від 2 до 12
- Метод: Монте-Карло

## Результати симуляції

### Детальне порівняння ймовірностей:

| Сума | Експериментальна ймовірність (%) | Теоретична ймовірність (%) | Різниця (%) |
|------|----------------------------------|---------------------------|-------------|
| 2    | 2.79                             | 2.78                      | +0.01       |
| 3    | 5.57                             | 5.56                      | +0.01       |
| 4    | 8.35                             | 8.33                      | +0.02       |
| 5    | 11.10                            | 11.11                     | -0.01       |
| 6    | 13.97                            | 13.89                     | +0.08       |
| 7    | 16.62                            | 16.67                     | -0.05       |
| 8    | 13.87                            | 13.89                     | -0.02       |
| 9    | 11.13                            | 11.11                     | +0.02       |
| 10   | 8.30                             | 8.33                      | -0.03       |
| 11   | 5.53                             | 5.56                      | -0.03       |
| 12   | 2.77                             | 2.78                      | -0.01       |

### Основні спостереження:

1. **Точність результатів:**
   - Середня абсолютна похибка: 0.0264%
   - Максимальне відхилення: 0.08% (для суми 6)
   - Мінімальне відхилення: 0.01% (для сум 2, 3, 5, 12)

2. **Розподіл відхилень:**
   - Позитивні відхилення: суми 2, 3, 4, 6, 9 
   - Негативні відхилення: суми 5, 7, 8, 10, 11, 12
   - Найбільше відхилення спостерігається для суми 6 (+0.08%)

3. **Розподіл ймовірностей:**
   - Максимальна ймовірність для суми 7: 16.62% (експериментальна) vs 16.67% (теоретична)
   - Мінімальна ймовірність для суми 12: 2.77% (експериментальна) vs 2.78% (теоретична)
   - Чітко спостерігається симетричність розподілу

## Висновки

1. **Точність методу Монте-Карло:**
   - Метод показав надзвичайно високу точність з середньою абсолютною похибкою лише 0.0264%
   - Максимальне відхилення не перевищує 0.1%, що свідчить про надійність методу
   - Симетричність розподілу зберігається в експериментальних даних

2. **Відповідність теоретичним розрахункам:**
   - Експериментальні результати майже ідеально співпадають з теоретичними
   - Відхилення мають випадковий характер та не показують систематичної помилки
   - Форма розподілу повністю відповідає теоретичним очікуванням

3. **Практичні результати:**
   - Метод Монте-Карло підтвердив теоретичні розрахунки з високою точністю
   - Кількість симуляцій (1,000,000) виявилася достатньою для отримання надійних результатів
   - Візуалізація результатів чітко демонструє закономірності розподілу

## Графічна інтерпретація

1. **Порівняльна діаграма:**
   - Показує практично повне співпадіння експериментальних та теоретичних значень
   - Демонструє чітку симетрію розподілу відносно суми 7

2. **Діаграма відхилень:**
   - Візуалізує різницю між експериментальними та теоретичними значеннями
   - Показує, що всі відхилення знаходяться в межах ±0.08%
   - Не виявляє систематичного зміщення результатів

## Рекомендації

1. **Для практичного використання:**
   - Використана кількість симуляцій (1,000,000) є оптимальною для отримання точних результатів
   - При меншій кількості симуляцій можна очікувати більших відхилень
   - Метод можна використовувати для перевірки теоретичних розрахунків ймовірностей

2. **Для подальших досліджень:**
   - Дослідити вплив різної кількості симуляцій на точність результатів
   - Розширити дослідження на більшу кількість кубиків
   - Провести аналіз часової ефективності методу