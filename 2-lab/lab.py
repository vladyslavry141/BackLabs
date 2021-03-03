import re

def find_words(indef):
	p = re.compile(r'\b[a-z]{3}\b')
	list_words = p.findall(indef)
	result = ", ".join(result)
	print(result)


def check_word(indef):
	p = re.compile(r'\b[a-z]{3}\b')
	match = p.fullmatch(indef)
	print("True" if match else 'False') 




variant = input("Press 1 to check one identifier or 2 to find the list of identifiers   ")
indeficators = input("enter the string   ")
if(variant == '1'):
	check_word(indeficators)
elif(variant == '2'):
	find_words(indeficators)

