"""Big-O
    Objectve comparison between algorithms.

    The complexity of the algorithm increases with the inputs.
    """

# Exemple

# Function 1 - O(n)


from timeit import timeit

# O(n) - n steps


def add(n):
    total = 0  # 1
    for i in range(n + 1):  # n
        total += i
    return total


# output: 55


print(f"Total is: {add(10)} - Time is: {timeit():.4f}s")

# O(3) - 3 steps


def add2(n):
    return (n * (n + 1)) / 2  # n * = 1, (n + 1) = 2 and / 2 = 3


# output: 55


print(f"Total is: {add2(10)} - Time is: {timeit():.4f}s")

# Lists


def list1():
    """Create a list with 1000 objects

    Returns:
        list: [0, ..., 999]

    Big-O -> O(1000) or O(n)-> n steps in loop for
    """
    l = []
    for i in range(1000):
        l += [i]
    return l


print(f"Total is: {list1()} - Time is: {timeit():.4f}s")
print(len(list1()))

# output:
# [0, ..., 999]
# [1000]


def list2():
    """Create a list with 1000 elements, using range class

    Returns:
        range: (0, 1000)

    Bi-O -> O(1) around the use range class
    """
    return range(1000)


print(list2())
# output: range(0, 1000)
