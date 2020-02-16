class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self._insert_value(self.root, new_val)

    def _insert_value(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self._insert_value(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self._insert_value(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        self._search_helper(self.root, find_val)

    def _search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self._search_helper(current.right, find_val)
            else:
                return self._search_helper(current.left, find_val)