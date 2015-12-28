from queue import Queue
import unittest
import random

class TestQueue(unittest.TestCase):

	def test_empty(self):
		q = Queue(10)
		assert q.empty()
		assert q.enqueue(22)
		assert not q.empty()

	def test_full(self):
		q = Queue(1)
		assert not q.full()
		assert q.enqueue(22)
		assert q.full()

	def test_getSize(self):
		q = Queue(8)
		assert q.getSize() == 8

	def test_getNumElements(self):
		q = Queue(2)
		assert q.getNumElements() == 0;
		assert q.enqueue(22)
		assert q.getNumElements() == 1;

	def test_enqueue(self):
		q = Queue(3)
		assert q.enqueue(10)
		assert q.enqueue(20)
		assert q.enqueue(30)
		assert not q.enqueue(40)
		assert q.dequeue() == 10
		assert q.getNumElements() == 2
		assert q.enqueue(40)

	def test_dequeue(self):
		q = Queue(3)
		assert q.dequeue() == None
		assert q.enqueue(10)
		assert q.dequeue() == 10
		assert q.enqueue(10)
		assert q.enqueue(20)
		assert q.enqueue(30)
		assert q.dequeue() == 10
		assert q.dequeue() == 20
		assert q.dequeue() == 30

	def test_pseudoRandom(self):
		data = []
		q = Queue(5)
		random.seed(1234)
		for it in range(0, 100):
			if not random.randint(0,1):
				val = random.randint(0,1000)
				if q.enqueue(val):
					data.append(val)
			else:
				if len(data):
					val = q.dequeue()
					assert val == data[0]
					del(data[0])
