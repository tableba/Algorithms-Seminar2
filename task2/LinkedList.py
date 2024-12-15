class Node() :
    def __init__(self, name, address, next) -> None:
        self.address = address
        self.name = name
        self.next = next

class LinkedList() :
    def __init__(self) -> None:
        self.head = None
        self._current = None

    def __iter__(self):
        """Return an iterator object (self in this case)."""
        self._current = self.head 
        return self

    def __next__(self):
        """Return the next value in the linked list during iteration."""
        if not self._current:
            name = self.head.name
            address = self.head.address
            self._current = self.head.next
            return (name, address)
            
        name = self._current.name
        address = self._current.address
        self._current = self._current.next
        return (name, address)

    def __str__(self) :
        out = ""
        if self.head is None:
            return out
        current_node = self.head
        while current_node.next :
            out += f"{current_node.name}|{current_node.address} -> "
            current_node = current_node.next
        out += f"{current_node.name}|{current_node.address} -> "
        
        return out[:-3]

    def get_size(self) :
        if self.head is None:
            return 0

        size  = 1
        current_node = self.head
        while current_node.next is not None :
            current_node = current_node.next
            size += 1

        return size

    def get_node(self, index:int):
        if self.head is None:
            return
        current_node = self.head
        try:
            for _ in range(index) :
                current_node = current_node.next

            return (current_node.name, current_node.address)
        except Exception :
            print("index out of range")

    def remove_first_node(self) :
        if self.head is None :
            return
        self.head = self.head.next

    def remove_at_index(self, index):
            if self.head is None:
                return

            if index == 0:
                self.remove_first_node()
                return

            current_node = self.head
            position = 0
            while current_node is not None and current_node.next is not None and position + 1 != index:
                position += 1
                current_node = current_node.next

            if current_node is not None and current_node.next is not None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def remove_node(self) :
        """removes last element in the linked list"""
        # there no node
        if self.head is None:
            return

        # there is only one node
        if self.head.next is None:
            self.head = None
                
        # there is more than one node
        else :
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next

            current_node.next = None

    def remove_node_name(self, name):
        current_node = self.head

        # If the node to be removed is the head node
        if current_node is not None and current_node.name == name:
            self.remove_first_node()
            return

        # Traverse and find the node with the matching name
        while current_node is not None and current_node.next is not None:
            if current_node.next.name == name:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # If the name was not found
        print("Node with the given name not found")

    def add_node(self, name, address) :
        """appends data to the linked list (as last element)"""
        # there no node
        if self.head is None:
            self.head = Node(name, address, None)

        # there is at least one node
        else :
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = Node(name, address, None)


if __name__ == "__main__":
    LL = LinkedList()

    LL.add_node(9, 0)
    LL.add_node(9, 0)
    LL.add_node(9, 0)
    LL.add_node(3, 0)
    LL.add_node(9, 0)
    LL.add_node(9, 0)

    print(LL)
    print(LL.get_size())

    LL.remove_at_index(3)

    print(LL)
    print(LL.get_size())
