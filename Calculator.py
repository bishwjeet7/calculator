from tkinter import *


def click(event):
    global input_str
    text = event.widget.cget("text")
    if text == "=":
        if input_str.get().isdigit():
            value = int(input_str.get())
        else:
            try:
                value = eval(input_str.get())
            except Exception as e:
                print(e)
                value = "Error"
        input_str.set(value)
        input_strEntry.update()
    elif text == "C":
        input_str.set("")
        input_strEntry.update()
    else:
        input_str.set(input_str.get() + text)
        input_strEntry.update()


root = Tk()
root.wm_iconbitmap("Calculator.ico")
root.title("Calculator")
root.geometry("280x420")
root.maxsize(280, 420)
root.minsize(280, 420)

input_str = StringVar()
input_strEntry = Entry(root, textvariable=input_str, font="lucida 30", relief=SUNKEN, width=12)
input_strEntry.place(x=5, y=5)

btn1 = Button(root, text='C', bg="gray", font="lucida 18", padx=13, pady=10)
btn1.place(x=10, y=70)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='/', bg="gray", font="lucida 18", padx=18, pady=10)
btn1.place(x=75, y=70)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='*', bg="gray", font="lucida 18", padx=17, pady=10)
btn1.place(x=140, y=70)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='+', bg="gray", font="lucida 18", padx=15, pady=44)
btn1.place(x=205, y=70)
btn1.bind("<Button-1>", click)


btn1 = Button(root, text='7', bg="gray", font="lucida 18", padx=15, pady=10)
btn1.place(x=10, y=138)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='8', bg="gray", font="lucida 18", padx=15, pady=10)
btn1.place(x=75, y=138)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='9', bg="gray", font="lucida 18", padx=15, pady=10)
btn1.place(x=140, y=138)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='-', bg="gray", font="lucida 18", padx=18, pady=44)
btn1.place(x=205, y=206)
btn1.bind("<Button-1>", click)

btn1 = Button(root, text='4', bg="gray", font="lucida 18", padx=15, pady=10)
btn1.place(x=10, y=206)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='5', bg="gray", font="lucida 18", padx=15, pady=10)
btn1.place(x=75, y=206)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='6', bg="gray", font="lucida 18", padx=15, pady=10)
btn1.place(x=140, y=206)
btn1.bind("<Button-1>", click)

btn1 = Button(root, text='1', bg="gray", font="lucida 18", padx=15, pady=10)
btn1.place(x=10, y=274)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='2', bg="gray", font="lucida 18", padx=15, pady=10)
btn1.place(x=75, y=274)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='3', bg="gray", font="lucida 18", padx=15, pady=10)
btn1.place(x=140, y=274)
btn1.bind("<Button-1>", click)

btn1 = Button(root, text='0', bg="gray", font="lucida 18", padx=48, pady=10)
btn1.place(x=10, y=342)
btn1.bind("<Button-1>", click)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='.', bg="gray", font="lucida 18", padx=18, pady=10)
btn1.place(x=140, y=342)
btn1.bind("<Button-1>", click)
btn1 = Button(root, text='=', bg="gray", font="lucida 18", padx=15, pady=10)
btn1.place(x=205, y=342)
btn1.bind("<Button-1>", click)

root.mainloop()
