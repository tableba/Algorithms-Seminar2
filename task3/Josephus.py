from itertools import cycle
from task2 import LinkedList 

class Josephus(): 
    def __init__(self) -> None:
        pass

    def array_solve(self, M, N):
        arr = [i + 1 for i in range(N)]
        remove_order = []
        pointer = 0
        while len(arr) > 1 :
            pointer = (pointer + M) % len(arr)
            # print(M , "+", len(arr), " mod ", len(arr), "=", pointer)
            remove_order.append(arr.pop(pointer))
            # print(arr, remove_order)

        return remove_order

    def array_iterator_solve(self, M, N):
        """iterators don't really work in python, this is some vague implementation using and iterator"""
        arr = [i + 1 for i in range(N)]
        remove_order = []

        # initialize iterator
        iterator = cycle(arr)
        next(iterator)

        current_index = 0
        removed = arr[0]
        while len(arr) > 1 :

            for _ in range(M):
                current_index = (current_index + 1) % len(arr)
                removed = next(iterator)
            arr.remove(removed)
            remove_order.append(removed)

            # recreate the iterator and put it at the right position
            iterator = cycle(arr)
            # update removed variable in case of m = 0
            removed = next(iterator)
            for _ in range(current_index) :
                next(iterator)

        return remove_order

    def linkedlist_solve(self, M, N):
        LL = LinkedList()
        # initialize linked list with all participants
        for i in range(N) :
            LL.add_node(i + 1, 0) 

        remove_order = []
        pointer = 0
        while LL.get_size() > 1 :
            pointer = (pointer + M) % LL.get_size()
            # print(pointer)
            # print(LL)
            remove_order.append(LL.get_node(pointer)[0]) # get_node returns name and address
            LL.remove_at_index(pointer)

        return remove_order

    def linkedlist_iterator_solve(self, M, N):
        LL = LinkedList()
        # initialize linked list with all participants
        for i in range(N) :
            LL.add_node(i + 1, 0) 

        # initialize iterator and point it to the first elt
        iterator = iter(LL)
        next(iterator)

        current_index = 0
        removed = LL.get_node(0)
        remove_order = []
        while LL.get_size() > 1 :
            for _ in range(M):
                current_index = (current_index + 1) % LL.get_size()
                removed = next(iterator)
            LL.remove_node_name(removed[0])
            remove_order.append(removed[0])

            iterator = iter(LL)
            removed = next(iterator)
            for _ in range(current_index) :
                next(iterator)


        return remove_order

if __name__ == "__main__":
    j = Josephus()

    print(f"remove order is {j.array_solve(2, 17)}")
    print(f"remove order is {j.array_iterator_solve(2, 17)}")
    print(f"remove order is {j.linkedlist_solve(2, 17)}")
    print(f"remove order is {j.linkedlist_iterator_solve(2, 17)}")


