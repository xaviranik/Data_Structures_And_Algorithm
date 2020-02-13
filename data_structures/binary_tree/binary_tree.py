from data_structures.queue.queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self._pre_order_print(self.root, '')
        elif traversal_type == 'inorder':
            return self._in_order_print(self.root, '')
        elif traversal_type == 'postorder':
            return self._post_order_print(self.root, '')
        elif traversal_type == 'levelorder':
            return self._level_order_print(self.root)
        else:
            return "Traversal type not found."

    def _pre_order_print(self, start, traversal):
        # Root->Left->Right
        if start:
            traversal += str(start.value) + '-'
            traversal = self._pre_order_print(start.left, traversal)
            traversal = self._pre_order_print(start.right, traversal)
        return traversal

    def _in_order_print(self, start, traversal):
        # Left->Root->Right
        if start:
            traversal = self._in_order_print(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self._in_order_print(start.right, traversal)
        return traversal

    def _post_order_print(self, start, traversal):
        # Left->Right->Root
        if start:
            traversal = self._post_order_print(start.left, traversal)
            traversal = self._post_order_print(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal

    def _level_order_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek().value) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree(traversal_type='preorder'))
print(tree.print_tree(traversal_type='inorder'))
print(tree.print_tree(traversal_type='postorder'))
print(tree.print_tree(traversal_type='levelorder'))
