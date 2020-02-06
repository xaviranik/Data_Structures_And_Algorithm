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
        current_node = self._get_node_at(n)

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

    def reverse_list_iterative(self):
        current_node = self.head
        previous_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p

        return new_head

    def length_iterative(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next

    def _get_node_at(self, n):
        current_node = self.head
        for i in range(1, n):
            if current_node:
                current_node = current_node.next
        return current_node


llist1 = LinkedList()