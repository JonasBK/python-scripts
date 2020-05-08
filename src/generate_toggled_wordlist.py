#!/usr/bin/python3

# Example:
# python3 generate_toggled_wordlist.py "CONGRAT0905"
# congrat0905
# congraT0905
# congrAt0905
# congrAT0905
# congRat0905
# congRaT0905
# congRAt0905
# ...

import sys, argparse

SLEN_1 = 0

def printwordlist(index, curword):
	# Check if index is last symbol in string
	if (index == SLEN_1):
		# Check if index symbol is letter
		if (curword[index].isalpha()):
			# With lower
			print(curword[:index] + curword[index].lower() + curword[index + 1:])
			# With upper
			print(curword[:index] + curword[index].upper() + curword[index + 1:])
		else:
			print(curword)
	
	# Check if index symbol is letter
	elif (curword[index].isalpha()):
		curword = curword[:index] + curword[index].lower() + curword[index + 1:]
		# With lower
		printwordlist(index+1, curword)

		# With upper
		curword = curword[:index] + curword[index].upper() + curword[index + 1:]		
		printwordlist(index+1, curword)
	else:
		printwordlist(index+1, curword)


def main(argv):
	global SLEN_1
	parser = argparse.ArgumentParser()
	parser.add_argument("inword", help="the word used to generate toggled wordlist")
	args = parser.parse_args()
	SLEN_1 = len(str(args.inword)) - 1
	printwordlist(0, str(args.inword))

if __name__ == "__main__":
	main(sys.argv[1:])
