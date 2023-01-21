from tkinter import *
expression =" "
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=" "
    except:
        equation.set("error")
        expression=" "
def clear():
    global expression
    expression =" "
    equation.set(" ")

if __name__=="__main__":
    win=Tk()
    win.configure(background="grey")
    win.title("calculator")
    win.geometry("450x400")
    equation=StringVar()
    expression_field=Entry(win,textvariable=equation, font=("Arial", 22))
    expression_field.grid(columnspan=4, padx=10, pady=10)
    btn1=Button(win, text="1", fg="black", font=("arial", 10) ,bg= "white", command=lambda: press(1), height=2, width=10)
    btn2 = Button(win, text="2", fg="black", font=("arial", 10),bg="white", command=lambda: press(2), height=2, width=10)
    btn3 = Button(win, text="3", fg="black", font=("arial", 10),bg="white", command=lambda: press(3), height=2, width=10)
    btn4 = Button(win, text="4", fg="black", font=("arial", 10),bg="white", command=lambda: press(4), height=2, width=10)
    btn5 = Button(win, text="5", fg="black", font=("arial", 10),bg="white", command=lambda: press(5), height=2, width=10)
    btn6 = Button(win, text="6", fg="black", font=("arial", 10),bg="white", command=lambda: press(6), height=2, width=10)
    btn7 = Button(win, text="7", fg="black", font=("arial", 10),bg="white", command=lambda: press(7), height=2, width=10)
    btn8 = Button(win, text="8", fg="black", font=("arial", 10),bg="white", command=lambda: press(8), height=2, width=10)
    btn9 = Button(win, text="9", fg="black", font=("arial", 10),bg="white", command=lambda: press(9), height=2, width=10)
    btn10 =Button(win, text="+", fg="black", font=("arial", 10),bg="white", command=lambda: press("+"), height=2, width=10)
    btn11= Button(win, text="-", fg="black", font=("arial", 10),bg="white", command=lambda: press("-"), height=2, width=10)
    btn12= Button(win, text="*", fg="black", font=("arial", 10),bg="white", command=lambda: press("*"), height=2, width=10)
    btn13= Button(win, text="/", fg="black", font=("arial", 10),bg="white", command=lambda: press("/"), height=2, width=10)
    btn14= Button(win, text="0", fg="black", font=("arial", 10),bg="white", command=lambda: press(0), height=2, width=10)
    btn15= Button(win, text=".", fg="black", font=("arial", 10),bg="white", command=lambda: press("."), height=2, width=10)
    btn16= Button(win, text="clear", fg="black", font=("arial",10), bg="white", command=clear, height=2, width=10)
    btn17 = Button(win, text="=", fg="black", font=("arial", 10), bg="white", command=equalpress, height=2, width=10)




    btn1.grid(row=2, column=0, padx=10, pady=10)
    btn2.grid(row=2, column=1, padx=10, pady=10)
    btn3.grid(row=2, column=2, padx=10, pady=10)
    btn4.grid(row=2, column=3, padx=10, pady=10)
    btn5.grid(row=3, column=0, padx=10, pady=10)
    btn6.grid(row=3, column=1, padx=10, pady=10)
    btn7.grid(row=3, column=2, padx=10, pady=10)
    btn8.grid(row=3, column=3, padx=10, pady=10)
    btn9.grid(row=4, column=0, padx=10, pady=10)
    btn10.grid(row=4, column=1, padx=10, pady=10)
    btn11.grid(row=4,column=2, padx=10, pady=10)
    btn12.grid(row=4, column=3, padx=10, pady=10)
    btn13.grid(row=5, column=0, padx=10, pady=10)
    btn14.grid(row=5, column=1, padx=10, pady=10)
    btn15.grid(row=5, column=2, padx=10, pady=10)
    btn16.grid(row=5, column=3, padx=10, pady=10)
    btn17.grid(row=6, columnspan=4, padx=10, pady=10)

    n_rows=6
    n_col=4
    for i in range(6):
        win.grid_rowconfigure(i, weight=1)
    for i in range(4):
        win.grid_columnconfigure(i, weight=1)
    win.mainloop()