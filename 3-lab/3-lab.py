from tkinter import *
from tkinter import messagebox 
from tkinter import scrolledtext  

#Returns the result string
def result_string(dicti):  
	result = '';
	for key, value in dicti.items():
		if type(value) is dict:
			result += '{}:\n'.format(key)
			for key1, value1 in value.items():
				result += '  {} : {}\n'.format(key1, str(value1))
		else:
			result += '{} : {}\n'.format(key, str(value))
	return result		

#Causes text analysis, output preparation and outputs the result
def result_clicked():   
   dicti = analize_text(txt.get("1.0","end"))
   result= result_string(dicti)
   messagebox.showinfo('Result', result) 
  
#Graphical user interface settings  
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