from tkinter import *
from random import randint
from text_data import temp_list


#initial setup of GUI
window = Tk()
window.title("Speed typing checker")
window.geometry("500x500")
window.configure(padx=20, pady=20)

    #frame is helping me center stuff
frame = Frame(window)
frame.place(relx=0.5, rely=0.4, anchor="center")

#generate_text will generate text and start the timer
def generate_text():

    pass

def stop_timer():

    pass


#GUI elements
    #first row
btn_start = Button(frame,text="START", width=20, command=generate_text)
btn_start.grid(row=0, column=0, pady=(0,10))

btn_stop = Button(frame, text="STOP", width=20, command=stop_timer)
btn_stop.grid(row=0, column=2, pady=(0,10))

    #second row
input = Entry(frame, width=40)
input.grid(row=1, column=0, columnspan=3, pady=(0,10))

    #third row, text
text_box = Text(frame,height=15, width=40, wrap="word")
text_box.insert("1.0", temp_list[0])
text_box.grid(row=2, column=0, columnspan=3, pady=(10,0))


window.mainloop()