from data_structures.linked_list.singly_linked_list import LinkedList


def nth_to_last_count(head, n):
    if head is None:
        return

    current_node = head
    follower_node = head

    for i in range(n):
        current_node = current_node.next

    while current_node:
        current_node = current_node.next
        follower_node = follower_node.next
    return follower_node.data


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print(nth_to_last_count(ll.head, 1))
