from models.unordered import UnordArray


def menu():
	dct_menu = {
		1: {'Ordered Array': {
			1: 'Show length of array',
			2: 'Show array',
			3: 'Insert and Sort values',
			4: 'Search value',
			5: 'Delete value',
			6: 'Exit',
			}
		},
		
		2: {'Unordered Array': {
			1: 'Show length of array',
			2: 'Show array',
			3: 'Insert value',
			4: 'Search value',
			5: 'Delete value',
			6: 'Exit',
			}
		}
	}

	return dct_menu
	

def main():
	unordarr = UnordArray()
	
	# capacity
	cap = int(input('\nType the length of array: '))
	
	info_menu = menu()

	while True:
		print("\n")
		
		for key_menu, value_menu in info_menu.items():
			for key, value in value_menu.items():
				print(f"[ {key_menu} ] - [ {key} ] ")
				# [ 1 ] - [ Ordered Array ]
				# [ 2 ] - [ Unordered Array ]

		select_key = int(input("\nSelect a option: "))

		if select_key == 2:
			for key_menu, value_menu in info_menu.items():
				for key, value in value_menu.items():
					for k, v in value.items():
						print(f"{k} - {v}")

			select_key = int(input("\nSelect a option: "))

		#if select == 1:
		#	print(f"\nThe capacity's array is: {arr.len_arr}")

		#if select == 2:
		#	arr.show_arr()

		#if select == 3:
		#	value = int(input("\nType a value: "))
		#	arr.insert(value)

		#if select == 4:
		#	arr.clean()
		#	arr.len_arr = int(input('\nType the length of array: '))

		#if select == 5:
		#	break
