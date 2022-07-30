import numpy as np


class UnorderedVector:
    """
    Defining unordered vector or list

    attrib:
        capacity: int
        last_pos (last position): int
        values: []
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.last_pos = -1
        self.values = np.empty(self.capacity, dtype=int)

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
            self.values[self.last_pos] = value
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


if __name__ == "__main__":
    # 1 print
    print("\n# 1 - print")
    vector = UnorderedVector(5)
    vector.print_values()

    # 2 insert
    print("\n# 2 - insert")
    vector.insert(1)
    vector.print_values()

    # 3 insert
    print("\n# 3 - insert")
    vector.insert(2)
    vector.insert(3)
    vector.insert(4)
    vector.insert(5)
    vector.print_values()

    # 4 values
    print("\n# 4 values")
    print(vector.values)

    # 5 Vector is Full
    print("\n# 5 Vector is Full")
    vector.insert(6)

    # 6 Search value
    print("\n# 6 Search value")
    vector.search(4)

    # 7 Search value that doesn't in the vector
    print("\n# 7 Search value that doesn't in the vector")
    vector.search(7)

    # 8 Delete a value from vector
    print("\n# 8 Delete a value from vector")
    vector.print_values()

    print()
    vector.delete(3)
    vector.print_values()
