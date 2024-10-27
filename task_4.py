import uuid
import networkx as nx
import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

class BinaryHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        """Повертає індекс батьківського елемента"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Повертає індекс лівого нащадка"""
        return 2 * i + 1
    
    def right_child(self, i):
        """Повертає індекс правого нащадка"""
        return 2 * i + 2
    
    def insert(self, key):
        """Додає новий елемент до купи"""
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
    
    def _sift_up(self, i):
        """Просіює елемент вгору для підтримки властивостей купи"""
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._sift_up(parent)
    
    def heap_to_tree(self):
        """Конвертує масив купи в деревоподібну структуру"""
        if not self.heap:
            return None
            
        def create_node(i):
            if i >= len(self.heap):
                return None
            
            node = Node(self.heap[i])
            left_idx = self.left_child(i)
            right_idx = self.right_child(i)
            
            if left_idx < len(self.heap):
                node.left = create_node(left_idx)
            if right_idx < len(self.heap):
                node.right = create_node(right_idx)
                
            return node
            
        return create_node(0)

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Додає ребра до графу для візуалізації"""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap):
    """Візуалізує бінарну купу"""
    # Конвертуємо купу в дерево
    tree_root = heap.heap_to_tree()
    
    if tree_root is None:
        print("Купа порожня")
        return
        
    # Створюємо граф
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    # Отримуємо кольори та мітки вузлів
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    # Відображаємо дерево
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, 
            node_size=2500, node_color=colors)
    plt.title("Візуалізація бінарної купи")
    plt.show()

def test_heap_visualization():
    """Тестування візуалізації бінарної купи"""
    # Створюємо бінарну купу
    heap = BinaryHeap()
    
    # Додаємо елементи
    test_data = [random.randint(1, 100) for _ in range(15)]
    for num in test_data:
        heap.insert(num)
    
    print("Масив купи:", heap.heap)
    print("\nВізуалізація купи як дерева:")
    draw_heap(heap)

if __name__ == "__main__":
    test_heap_visualization()