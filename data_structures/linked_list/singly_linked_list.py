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
        current_node = self.__get_node_at(n)

        if current_node:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Node Not Found")

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_nth_node(self, n):
        if n == 1:
            current_node = self.head
            self.head = current_node.next
            current_node = None
            return

        current_node = self.head
        previous_node = None
        for i in range(1, n):
            previous_node = current_node
            current_node = current_node.next

        if current_node:
            previous_node.next = current_node.next
            current_node = None
        else:
            print("Node not found. Node can not be deleted.")

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next

    def __get_node_at(self, n):
        current_node = self.head
        for i in range(1, n):
            if current_node:
                current_node = current_node.next
        return current_node


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.prepend('X')

llist.insert_after_nth_node(1, 'D')

llist.print_list()
print("")
llist.delete_nth_node(4)
llist.print_list()
