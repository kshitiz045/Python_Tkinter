#Counter program  in python tkinter

from tkinter import *

counter = 0

def count_lab(label1):
	counter = 0
	def count():
		global counter
		counter +=1
		label1.config(text=str(counter))
		label1.after(1000 ,count)
	count()

root = Tk()
root.title("Counter")
label1 = Label(root , fg="red")
label1.pack()
count_lab(label1)
button = Button(root , text="Stop" , width=25  , command=root.destroy)
button.pack()
root.mainloop()
