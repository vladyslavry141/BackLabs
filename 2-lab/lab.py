import re
import keyword

def find_identifier(user_input):
	find_ident_re = re.compile(r'\b[^\W\d][\w]{0,78}\b')
	finded_ident = find_ident_re.findall(user_input)
	checked_ident = filter(lambda word: word not in keyword.kwlist, finded_ident)
	result = ", ".join(checked_ident)
	print(result)


def is_identifier(user_input):
	find_ident_re = re.compile(r'\b[^\W\d][\w]{0,78}\b')
	match = find_ident_re.fullmatch(user_input)
	if match is None:
		print("This string can not be a identifier")
	elif match[0] not in keyword.kwlist:
		print("This string can not be a identifier")
	else:
		print("This string is a keyword")


variant = input("""Press:
(1) to check one identifier
(2) to find the list of identifiers: """)
user_input = input("Enter the string: ")
if(variant == '1'):
	is_identifier(user_input)
elif(variant == '2'):
	find_identifier(user_input)
else:
	print("Wrong input")
