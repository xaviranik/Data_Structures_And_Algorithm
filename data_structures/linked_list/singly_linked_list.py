class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_nth_node(self, n, data):
        current_node = self.head

        for i in range(1, n):
            if current_node:
                current_node = current_node.next
            else:
                print("Node not found.")
                return

        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.prepend('X')

llist.insert_after_nth_node(3, 'D')

llist.print_list()
