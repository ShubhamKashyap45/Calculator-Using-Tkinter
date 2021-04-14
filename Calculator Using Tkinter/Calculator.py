from tkinter import *

def back():
    screen.delete(0,1)
    screen.update()

def click(event):
    global screen_value
    text=event.widget.cget("text")
    if text == "=":
        if screen_value.get().isdigit():
            value = int(screen_value.get())
        else:
            value = eval(screen.get())

        screen_value.set(value)
        screen.update()

    elif text == " A ":
        screen_value.set("")
        screen.update()

    else:
        screen_value.set(screen_value.get() + (text))
        screen.update()

root = Tk()
root.geometry("300x500")
root.title("Calculator")
root.wm_iconbitmap("Calculator.ico")

screen_value = StringVar()
screen_value.set("")

# Creating Screen
screen = Entry(root, textvar=screen_value,font="lucida 30 bold",)
screen.pack(padx=10, pady=30,fill=X)

# Creating Frame for 0 row
frame = Frame(root, bg="grey")
frame.pack()

# Creating Buttons for 0  row
button = Button(frame, text=" / ", padx=5, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text="%", padx=5, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text="C",padx=7, pady=3, font="lucida 20 bold", command=back)
button.pack(side=RIGHT)

button = Button(frame, text=" A ", padx=1, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

# Creating Frame for 1st row
frame = Frame(root, bg="grey")
frame.pack()

# Creating Buttons for 1st  row
button = Button(frame, text="*", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text="9", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text="8", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text="7", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

# Creating Frame for 2nd row
frame = Frame(root, bg="grey")
frame.pack()

# Creating Buttons for 2nd row
button = Button(frame, text="-", padx=11, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text="6",padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text="5", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text="4", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

# Creating Frame for 3rd row
frame = Frame(root, bg="grey")
frame.pack()

# Creating Buttons for 3rd row
button = Button(frame, text="+", padx=8, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text="3", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text="2", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text="1", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

# Creating Frame for 4rd row
frame = Frame(root, bg="grey")
frame.pack()

# Creating Buttons for 4rd row
button = Button(frame, text="=", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

# button = Button(frame, text="()",padx=10, pady=3, font="lucida 20 bold")
# button.pack(side=RIGHT)
# button.bind("<Button-1>", click)

button = Button(frame, text="0", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)

button = Button(frame, text=".", padx=10, pady=3, font="lucida 20 bold")
button.pack(side=RIGHT)
button.bind("<Button-1>", click)



root.mainloop()