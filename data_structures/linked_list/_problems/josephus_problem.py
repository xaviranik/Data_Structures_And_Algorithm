from data_structures.linked_list.circular_linked_list import CircularLinkedList


def solve_josephus(node, step):
    current_node = node.head

    while len(node) > 1:
        count = 1
        while count != step:
            current_node = current_node.next
            count += 1
        print("REMOVED: " + str(current_node.data))
        node.remove_node(current_node)
        current_node = current_node.next


clist = CircularLinkedList()
clist.append(10)
clist.append(20)
clist.append(30)
clist.append(40)

solve_josephus(node=clist, step=2)
print("AVAILABLE: ", end="")
clist.print_list()