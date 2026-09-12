from tkinter import *

#initial setup of GUI
window = Tk()
window.title("Speed typing checker")
window.geometry("500x500")

#generate_text will generate text and start the timer
def generate_text():

    pass

def stop_timer():

    pass


#GUI elements
    #first row
btn_start = Button(text="START", width=20, command=generate_text)
btn_start.grid(row=0, column=0)

btn_stop = Button(text="STOP", width=20, command=stop_timer)
btn_start.grid(row=0, column=1)

    #second row




window.mainloop()