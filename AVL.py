import random
class node:
    def __init__(self, key):
        self.key = key
        self.right_child = None
        self.left_child = None
        self.parent = None
        self.height = 1
        self.data = None


class AVL:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def balance_factor(self, node):
        return self.height(node.right_child) - self.height(node.left_child)

    def fix_height(self, node):
        node.height = 1 + max(self.height(node.left_child), self.height(node.right_child))

    def left_rotation(self, p):
        q = p.right_child
        p.right_child = q.left_child
        if q.left_child is not None:
            q.left_child.parent = p
        q.parent = p.parent
        if p.parent is None:  # p был корнем
            self.root = q
        elif p == p.parent.left_child:
            p.parent.left_child = q
        else:
            p.parent.right_child = q
        q.left_child = p
        p.parent = q

        # Обновляем высоты
        self.fix_height(p)
        self.fix_height(q)
        return q

    def right_rotation(self, p):
        q = p.left_child
        p.left_child = q.right_child
        if q.right_child is not None:
            q.right_child.parent = p
        q.parent = p.parent
        if p.parent is None:  # p был корнем
            self.root = q
        elif p == p.parent.right_child:
            p.parent.right_child = q
        else:
            p.parent.left_child = q
        q.right_child = p
        p.parent = q

        # Обновляем высоты
        self.fix_height(p)
        self.fix_height(q)
        return q

    def balance(self, node):
        self.fix_height(node)
        if self.balance_factor(node) == 2:  # Правосторонний
            if self.balance_factor(node.right_child) < 0:
                node.right_child = self.right_rotation(node.right_child)
            return self.left_rotation(node)
        elif self.balance_factor(node) == -2:  # Левосторонний
            if self.balance_factor(node.left_child) > 0:
                node.left_child = self.left_rotation(node.left_child)
            return self.right_rotation(node)
        return node

    def insert(self, key):  # вставка элемента
        new_node = node(key)  # Создаем новый узел
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if key < current_node.key:
                if current_node.left_child is None:
                    current_node.left_child = new_node
                    new_node.parent = current_node  # Устанавливаем родителя

                    break
                current_node = current_node.left_child
            else:
                if current_node.right_child is None:
                    current_node.right_child = new_node
                    new_node.parent = current_node  # Устанавливаем родителя
                    break
                current_node = current_node.right_child
        # Балансируем дерево
        node_to_balance = new_node.parent
        while node_to_balance is not None:
            if(self.balance_factor(node_to_balance) != 0):
                node_to_balance = self.balance(node_to_balance)
                node_to_balance = node_to_balance.parent
            else:
                break


    def search(self, key):
        current_node = self.root
        while current_node is not None:
            if key == current_node.key:
                return "Ключ найден"
            elif key < current_node.key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return "Ключ не найден"

    def find_min_node(self, node):
        current_node = node
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node

    def delete_node(self, node, key):
        if node is None:
            return node  # Узел не найден

        if key < node.key:
            node.left_child = self.delete_node(node.left_child, key)
        elif key > node.key:
            node.right_child = self.delete_node(node.right_child, key)
        else:  # Узел с ключом найден
            if node.left_child is None and node.right_child is None:
                return None
            elif node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child

            # Узел с двумя детьми
            min_node = self.find_min_node(node.right_child)
            node.key = min_node.key
            node.right_child = self.delete_node(node.right_child, min_node.key)

        # Балансируем узел после удаления
        return self.balance(node)
    def heightA(self, node):
        if node is None:
            return -1  # Возвращаем -1 для учета высоты пустого дерева
        else:
            left_height = self.heightA(node.left_child)
            right_height = self.heightA(node.right_child)
            return 1 + max(left_height, right_height)

    def get_height(self):
        return self.heightA(self.root)



def pre_order(node):
    keys =[]
    if node is None:
        return keys
    else:
        keys.append(node.key)
        keys += pre_order(node.left_child)
        keys += pre_order(node.right_child)
    return keys

def post_order(node):
    keys = []
    if node is None:
        return keys
    else:
        keys += pre_order(node.left_child)
        keys += pre_order(node.right_child)
        keys.append(node.key)
    return keys

def in_order(node):
    keys = []
    if node is None:
        return keys
    else:
        keys += pre_order(node.left_child)
        keys.append(node.key)
        keys += pre_order(node.right_child)
    return keys


def bfs(root):
    keys = []
    if root is None:  # Проверка на пустое дерево
        return

    current_level = [root]  # Начинаем с корня дерева

    while current_level:  # Пока есть узлы на текущем уровне
        next_level = []  # Список для хранения узлов следующего уровня

        for node in current_level:  # Проходим по узлам текущего уровня
            keys.append(node.key)  # Посещаем узел

            if node.left_child:  # Если есть левый ребенок, добавляем его в следующий уровень
                next_level.append(node.left_child)
            if node.right_child:  # Если есть правый ребенок, добавляем его в следующий уровень
                next_level.append(node.right_child)

        current_level = next_level  # Переходим к следующему уровню
    return keys


tree = AVL()
'''keys = []
heights = []
random.seed(21)
for n in range(10000, 100001, 10000):
    keys = random.sample(range(1, n+1), n)  # Генерация уникальных случайных ключей
    tree = AVL()

    for key in keys:
        tree.insert(key)  # Вставка ключей в дерево

    height = tree.get_height()  # Получение высоты дерева
    heights.append(height)  # Сохранение высоты в список


print(heights)'''

'''while n != 0:
    n = int(input("Введите число (0 для выхода): "))
    if n != 0:
        tree.insert(n)'''


for i in range (1,11):
    tree.insert(i)

print("Прямой обход в ширину:")
print(pre_order(tree.root))
print("Обратный обход в ширину:")
print(post_order(tree.root))
print("Центрированный обход в ширину:")
print(in_order(tree.root))
print("Обход в глубину:")
print(bfs(tree.root))









