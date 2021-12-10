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

	def retrieve(self, key):
		# get index with same way as assign
		array_index = self.compressor(self.hash(key))
		return self.array[array_index]

# create the object
hash_map = HashMap(20)
# assign key-value
hash_map.assign("gneiss", "metamorphic")
# get the value using the key
print(hash_map.retrieve("gneiss"))