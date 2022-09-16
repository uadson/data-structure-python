class UnordArray:
	len_arr: int = 0
	arr: list = []

	def show(self):
		if not self.arr:
			print("\nArray is empty")
		else:
			print(f"\nArray: {self.arr}\n")
			for n, i in enumerate(self.arr):
				print(f"index: {n} - value: {i}")

	def insert(self, value):
		if len(self.arr) == self.len_arr:
			print("\nArray is full")
			return

		self.arr.append(value)

	def search(self, value):
		for i in range(len(self.arr)):
			if value == self.arr[i]:
				print(f"\nvalue: {value} - index: {i}")
				return i

		print("\nNot found")
		return 

	def delete(self, value):
		index = self.search(value)

		for i in range(index, len(self.arr)):
			self.arr[i] = self.arr[i + 1]
				