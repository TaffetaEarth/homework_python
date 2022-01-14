class BST_Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder_print(head):
    if head:
        inorder_print(head.left)
        print(head.data)
        inorder_print(head.right)


def insert_bst(head, node):
    if not head:
        return node
    elif head.data > node.data:
        head.left = insert_bst(head.left, node)
    elif head.data < node.data:
        head.right = insert_bst(head.right, node)
    return head


a = BST_Node(5)
for i in range(10):
    insert_bst(a, BST_Node(i))
b = BST_Node(7)
insert_bst(a, b)


def min_bst(head):
    if head.left:
        return min_bst(head.left)
    else:
        return head


def max_bst(head):
    if head.right:
        return min_bst(head.right)
    else:
        return head


def next_bst(node):
    if not node or not node.right:
        return None
    else:
        return min_bst(node.right)


def delete_bst(node):
    new_node = min_bst(node)
    node.data = new_node.data
    print(node)
    print(node.right)
    print(node.left)
    if node.right:
        node = node.rigth
        print("right")
    while node.left:
        print("A" + str(node.left))
        node = node.left
    node.left = None


inorder_print(a)
delete_bst(b)
inorder_print(a)
