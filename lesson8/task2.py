# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter
from binarytree import Node


def haffman_tree(string):
    frequency = Counter(string)
    tree = {}
    for freq in frequency.most_common():
        root = Node(freq[1])
        root.left = Node(ord(freq[0]))
        if root.value in tree:
            tree[root.value].append(root)
        else:
            tree[root.value] = [root]

    m = min(tree.keys())
    while len(tree) != 1 or m is not None:
        nodes = [0, 0]
        for i in range(len(nodes)):
            nodes[i] = tree[m].pop()
            if not tree[m]:
                tree.pop(m)
                try:
                    m = min(tree.keys())
                except ValueError:
                    m = None

        root = Node(nodes[0].value + nodes[1].value)
        root.left = nodes[0]
        root.right = nodes[1]

        if root.value in tree:
            tree[root.value].append(root)
        else:
            tree[root.value] = [root]

    return tree[min(tree.keys())][0]


def haffman_table(tree):
    haf_table = {}

    def traversal(current_node, string=''):
        if current_node.right is not None:
            traversal(current_node.left, string + '0')
            traversal(current_node.right, string + '1')
        else:
            haf_table[chr(current_node.left.value)] = string

    traversal(tree)
    return haf_table


def haffman(string):
    haf_tree = haffman_tree(string)
    haf_table = haffman_table(haf_tree)

    # Визуализация результатов
    print(f'Дерево алгоритма Хаффмана:\n{haf_tree}')
    print(f'Таблица кодировки:')
    for freq in Counter(string).most_common():
        print(f'key: {freq[0]} \t '
              f'id_key: {ord(freq[0])} \t '
              f'freq: {freq[1]} \t '
              f'haf_code: {haf_table[freq[0]]}')
    print()

    result = []
    for char in string:
        result.append(haf_table[char])

    return result


def to_bits(string):
    result = []
    for char in string:
        bits = bin(ord(char))[2:]
        bits = bits.zfill(8)
        result.append(bits)
    return result


# s = input('Введите строку, которую необходимо закодировать: ')
s = 'beep boop beer!'

print(f'Строка в битах:\n{to_bits(s)}')
print()
print(f'Закодированная по алгоритму Хаффмана строка:\n{haffman(s)}')
