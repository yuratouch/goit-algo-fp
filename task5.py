import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#FFFFFF"
        self.id = str(uuid.uuid4())

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

def draw_tree(tree_root, visited=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    colors = [node[1].get('color', '#FFFFFF') for node in tree.nodes(data=True)]

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_colors(num_colors):
    return [mcolors.rgb2hex(c) for c in plt.cm.viridis(np.linspace(0, 1, num_colors))]

def bfs(root):
    queue = deque([root])
    visited = []
    color_map = generate_colors(len(list_all_nodes(root)))
    color_index = 0

    while queue:
        node = queue.popleft()
        visited.append(node)
        node.color = color_map[color_index]
        color_index += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited

def dfs(root):
    stack = [root]
    visited = []
    color_map = generate_colors(len(list_all_nodes(root)))
    color_index = 0

    while stack:
        node = stack.pop()
        visited.append(node)
        node.color = color_map[color_index]
        color_index += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited

def list_all_nodes(root):
    if root is None:
        return []
    nodes = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        nodes.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return nodes

def create_sample_tree():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    return root

# Створення дерева
root = create_sample_tree()

# Виконання обходу в ширину
visited_bfs = bfs(root)
draw_tree(root, visited_bfs)

# Виконання обходу в глибину
root = create_sample_tree()  # Перестворюємо дерево, щоб відновити початкові кольори
visited_dfs = dfs(root)
draw_tree(root, visited_dfs)
