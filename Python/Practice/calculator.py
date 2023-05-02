import tkinter as tk

calculation = "" #calculation stream, i.e. the entry

def addToCalc(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end") #clears the unwanted
    text_result.insert(1.0, calculation)

def evaluateCalc(): #evaluates python statements/functions
    global calculation
    try:
        result = str(eval(calculation)) #turns the evaluation of the calculation into string
        calculation = "" # reset calculation
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clearField()
        text_result.insert(1.0, "error")

def clearField():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x275")
root.title("Calculator")

text_result = tk.Text(root, height=2, width=16, font=("Calibri", 24))
text_result.grid(columnspan=5)

btn1 = tk.Button(root, text="1", command=lambda: addToCalc(1), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
btn1.grid(row=2, column=1)

btn2 = tk.Button(root, text="2", command=lambda: addToCalc(2), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
btn2.grid(row=2, column=2)

btn3 = tk.Button(root, text="3", command=lambda: addToCalc(3), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
btn3.grid(row=2, column=3)

btn4 = tk.Button(root, text="4", command=lambda: addToCalc(4), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
btn4.grid(row=3, column=1)

btn5 = tk.Button(root, text="5", command=lambda: addToCalc(5), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
btn5.grid(row=3, column=2)

btn6 = tk.Button(root, text="6", command=lambda: addToCalc(6), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
btn6.grid(row=3, column=3)

btn7 = tk.Button(root, text="7", command=lambda: addToCalc(7), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
btn7.grid(row=4, column=1)

btn8 = tk.Button(root, text="8", command=lambda: addToCalc(8), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
btn8.grid(row=4, column=2)

btn9 = tk.Button(root, text="9", command=lambda: addToCalc(9), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
btn9.grid(row=4, column=3)

btn0 = tk.Button(root, text="0", command=lambda: addToCalc(0), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
btn0.grid(row=5, column=2)

Oparabtn = tk.Button(root, text="(", command=lambda: addToCalc("("), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
Oparabtn.grid(row=5, column=1)

Cparabtn = tk.Button(root, text=")", command=lambda: addToCalc(")"), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space. Also if the method has parameters
Cparabtn.grid(row=5, column=3)

deletebtn = tk.Button(root, text="del", command= lambda: clearField(), width=5, font="Calibri")
deletebtn.grid(row=6, column=1)

eqbtn = tk.Button(root, text="=", command= evaluateCalc, width=5, font="Calibri")
eqbtn.grid(row=6, column=4)

Pbtn = tk.Button(root, text="+", command=lambda: addToCalc("+"), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
Pbtn.grid(row=2, column=4)

Sbtn = tk.Button(root, text="-", command=lambda: addToCalc("-"), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
Sbtn.grid(row=3, column=4)

Dbtn = tk.Button(root, text="/", command=lambda: addToCalc("/"), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
Dbtn.grid(row=4, column=4)

Mbtn = tk.Button(root, text="*", command=lambda: addToCalc("*"), width=5, font="Calibri") #lambda creates hidden functions that are only used a few times and doesn't take up too much space
Mbtn.grid(row=5, column=4)

root.mainloop()
