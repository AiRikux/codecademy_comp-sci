class HashMap:
	def __init__(self, array_size):
		self.array_size = array_size
		self.array = [None] * array_size

	def hash(self, key):
		# turn the key into list of bytes
		key_bytes = key.encode()
		# turn the bytes into hash code with sum
		hash_code = sum(key_bytes)
		return hash_code

	def compressor(self, hash_code):
		# get modulus
		return hash_code % self.array_size

	def assign(self, key, value):
		# get hash code
		code = self.hash(key)
		# get index
		index = self.compressor(code)
		# assign value to this index
		self.array[index] = value

