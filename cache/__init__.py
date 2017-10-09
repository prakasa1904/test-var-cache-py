class Cache:
	def __init__(self, memory):
		self.memory = memory

	def set(self, key, value):
		self.memory[key] = value

	def get(self, key):
		if key in self.memory:
			return self.memory[key]
		return False