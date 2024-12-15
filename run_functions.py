from task1 import single_queued_stack, double_queued_stack, single_stacked_queue, double_stacked_queue
from task2 import LinkedList
from task3 import Josephus
from time import time
import matplotlib.pyplot as plt
import numpy as np


def run_joshephus():
    j = Josephus()
    
    result = {"array": [],
              "array_iterator": [],
              "linkedlist": [],
              "linkedlist_iterator": []}
    n = 1
    while n < 100000:
        for m in range(1, 2, 1) :
            start = time()
            j.array_solve(m, n)
            stop = time()
            result["array"].append((n, m, stop - start))
        
            start = time()
            j.array_iterator_solve(m, n)
            stop = time()
            result["array_iterator"].append((n, m, stop - start))

            start = time()
            j.linkedlist_solve(m, n)
            stop = time()
            result["linkedlist"].append((n, m, stop - start))

            start = time()
            j.linkedlist_iterator_solve(m, n)
            stop = time()
            result["linkedlist_iterator"].append((n, m, stop - start))
        n *= 10

    plt.figure(figsize=(12, 6))
    for algo, timing_data in result.items() :
        x = [data[0] for data in timing_data]
        y = [data[2] for data in timing_data]
        plt.plot(x, y, label=algo)

    plt.title('Execution Time of Jesephus Problem Algorithms (M = 1)')
    plt.xlabel('n (number of people)')
    plt.ylabel('Time (sec)')
    plt.yscale('log')
    plt.xscale('log')
    plt.legend()
    plt.grid()
    plt.show()


def run_linked_list():
    LL = LinkedList()
    LL.add_node("Antoine", "2 Rue ...")
    LL.add_node("Peter", "Hell")
    LL.add_node("Dieter", "In heaven")
    LL.add_node("Chrisian", "In church")
    LL.add_node("Max", "Some street in america because Max sounds american for some reason")
    LL.add_node("Piotr", "Definately in russia")

    print(f"added 6 nodes:\n{LL}")

    LL.remove_node()
    LL.remove_node()

    print(f"removed 2 nodes:\n{LL}")

    print(f"get the 3th node:\n{LL.get_node(2)}")



def run_stacks():
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


def run_queues():
    # Initialize the double_stacked_queue
    print("Testing double_stacked_queue...")
    queue1 = double_stacked_queue()
    for i in range(1, 11):  # Enqueue numbers 1 to 10
        queue1.enqueue(i)
        print(f"Enqueued {i} to double_stacked_queue")

    print("\nDequeueing 5 elements from double_stacked_queue:")
    for _ in range(5):
        dequeued_value = queue1.dequeue()
        print(f"Dequeued {dequeued_value} from double_stacked_queue")

    # Initialize the single_stacked_queue
    print("\nTesting single_stacked_queue...")
    queue2 = single_stacked_queue()
    for i in range(1, 11):  # Enqueue numbers 1 to 10
        queue2.enqueue(i)
        print(f"Enqueued {i} to single_stacked_queue")

    print("\nDequeueing 5 elements from single_stacked_queue:")
    for _ in range(5):
        dequeued_value = queue2.dequeue()
        print(f"Dequeued {dequeued_value} from single_stacked_queue")

    # Compare the states of both queues by dequeuing all elements
    double_queue_remaining = []
    single_queue_remaining = []

    print("\nDequeuing remaining elements from both queues...")
    while True:
        val1 = queue1.dequeue()
        val2 = queue2.dequeue()
        if val1 == -1 and val2 == -1:  # Both queues are empty
            break
        if val1 != -1:
            double_queue_remaining.append(val1)
            print(f"Remaining in double_stacked_queue: {val1}")
        if val2 != -1:
            single_queue_remaining.append(val2)
            print(f"Remaining in single_stacked_queue: {val2}")

    # Check if the remaining elements match
    print("\nFinal comparison:")
    print(f"Remaining in double_stacked_queue: {double_queue_remaining}")
    print(f"Remaining in single_stacked_queue: {single_queue_remaining}")
    print(f"Queues match: {double_queue_remaining == single_queue_remaining}")


# run_queues()
# run_stacks()
