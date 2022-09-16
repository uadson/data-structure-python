from models.unordered import UnordArray
from core import capacity, num_input


menu = {
	1: "Show length/capacity's array",
	2: 'Show array',
	3: 'Insert value',
	4: 'Search value',
	5: 'Delete value',
	6: 'Exit',
}


def unord():
	arr = UnordArray()

	arr.len_arr = capacity()

	while True:
		print("\n")

		for key, value in menu.items():
			print(f"[{key}] - [{value}]")

		select = int(input("\nSelect a option: "))

		if select == 1:
			print(f"\nThe capacity's array is: {arr.len_arr}")

		if select == 2:
			arr.show()

		if select == 3:
			for num in num_input():
				arr.insert(num)
		
		#if select == 4:
		#	arr.clean()
		#	arr.len_arr = int(input('\nType the length of array: '))

		#if select == 5:
		#	break