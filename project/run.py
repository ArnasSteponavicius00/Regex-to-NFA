#! usr/bin/env python3
#Arnas Steponavicius

import argparse
import sys
sys.path.append('./utils')

from match import match
import menu

#Print header
menu.header()

parser = argparse.ArgumentParser(
	description='Takes in a regex and string, then checks if they match', 
	prog='Regular expression matcher')

parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-r', '--regex', help='The regular expression used to match.')
parser.add_argument('-s', '--string', help='The string you wish to check if it matches.')
args = parser.parse_args()

def main():
	result = match(args.regex, args.string)
	print(f"result: {result}")


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

if __name__ == '__main__':
	if not any (vars(args).values()):
		runner()
	
	if any (vars(args).values()):
		main()