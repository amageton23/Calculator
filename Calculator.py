from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    eqution.set(expression)

def pressEqual():
    try: 
        global expression

        total = str(eval (expression))

        equation.set(total)

        expression = ""

    except: 
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def __name__ == "__main__"
    gui = Tk()

    gui.configure(background = "gray3")

    gui.geometry("300x500")

    equation = StringVar()

    expression_field = Entry(gui,textvariable=equation)

    expression_field.grid(columnspan=4, ipadx = 70)






