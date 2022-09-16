from unord_vec import UnorderedVector

# 1 print
print("\n# 1 - print")
vector = UnorderedVector()
vector.capacity = 5
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
