class UnorderedVector:
    """
    Defining unordered vector or list

    attrib:
        capacity: int
        last_pos (last position): int
        values: []
    """

    capacity: int
    last_pos: int = -1
    values: list = []

    # O(n)
    def print_values(self):
        """print result in terminal"""
        if self.last_pos == -1:
            print("Vector is Empty")
        else:
            for i in range(self.last_pos + 1):
                print(f"Position {i} - value {self.values[i]}")

    # O(1) - constant
    def insert(self, value):
        """Insert value to vector

        Args:
            value (int): 1 to 5
        """
        if self.last_pos == self.capacity - 1:
            print(f"Capacity: {self.capacity}")
            print(f"Last Position: {self.last_pos} - Value: {self.values[4]}")
            print("Vector is Full")
        else:
            self.last_pos += 1
            # last_pos(-1) + last_pos(1) = 0
            # last_pos = 0
            # self.values[self.last_pos] = value
            self.values.append(value)
            # from values[] to values[value]

    # O(n) - linear
    def search(self, value):
        """Search value in vector

        Args:
            value (int): 1 to 5
        """
        for i in range(self.last_pos + 1):
            if value == self.values[i]:
                print(f"Position: {i} - Value: {self.values[i]}")
                return self.values[i]
        print(f"Not found")
        return -1

    def delete(self, value):
        """Delete a value

        Args:
            value (int): value selected to delete
        """
        print("\n# 1 - search value")
        pos = self.search(value)
        print("\n# 2 - check if value exists")
        if pos == -1:
            print("\nValue not found.")
            return -1
        else:
            print("# 3 - reorganize the list of values")
            for i in range(pos, self.last_pos):
                print(i, self.values[i], self.values[i + 1])
                self.values[i] = self.values[i + 1]
            print("\n#Update")
            self.last_pos -= 1
