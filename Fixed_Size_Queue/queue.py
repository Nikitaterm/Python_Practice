import array

class Queue:
	""" Simple fixed size queue implementation """
	def __init__(self, size):
		self.size = size
		self.num_elements = 0
		self.tail = 0
		self.head = 0
		self.data = array.array("i", range(size))

	def empty(self):
		return self.num_elements == 0

	def full(self):
		return self.num_elements == self.size

	def getSize(self):
		return self.size

	def getNumElements(self):
		return self.num_elements;

	def enqueue(self, val):
		if self.full():
			return False
		self.data[self.tail] = val
		if (self.tail == self.size - 1):
			self.tail = 0
		else:
			self.tail += 1
		self.num_elements += 1
		return True

	def dequeue(self):
		if self.empty():
			return None
		data = self.data[self.head]
		if (self.head == self.size - 1):
			self.head = 0
		else:
			self.head += 1
		self.num_elements -= 1
		return data
