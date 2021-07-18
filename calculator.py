import tkinter as tk
from tkinter.constants import END

# screen
window = tk.Tk()
window.title("Calculator")
window.iconbitmap("calculator.ico")

# place to type in
enter = tk.Entry(window, width = 45, borderwidth = 10)
enter.grid(row = 0, column = 0, columnspan = 3)

# print number in thing function
def button_clicked(number):
    get = enter.get()
    enter.delete(0, END)
    enter.insert(0, get + str(number))

def addition():
    global num1
    global math 

    math = "add"
    num1 = enter.get()
    
    enter.delete(0, END)

def subtract():
    global num1
    global math

    math = "subtract"
    num1 = enter.get()
    
    enter.delete(0, END)

def multiply():
    global num1 
    global math

    math = "multiply"
    num1 = enter.get()
    
    enter.delete(0, END)

def divide():
    global num1
    global math

    math = "divide"
    num1 = enter.get()
    
    enter.delete(0, END)

def equals():
    num2 = enter.get()
    enter.delete(0, END)
    if math == "add":
        enter.insert(0, int(num1) + int(num2))
    
    elif math == "subtract":
        enter.insert(0, int(num1) - int(num2))

    elif math == "multiply":
        enter.insert(0, int(num1) * int(num2))

    elif math == "divide":
        enter.insert(0, int(int(num1) / int(num2)))


# buttons
button1 = tk.Button(window, text = "1", padx=40, pady=20, command= lambda: button_clicked(1))
button2 = tk.Button(window, text = "2", padx=40, pady=20, command= lambda: button_clicked(2))
button3 = tk.Button(window, text = "3", padx=40, pady=20, command= lambda: button_clicked(3))
button4 = tk.Button(window, text = "4", padx=40, pady=20, command= lambda: button_clicked(4))
button5 = tk.Button(window, text = "5", padx=40, pady=20, command= lambda: button_clicked(5))
button6 = tk.Button(window, text = "6", padx=40, pady=20, command= lambda: button_clicked(6))
button7 = tk.Button(window, text = "7", padx=40, pady=20, command= lambda: button_clicked(7))
button8 = tk.Button(window, text = "8", padx=40, pady=20, command= lambda: button_clicked(8))
button9 = tk.Button(window, text = "9", padx=40, pady=20, command= lambda: button_clicked(9))
button0 = tk.Button(window, text = "0", padx=40, pady=20, command= lambda: button_clicked(0))

button_plus = tk.Button(window, text = "+", padx=40, pady=20, command = addition)
button_sub = tk.Button(window, text = "-", padx=40, pady=20, command = subtract)
button_multi = tk.Button(window, text = "*", padx=40, pady=20, command = multiply)
button_div = tk.Button(window, text = "/", padx=40, pady=20, command = divide)
button_equals = tk.Button(window, text = "=", padx=40, pady=20, command = equals)

# place the button in window
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button_plus.grid(row=4, column=0)
button0.grid(row=4, column=1)
button_equals.grid(row=4, column=2)

button_sub.grid(row=5, column=0)
button_multi.grid(row=5, column=1)
button_div.grid(row=5, column=2)

window.mainloop()
