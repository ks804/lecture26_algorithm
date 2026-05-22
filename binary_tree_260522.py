def preorder(node):
    if node is not None:
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node is not None:
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])


def postorder(node):
    if node is not None:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')


def make_tree(tree):
    turn = int(input())
    
    for _ in range(turn):
        data = input().split()
        node = data[0]
        left = data[1] if data[1] != '.' else None
        right = data[2] if data[2] != '.' else None
        tree[node] = [left, right]

tree = {}

tree['A'] = ['B', 'C']
tree['B'] = ['D', None]
tree['C'] = ['E', 'F']
tree['E'] = [None, None]
tree['F'] = [None, 'G']
tree['D'] = [None, None]
tree['G'] = [None, None]

print("전위 순회한 결과 : ", end='')
preorder('A')
print()

print("중위 순회한 결과 : ", end='')
inorder('A')
print()

print("후위 순회한 결과 : ", end='')
postorder('A')
print()
