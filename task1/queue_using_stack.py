class double_stacked_queue: 
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enqueue(self, x):
		
		# Move all elements from s1 to s2 
		while len(self.s1) != 0: 
			self.s2.append(self.s1[-1]) 
			self.s1.pop()

		# Push item into self.s1 
		self.s1.append(x) 

		# Push everything back to s1 
		while len(self.s2) != 0: 
			self.s1.append(self.s2[-1]) 
			self.s2.pop()

	# Dequeue an item from the queue 
	def dequeue(self):
		# if first stack is empty 
		if len(self.s1) == 0: 
			return -1
	
		# Return top of self.s1 
		x = self.s1[-1] 
		self.s1.pop() 
		return x


class single_stacked_queue:
	def __init__(self):
		self.s = []
		
	# Enqueue an item to the queue 
	def enqueue(self, data):
		self.s.append(data)
		
	# Dequeue an item from the queue 
	def dequeue(self):
		# Return if queue is empty
		if len(self.s) <= 0:
			return -1
		
		# pop an item from the stack
		x = self.s[len(self.s) - 1]
		self.s.pop()
		
		# if stack become empty
		# return the popped item
		if len(self.s) <= 0:
			return x
			
		# recursive call
		item = self.dequeue()
		
		# push popped item back to
		# the stack
		self.s.append(x)
		
		# return the result of 
		# deQueue() call
		return item
	

if __name__ == '__main__':
    q = single_stacked_queue()
    print("queueing 1, 2, and 3")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
     
    print("dequeuing 3 times")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())  


    print("\nqueueing 1, 2, and 3")
    t = double_stacked_queue()
    t.enqueue(1)
    t.enqueue(2)
    t.enqueue(3)
     
    print("dequeuing 3 times")
    print(t.dequeue())
    print(t.dequeue())
    print(t.dequeue())  
