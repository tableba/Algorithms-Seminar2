from queue import Queue

class double_queued_stack :

    # Initializing a stack.
    def __init__(self):
        self.q = Queue()
        self.q2 = Queue()
        self.size = 0

    # Push a value into the stack.
    def push(self, value):
        self.q.put(value)
        self.size += 1

    # Remove a value from the stack and return.
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        
        item = self.__get_last_element(remove=True)
        self.size -= 1
        return item

    def __get_last_element(self, remove=False) :
        """return the last element of the queue ; removes that item if remove = True"""
        if self.size == 0:
            return 0
            # put the queue's content into a second queue without the most recent elt

        q2 = Queue()
        for _ in range(self.size - 1) :
            q2.put(self.q.get())

        # remove remaining elt
        removed_elt = self.q.get()

        # put content back into the main queue
        for _ in range(self.size - 1) :
            self.q.put(q2.get())

        return removed_elt
        
    def is_empty(self) :
        return self.size == 0

    # String representation of the stack
    def __str__(self):
        queue_array = [self.q.get() for _ in range(self.size)]
        out = ""
        for elt in queue_array:
            out += f"{elt}<-"
            self.q.put(elt)

        return out[:-2]


class single_queued_stack :

    # Initializing a stack.
    def __init__(self):
        self.q = Queue()
        self.size = 0

    # Push a value into the stack.
    def push(self, value):
        self.q.put(value)
        self.size += 1

    # Remove a value from the stack and return.
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        
        item = self.__get_last_element(remove=True)
        self.size -= 1
        return item

    def __get_last_element(self, remove=False) :
        """return the last element of the queue ; removes that item if remove = True"""
        if self.size == 0:
            return 0

        # put the queue's content into a list
        queue_array = [self.q.get() for _ in range(self.size)]

        if remove:
            # reconstruct the queue without the last element
            for elt in queue_array[:-1]:
                self.q.put(elt)

        else:
            # reconstruct the whole queue
            for elt in queue_array:
                self.q.put(elt)

        return queue_array[-1]
        
    def is_empty(self) :
        return self.size == 0

    # String representation of the stack
    def __str__(self):
        queue_array = [self.q.get() for _ in range(self.size)]
        out = ""
        for elt in queue_array:
            out += f"{elt}<-"
            self.q.put(elt)

        return out[:-2]



if __name__ == "__main__":
    stack1 = double_queued_stack()
    for i in range(1, 11):
        stack1.push(i)
    print(f"stack1: {stack1}")

    for _ in range(1, 6):
        top_value = stack1.pop()
        print(f"Pop: {top_value}") 
    print(f"stack1: {stack1}")

    #padding
    print()

    stack2 = single_queued_stack()
    for i in range(1, 11):
        stack2.push(i)
    print(f"stack2: {stack2}")

    for _ in range(1, 6):
        top_value = stack2.pop()
        print(f"Pop: {top_value}") 
    print(f"stack2: {stack2}")


    print(f"Stacks match : {str(stack1) == str(stack2)}")
