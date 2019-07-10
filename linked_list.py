class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def has_next(self):
        if self.next is not None:
            return True
        else:
            return False


class LinkedList:

    def __init__(self):
        self.head = None
        self.current_node = None

    def add(self, data):
        if self.current_node is None:
            self.current_node = Node(data)
            return self.current_node

        else:
            self.current_node.next = Node(data)

            if self.head is None:
                self.head = self.current_node

            self.current_node = Node(data)
            return self.current_node



def generate_list(n):
    linked_list = LinkedList()
    asd = 0  # type: dict
    for i in range(n):
        linked_list.add(i)
