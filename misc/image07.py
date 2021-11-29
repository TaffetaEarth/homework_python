class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(1)
b = Node(2)
a.next = b
c = Node(5)
b.next = c
d = Node(3)
c.next = d


def sort_linked_list(head):
    begin = head
    while head.next:
        if head.data > head.next.data:
            head.data, head.next.data = head.next.data, head.data
            head = begin
        else:
            head = head.next


def print_list(head):
    while head:
        print(head.data)
        head = head.next


print_list(a)
sort_linked_list(a)
print_list(a)