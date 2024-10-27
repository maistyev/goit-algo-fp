import uuid
import networkx as nx
import matplotlib.pyplot as plt
import random
import colorsys
import time
from collections import deque

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
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
    
    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._sift_up(parent)
    
    def heap_to_tree(self):
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

def generate_color(step, total_steps):
    """Генерує колір в форматі RGB"""
    hue = step / total_steps
    saturation = 0.7
    value = 0.9
    rgb = colorsys.hsv_to_rgb(hue, saturation, value)
    return '#{:02x}{:02x}{:02x}'.format(
        int(rgb[0] * 255),
        int(rgb[1] * 255),
        int(rgb[2] * 255)
    )

def add_edges(graph, node, pos, x=0, y=0, layer=1):
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

def draw_traversal_step(root, node_colors, title):
    """Візуалізує один крок обходу"""
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)
    
    colors = []
    labels = {}
    
    for node in tree.nodes(data=True):
        node_id = node[0]
        if node_id in node_colors:
            colors.append(node_colors[node_id])
        else:
            colors.append('skyblue')
        labels[node_id] = node[1]['label']
    
    plt.clf()
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, 
            node_size=2500, node_color=colors)
    plt.pause(0.5)

def dfs_traversal(heap):
    """Обхід у глибину для бінарної купи"""
    root = heap.heap_to_tree()
    if not root:
        return
    
    stack = [(root, 0)]  # (вузол, крок)
    visited = set()
    node_colors = {}
    total_nodes = len(heap.heap)
    
    plt.figure(figsize=(10, 6))
    step = 0
    
    while stack:
        current, step = stack.pop()
        if current.id not in visited:
            visited.add(current.id)
            node_colors[current.id] = generate_color(step, total_nodes)
            
            if current.right:
                stack.append((current.right, step + 1))
            if current.left:
                stack.append((current.left, step + 1))
            
            draw_traversal_step(root, node_colors, "Обхід у глибину (DFS)")
            
    plt.close()

def bfs_traversal(heap):
    """Обхід в ширину для бінарної купи"""
    root = heap.heap_to_tree()
    if not root:
        return
    
    queue = deque([(root, 0)])  # (вузол, крок)
    visited = set()
    node_colors = {}
    total_nodes = len(heap.heap)
    
    plt.figure(figsize=(10, 6))
    step = 0
    
    while queue:
        current, step = queue.popleft()
        if current.id not in visited:
            visited.add(current.id)
            node_colors[current.id] = generate_color(step, total_nodes)
            
            if current.left:
                queue.append((current.left, step + 1))
            if current.right:
                queue.append((current.right, step + 1))
            
            draw_traversal_step(root, node_colors, "Обхід в ширину (BFS)")
            
    plt.close()

def test_heap_traversals():
    """Тестування візуалізації обходів бінарної купи"""
    # Створюємо бінарну купу
    heap = BinaryHeap()
    
    # Додаємо випадкові елементи
    test_data = [random.randint(1, 100) for _ in range(15)]
    for num in test_data:
        heap.insert(num)
    
    print("Масив купи:", heap.heap)
    
    print("\nПочинаємо обхід у глибину (DFS)...")
    dfs_traversal(heap)
    time.sleep(1)
    
    print("Починаємо обхід в ширину (BFS)...")
    bfs_traversal(heap)

if __name__ == "__main__":
    test_heap_traversals()