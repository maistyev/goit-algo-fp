class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Функція 1: Реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_temp = current.next  # Зберігаємо наступний вузол
            current.next = prev       # Змінюємо посилання на попередній
            prev = current            # Оновлюємо prev
            current = next_temp       # Переходимо до наступного вузла
        
        self.head = prev

    # Функція 2: Сортування вставками
    def insertion_sort(self):
        # Якщо список порожній або має один елемент
        if not self.head or not self.head.next:
            return

        sorted_list = None
        current = self.head

        while current:
            next_temp = current.next  # Зберігаємо наступний вузол
            
            # Вставка current у відсортований список
            if not sorted_list or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                search = sorted_list
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current
            
            current = next_temp

        self.head = sorted_list

    # Функція 3: Об'єднання двох відсортованих списків
    def merge_sorted_lists(self, other_list):
        # Створюємо фіктивний вузол для спрощення операції
        dummy = Node()
        tail = dummy
        
        list1 = self.head
        list2 = other_list.head
        
        # Порівнюємо елементи обох списків
        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Додаємо залишки першого списку
        if list1:
            tail.next = list1
        # Додаємо залишки другого списку
        if list2:
            tail.next = list2
            
        self.head = dummy.next

# Тестування функцій
def test_linked_list_operations():
    # Створюємо та заповнюємо перший список
    list1 = LinkedList()
    list1.insert_at_end(3)
    list1.insert_at_end(1)
    list1.insert_at_end(4)
    
    print("Оригінальний список 1:")
    list1.print_list()
    
    # Тестуємо реверсування
    list1.reverse()
    print("\nРеверсований список 1:")
    list1.print_list()
    
    # Тестуємо сортування
    list1.insertion_sort()
    print("\nВідсортований список 1:")
    list1.print_list()
    
    # Створюємо та заповнюємо другий список
    list2 = LinkedList()
    list2.insert_at_end(2)
    list2.insert_at_end(5)
    list2.insert_at_end(6)
    
    print("\nСписок 2:")
    list2.print_list()
    
    # Тестуємо об'єднання відсортованих списків
    list1.merge_sorted_lists(list2)
    print("\nОб'єднаний відсортований список:")
    list1.print_list()

if __name__ == "__main__":
    test_linked_list_operations()