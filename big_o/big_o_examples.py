# Constant - O(1)

list1 = [1, 2, 3, 4, 5]


def constant(n):
    """Fixed number of steps for execution regardless of the value of n"""

    # Example:
    # Step 1
    print(n[0])

    # Step 2
    print(n[1])


print(f"\nConstant")
constant(list1)

# output:
# 1
# 2


# Linear - O(n)


def linear(n):
    """The number of steps increases proportionally to the value of n"""

    # Example:

    for i in n:
        # Steps
        print(i)


print("\nLinear")
linear(list1)

# output:
# 1
# 2
# 3
# 4
# 5


# Quadratic - O(n^2) - polynomial


def quadratic(n):
    # Step 1
    for i in n:
        # Step 2
        for j in n:
            # Steps of step 1 and step 2
            print(i, j)
        print("---")


print("\nQuadratic")
quadratic(list1)


# output:
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# ---
# 2 1
# 2 2
# 2 3
# 2 4
# 2 5
# ---
# 3 1
# 3 2
# 3 3
# 3 4
# 3 5
# ---
# 4 1
# 4 2
# 4 3
# 4 4
# 4 5
# ---
# 5 1
# 5 2
# 5 3
# 5 4
# 5 5
# ---


# Evaluation
# O(1) + O(5) + O(n) + O(3) =
# O(9) + O(n) -> O(n)
# Finally Algorithm is O(n)
def combination(n):
    # O(1)
    print(n[0])

    # O(5)
    for i in range(5):
        print(i)

    # O(n)
    for i in n:
        print(i)

    # O(3)
    print("Python")
    print("is")
    print("Cool")
