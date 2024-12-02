import random
class node:

    def __init__(self, key):
        self.key = key
        self.right_child = None
        self.left_child = None
        self.parent = None
        self.data = None
        self.color = "Red"

class Red_Black:
    def __init__(self):
        self.root = None
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
        return q

    def fix_insertion(self, node):
        if (node == self.root):
            node.color = "Black"
            return
        while (node.parent is not None and node.parent.color == "Red"):
            if (node.parent == node.parent.parent.left_child):
                node_uncle = node.parent.parent.right_child
                if (node_uncle and node_uncle.color == "Red"):
                    node.parent.color = "Black"
                    node_uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if (node == node.parent.right_child):
                        node = node.parent
                        self.left_rotation(node)
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self.right_rotation(node.parent.parent)

            else:
                node_uncle = node.parent.parent.left_child
                if (node_uncle and node_uncle.color == "Red"):
                    node.parent.color = "Black"
                    node_uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if (node == node.parent.left_child):
                        node = node.parent
                        self.right_rotation(node)
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self.left_rotation(node.parent.parent)
        self.root.color = "Black"

    def insert(self, key):  # вставка элемента
        new_node = node(key)  # Создаем новый узел
        if self.root is None:
            self.root = new_node
            self.root.color = "Black"
            return
        current_node = self.root
        while True:
            if key < current_node.key:
                if current_node.left_child is None:
                    current_node.left_child = new_node
                    new_node.parent = current_node  # Устанавливаем родителя
                    self.fix_insertion(new_node)
                    return
                current_node = current_node.left_child
            else:
                if current_node.right_child is None:
                    current_node.right_child = new_node
                    new_node.parent = current_node  # Устанавливаем родителя
                    self.fix_insertion(new_node)
                    return
                current_node = current_node.right_child

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

    def fix_delete(self, node):
        while node != self.root and node.color == "Black":
            if node == node.parent.left_child:  # Если узел - левый ребенок
                node_brother = node.parent.right_child
                if node_brother is not None and node_brother.color == "Red":  # Если брат красный
                    node_brother.color = "Black"
                    node.parent.color = "Red"
                    self.left_rotation(node.parent)
                    node_brother = node.parent.right_child  # Обновляем узла-брата после поворота

                # Если оба ребенка брата черные
                if (node_brother is None or
                        (node_brother.left_child is None or node_brother.left_child.color == "Black") and
                        (node_brother.right_child is None or node_brother.right_child.color == "Black")):
                    if node_brother is not None:
                        node_brother.color = "Red"
                    node = node.parent
                else:
                    if node_brother is not None and (
                            node_brother.right_child is None or node_brother.right_child.color == "Black"):
                        if node_brother.left_child is not None:
                            node_brother.left_child.color = "Black"
                        node_brother.color = "Red"
                        self.right_rotation(node_brother)
                        node_brother = node.parent.right_child  # Обновляем узла-брата после поворота

                    if node_brother is not None:
                        node_brother.color = node.parent.color
                        node.parent.color = "Black"
                        if node_brother.right_child is not None:
                            node_brother.right_child.color = "Black"
                        self.left_rotation(node.parent)
                        node = self.root
            else:  # Если узел - правый ребенок
                node_brother = node.parent.left_child
                if node_brother is not None and node_brother.color == "Red":  # Если брат красный
                    node_brother.color = "Black"
                    node.parent.color = "Red"
                    self.right_rotation(node.parent)
                    node_brother = node.parent.left_child  # Обновляем узла-брата после поворота

                # Если оба ребенка брата черные
                if (node_brother is None or
                        (node_brother.left_child is None or node_brother.left_child.color == "Black") and
                        (node_brother.right_child is None or node_brother.right_child.color == "Black")):
                    if node_brother is not None:
                        node_brother.color = "Red"
                    node = node.parent
                else:
                    if node_brother is not None and (
                            node_brother.left_child is None or node_brother.left_child.color == "Black"):
                        if node_brother.right_child is not None:
                            node_brother.right_child.color = "Black"
                        node_brother.color = "Red"
                        self.left_rotation(node_brother)
                        node_brother = node.parent.left_child  # Обновляем узла-брата после поворота

                    if node_brother is not None:
                        node_brother.color = node.parent.color
                        node.parent.color = "Black"
                        if node_brother.left_child is not None:
                            node_brother.left_child.color = "Black"
                        self.right_rotation(node.parent)
                        node = self.root
        node.color = "Black"

    def find_min_node(self, node):
        current_node = node
        while(current_node.left_child is not None):
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
            if (node.left_child is None and node.right_child is None):
                return None
            elif node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child

            # Узел с двумя детьми
            min_node = self.find_min_node(node.right_child)
            node.key = min_node.key
            node.right_child = self.delete_node(node.right_child, min_node.key)

        self.fix_delete(node)
        return node
    def height(self, node):
        if node is None:
            return -1  # Возвращаем -1 для учета высоты пустого дерева
        else:
            left_height = self.height(node.left_child)
            right_height = self.height(node.right_child)
            return 1 + max(left_height, right_height)

    def get_height(self):
        return self.height(self.root)

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


tree = Red_Black()
'''keys = []
heights = []
random.seed(21)
for n in range(10000, 100001, 10000):
    keys = random.sample(range(1, n+1), n)  # Генерация уникальных случайных ключей
    tree = Red_Black()

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



