def remove_dups(head):  # O(n) speed with O(n) space for hash table
    hash_table = {head.value: True}
    while head is not None:
        print(hash_table)
        if head.next_node is not None:
            if hash_table.get(head.next_node.value, None) is not None:
                head.next_node = head.next_node.next_node
            else:
                hash_table[head.next_node.value] = True
        head = head.next_node


def remove_dups_alternative(head):  # O(n^2) speed with O(1) space due to no hash table
    while head is not None:
        runner = head
        while runner is not None:
            if runner.next_node is not None and runner.next_node.value == head.value:
                if runner.next_node is None:
                    break
                else:
                    runner.next_node = runner.next_node.next_node
            runner = runner.next_node
        head = head.next_node
