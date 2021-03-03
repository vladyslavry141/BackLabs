import re
import keyword

def find_words(user_input):
	find_words_re = re.compile(r'\b[^\W\d][\w]{0,78}\b')
	finded_indef = find_words_re.findall(user_input)
	checked = filter(lambda word: word not in keyword.kwlist, list_words)
	result = ", ".join(checked)
	print(result)


def check_word(user_input):
	p = re.compile(r'\b[^\W\d][\w]{0,78}\b')
	match = p.fullmatch(user_input)
	if match is None:
		print(False)
	else:
		print(match not in keyword.kwlist)


variant = input("""Press:
(1) to check one identifier
(2) to find the list of identifiers: """)
user_input = input("Enter the string: ")
if(variant == '1'):
	check_word(user_input)
elif(variant == '2'):
	find_words(user_input)
else:
	print("Wrong input")
