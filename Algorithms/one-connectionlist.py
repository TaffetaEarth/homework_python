class Node_double:
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


a = Node_double(1)


b = Node_double(2)
c = Node_double(3)
a.next = b
b.previous = a
b.next = c
c.previous = b


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_linked(head):
    while head:
        print(head)
        print(head.data)
        head = head.next


def insert(to_replace, data):
    if to_replace is None:
        print("Nothing to replace")
        return
    new_node = Node(data)
    new_node.next = to_replace.next
    to_replace.next = new_node
    return new_node


def sort_linked(head):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        current = head
        while current is not None:
            if current.next is not None and current.data > current.next.data:
                current.next.data, current.data = current.data, current.next.data
                is_sorted = False
            current = current.next
        return head


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def get(self):
        return self.stack.pop()


class Queue:
    def __init__(self):
        self.queue = []

    def get(self):
        return self.queue.pop()

    def push(self, data):
        self.queue.insert(0, data)


class Deque:
    def __init__(self):
        self.deque = []

    def push(self, data, end=False):
        if end:
            self.deque.append(data)
        else:
            self.deque.insert(0, data)

    def get(self, end):
        if end:
            return self.deque.pop()
        else:
            return self.deque.pop(0)


# st = Stack()
# for i in range(10):
#     st.push(i)
# print(st.stack)
# print(st.get())
# print(st.stack)
