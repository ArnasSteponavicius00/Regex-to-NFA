#! usr/bin/env python3
#Arnas Steponavicius

from match import match
import menu

#Print header
menu.header()

def runner():
	'''Runner function, allows user to input their regex and string to match'''
	cont = True;

	while cont:
		#Take user input
		regex = input("\nregex=")
		userString = input("match=")

		result = match(regex, userString)
		print(f"\nmatch: {result}")

		option = input("\ntest another string? [y/n]: ")

		if option.casefold() == 'n':
			cont = False
			print("===============================")
			print("EXIT")

		print("===============================")

runner()