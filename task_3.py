import heapq
import math
from collections import defaultdict

class Graph:
    def __init__(self):
        """Ініціалізація графа за допомогою словника суміжності"""
        self.graph = defaultdict(list)
    
    def add_edge(self, from_vertex, to_vertex, weight):
        """
        Додавання ребра до графа
        
        Args:
            from_vertex: Початкова вершина
            to_vertex: Кінцева вершина
            weight: Вага ребра
        """
        self.graph[from_vertex].append((to_vertex, weight))
        self.graph[to_vertex].append((from_vertex, weight))  # Для неорієнтованого графа
    
    def dijkstra(self, start_vertex):
        """
        Реалізація алгоритму Дейкстри з використанням бінарної купи
        
        Args:
            start_vertex: Початкова вершина
            
        Returns:
            Tuple[Dict[int, int], Dict[int, int]]: Кортеж з відстанями та попередніми вершинами
        """
        # Ініціалізація відстаней та попередніх вершин
        distances = {vertex: math.inf for vertex in self.graph}
        distances[start_vertex] = 0
        previous = {vertex: None for vertex in self.graph}
        
        # Створення мінімальної купи
        # Елементи купи: (відстань, вершина)
        priority_queue = [(0, start_vertex)]
        visited = set()
        
        while priority_queue:
            # Отримуємо вершину з найменшою відстанню
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Якщо вершину вже відвідали або знайшли довший шлях, пропускаємо
            if current_vertex in visited:
                continue
            
            # Додаємо поточну вершину до відвіданих
            visited.add(current_vertex)
            
            # Перевіряємо всі сусідні вершини
            for neighbor, weight in self.graph[current_vertex]:
                # Якщо вершину ще не відвідали
                if neighbor not in visited:
                    # Рахуємо нову відстань
                    distance = current_distance + weight
                    
                    # Якщо знайшли коротший шлях
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous[neighbor] = current_vertex
                        heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances, previous

    def get_path(self, previous, start_vertex, end_vertex):
        """
        Відновлення шляху від початкової до кінцевої вершини
        
        Args:
            previous: Словник попередніх вершин
            start_vertex: Початкова вершина
            end_vertex: Кінцева вершина
            
        Returns:
            List[int]: Список вершин, що складають найкоротший шлях
        """
        path = []
        current_vertex = end_vertex
        
        # Якщо шлях не існує
        if previous[end_vertex] is None and start_vertex != end_vertex:
            return path
        
        # Відновлюємо шлях від кінця до початку
        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = previous[current_vertex]
            
        # Повертаємо розвернутий шлях
        return path[::-1]

def test_dijkstra():
    """
    Функція для тестування алгоритму Дейкстри
    """
    # Створюємо граф
    g = Graph()
    
    # Додаємо ребра (створюємо тестовий граф)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)
    
    # Запускаємо алгоритм Дейкстри з початкової вершини 0
    start_vertex = 0
    distances, previous = g.dijkstra(start_vertex)
    
    # Виводимо результати
    print("Найкоротші відстані від вершини", start_vertex)
    for vertex in sorted(distances.keys()):
        path = g.get_path(previous, start_vertex, vertex)
        print(f"До вершини {vertex}:")
        print(f"  Відстань: {distances[vertex]}")
        print(f"  Шлях: {' -> '.join(map(str, path))}")
        print()

if __name__ == "__main__":
    test_dijkstra()