from tkinter import *


def calculate():

    LpaVal = LPValue.get()
    answer= float(LpaVal)*100000/12

    
    
    salaryPerMonth.set(f"Montly salary is {round(answer)} ")

def clear():
     salaryPerMonth.set(" ")
     LPValue.set(" ")   
    


root = Tk()
root.geometry("655x355")
root.title("Salery tool")
root.minsize(655, 355)
root.maxsize(655, 355)

salaryInLPA = Label(root, text="Salary in LPA").pack()
LPValue = StringVar()
LPA = Entry(root, textvariable=LPValue).pack(padx=3, pady=4)

Button(root, text="Calculate", command=calculate).pack()
Button(root, text="Clear", command=clear).pack()


salaryPerMonth = StringVar()
salaryPerMonth.set("Mothly salery is ")

SPM = Label(root, textvariable=salaryPerMonth).pack(side=TOP, fill=X, pady=10)


root.mainloop()
