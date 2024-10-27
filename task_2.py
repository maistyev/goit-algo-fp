import turtle

def setup_turtle():
    """Налаштування параметрів вікна та черепашки"""
    screen = turtle.Screen()
    screen.title("Фрактальне дерево")
    screen.setup(800, 800)  # Збільшено розмір вікна для кращої видимості
    
    ttl = turtle.Turtle()
    ttl.speed(0)  # Максимальна швидкість
    ttl.color("brown")
    ttl.pensize(1)
    
    # Встановлення початкової позиції
    ttl.penup()
    ttl.setposition(0, -200)  # Зміщено нижче для кращої видимості всього дерева
    ttl.pendown()
    ttl.hideturtle()
    ttl.setheading(90)
    
    return ttl, screen

def tree_fractal(ttl, recursion_level, branch_length, branch_reduction, angle):
    """
    Рекурсивна функція для малювання фрактального дерева
    
    Параметри:
    ttl: об'єкт черепашки
    recursion_level: рівень рекурсії
    branch_length: довжина гілки
    branch_reduction: зменшення довжини гілки на кожному рівні
    angle: кут повороту гілок
    """
    if recursion_level == 0:
        ttl.forward(0)
    else:
        # Зменшуємо довжину гілки
        branch_length = branch_length - branch_reduction
        
        # Малюємо основну гілку
        ttl.forward(branch_length)
        
        # Ліва гілка
        ttl.left(angle)
        tree_fractal(ttl, recursion_level-1, branch_length, branch_reduction, angle)
        
        # Права гілка
        ttl.right(angle * 2)
        tree_fractal(ttl, recursion_level-1, branch_length, branch_reduction, angle)
        
        # Повертаємось назад
        ttl.left(angle)
        ttl.backward(branch_length)

def main():
    """Основна функція програми"""
    # Отримуємо параметри від користувача
    try:
        recursion_level = int(input("Введіть рівень рекурсії (рекомендовано 5-12): "))
        if recursion_level < 1:
            raise ValueError("Рівень рекурсії повинен бути більше 0")
            
        # Додаткові параметри (опціонально)
        branch_length = float(input("Введіть початкову довжину гілки (рекомендовано 50-100): "))
        branch_reduction = float(input("Введіть зменшення довжини гілки (рекомендовано 5-10): "))
        angle = float(input("Введіть кут нахилу гілок (рекомендовано 15-30): "))
        
    except ValueError as e:
        print(f"Помилка: {e}")
        print("Будуть використані значення за замовчуванням")
        recursion_level = 9
        branch_length = 80
        branch_reduction = 5
        angle = 25

    # Налаштовуємо середовище малювання
    ttl, screen = setup_turtle()
    
    # Малюємо дерево
    tree_fractal(ttl, recursion_level, branch_length, branch_reduction, angle)
    
    # Чекаємо закриття вікна
    screen.exitonclick()

if __name__ == "__main__":
    main()