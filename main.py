from tkinter import *
from random import randint
from text_data import temp_list
import time

TICKS = 0

#initial setup of GUI
window = Tk()
window.title("Speed typing checker")
window.geometry("500x500")
window.configure(padx=20, pady=20)

    #frame is helping me center stuff
frame = Frame(window)
frame.place(relx=0.5, rely=0.5, anchor="center")

#------------ FUNCTIONS ------------#
#start_func will generate text and start the timer
def start_func():
    #mechanic for removing and adding text
    i = randint(0,len(temp_list)-1)
    text_box.delete("1.0", "end")
    text_box.insert("1.0",temp_list[i])

    #timer start
    global TICKS
    TICKS = 60
    timer_value.config(text=str(TICKS))
    timer_func(TICKS)

def timer_func(count_sec):
    if count_sec >=0:
        timer_value.config(text=f"{count_sec:02d}")
        timer_value.after(1000, timer_func, count_sec - 1)
    else:
        timer_value.config(text=f"Score was:")

#stop_func will stop the timer, call the word counter function
def stop_func():

    pass

#word counter function
def word_count():

    pass

#-----------------------------------------------#

#GUI elements
    #first row
btn_start = Button(frame,text="START", width=20, command=start_func)
btn_start.grid(row=0, column=0, pady=(0,10))

btn_stop = Button(frame, text="STOP", width=20, command=stop_func)
btn_stop.grid(row=0, column=2, pady=(0,10))

    #second row
input = Entry(frame, width=40)
input.grid(row=1, column=0, columnspan=3, pady=(0,10))

    #third row, text
text_box = Text(frame,height=16, width=40, wrap="word")
text_box.insert("1.0", "Just a random text before real text is generated with hitting START button!")
text_box.grid(row=2, column=0, columnspan=3, pady=(10,0))

    #forth row, timer label
timer_label = Label(frame,text="Timer", font=("Courier",20))
timer_label.grid(row=3, column=1, pady=(10,0))

    #fifth row, timer value
timer_value= Label(frame,text="00", font=("Courier",20,"bold"))
timer_value.grid(row=4, column=1, pady=(10,0))


window.mainloop()