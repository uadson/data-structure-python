from .unordered import unord


def main():
	menu = {
		1: "Ordered array",
		2: "Unorderd array",
		3: "Exit",
	}

	while True:
		print("\n Ordered or Unorderd Array\n")
		for key, value in menu.items():
			print(f"{key} - {value}")

		select = int(input("\nSelect a option: "))

		if select == 1:
			pass

		if select == 2:
			unord()

		try:
			if select == 3:
				break
		except KeyboardInterrupt:
			python("\nProgram closed")
			break