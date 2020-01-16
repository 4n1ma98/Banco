import sys

def run():
	while True:
		option = input('''
		-*-*-*-*-*- BANPLATZI -*-*-*-*-*-
		¿Qué deseas hacer hoy?

		[A] Add customer to the deposit line
		[B] Add customer to account opening
		[C] Attend customerz
		[D] List customers in the line
		[E] Exit
		>>>''').lower()

		if option == 'a':
			pass
		elif option == 'b':
			pass
		elif option == 'c':
			pass
		elif option == 'd':
			pass
		elif option == 'e':
			sys.exit()
		else:
			print('''
	-------------------
	*------ERROR------*
	-------------------''')




if __name__ == '__main__':
	run()