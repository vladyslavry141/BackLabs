import re
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

# Regex for extracting required values
word_regex = r'\b[^\W\d]+(?:[\'-]?[^\W\d]+)*\b'
punct_marks_regex = r'[^\w\n]'
letter_regex = r'[^\W\d]'


# Create dictionary where element of list
# and number of this element are collected
def list_to_dict(inp_list):
    res_dict = {}
    for el in inp_list:
        if res_dict.get(el) is None:
            res_dict[el] = 0
        res_dict[el] += 1
    return res_dict


# Return list of extracted values using regex
def found_re(regex, text):
    regex_re = re.compile(regex)
    matched = regex_re.findall(text)
    return matched


# Create a dictionary, where result values are collected
def analize_text(text):
    res = {}
    # Insert a number of letters on entered text in result dictionary
    letters = found_re(letter_regex, text)
    res['Letters'] = len(letters)
    # Insert a dictionary of words that are repeated in result dictionary
    words = found_re(word_regex, text)
    words_dict = list_to_dict(words)
    filtered_words_dict = {k: v for k, v in words_dict.items() if v > 1}
    res['Words'] = filtered_words_dict
    # Insert a dictionary of punctuation marks
    # which contains punctuation mark value and its num in text
    punct_marks = found_re(punct_marks_regex, text)
    punct_marks_dict = list_to_dict(punct_marks)
    # Remove a space sign num and insert it in result dictionary
    space_sign_num = punct_marks_dict.pop(' ', 0)
    res['Space sign num'] = space_sign_num
    res['Punctuation marks'] = punct_marks_dict
    return res

# Returns the result string
def result_string(dicti):
    result = ''
    for key, value in dicti.items():
        if type(value) is dict:
            result += '{}:\n'.format(key)
            for key1, value1 in value.items():
                result += '  {} : {}\n'.format(key1, str(value1))
        else:
            result += '{} : {}\n'.format(key, str(value))
    return result


# Causes text analysis, output preparation and outputs the result
def result_clicked():
    dicti = analize_text(txt.get("1.0", "end"))
    result = result_string(dicti)
    messagebox.showinfo('Result', result)


# Graphical user interface settings
window = Tk()
window.title("Lab-3")
window.geometry('500x250')
lbl = Label(window, text="Enter text")
lbl.grid(column=2, row=0)
txt = scrolledtext.ScrolledText(window, width=60, height=10)
txt.grid(column=2, row=1)
txt.focus()
btn = Button(window, text="Analize", command=result_clicked)
btn.grid(column=2, row=2)
window.mainloop()
