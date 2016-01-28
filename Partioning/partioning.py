class Partioning:
	def __init__(self, value, max_):
		self.result = []
		self.value = value
		self.max = max_

	def partion(self):
		self.__partion(self.value, self.max, [])

	def getResult(self):
		return self.result

	def __partion(self, value, max_, pref):
		if (value == 0):
			self.result.append(pref)
			return
		for i in range(1, min(value, max_) + 1):
			pref_ = pref[:]
			pref_.append(i)
			self.__partion(value - i, i, pref_)

p = Partioning(10,3)
p.partion()
print p.getResult()
