from random import randint


def capacity():
	return randint(4, 6)

def num_input():
	num_lst = []

	cap = capacity()

	for n in range(cap):
		num = randint(1, 20)

		while num in num_lst:
			num = randint(1, 20)

		if len(num_lst) == cap:
			break 

		num_lst.append(num)

	return num_lst


if __name__ == '__main__':
	num_input()
