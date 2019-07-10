class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked:


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
                self.head = self.current_node.next

            self.current_node = Node(data)
            return self.current_node

    def remove(self):


linked = Linked()
l1 = linked.add(1)
l2 = linked.add(2)
l3 = linked.add(3)
l4 = linked.add(4)

print(linked.head)

print(l1.data)
print(l1.next)
print(l2.data)
print(l2.next)
print(l3.data)
print(l3.next)
print(l4.data)
print(l4.next)