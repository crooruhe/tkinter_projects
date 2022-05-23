import os
import sys
import tkinter as tk





if __name__ == '__main__':


	def handle_click():
		print('test')
		entry_1.delete(0, tk.END)
    # check to make sure there is a valid IP Address
	# send input to xmas tcp packet function


	window = tk.Tk()
	#text_label_1 = tk.Label(text="IP Address")
	
	button_1 = tk.Button(master=window, text="Xmas Tree Attack", width=15, height=2, command=handle_click)
	entry_1 = tk.Entry(fg="#0fd9cb", bg="#000000")
	entry_1.insert(0, "ip address")
	
	
	#text_label_1.pack()
	relief = tk.GROOVE
	entry_1.pack()
	button_1.pack()
	
	

	
	window.mainloop() # code after this will not run until the window is closed (X)