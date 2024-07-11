from tkinter import *
from functools import partial
import keyboard

buttonHeight = 3
buttonWidth = 4

root = Tk()

# sukuriam langa
root.title("Skaičiuotuvas")
root.geometry("300x280")
root['pady'] = 5
root['padx'] = 5
# rasom remus
frame1 = LabelFrame(root, borderwidth=0, highlightthickness=0)
frame1.grid(column=0, row=0)
frame2 = LabelFrame(root, borderwidth=0, highlightthickness=0)
frame2.grid(column=0, row=1)
# irasom dalykus
equation = Entry(frame1, width = 30)
equation.grid(column=0, row=0)

# lygu zenklas
lbl1 = Label(frame1, text = "=")
lbl1.grid(column=1, row=0)

# atsakymo laukas
answer = Entry(frame1, width = 10)
answer.grid(column=2, row=0)

# mygtuko lygu dalykas
def equal():
    txt = equation.get()
    #print(txt)
    result = eval(txt)
    answer.delete(0, END)
    answer.insert(0, str(result))

# skaiciu mygtuku dalykai
def skaiciai(dalykas):
    equation.insert(END, dalykas)
# delete dalykas
def istrinti():
    tempTXT = equation.get()[:-1]
    equation.delete(0, END)
    equation.insert(0, tempTXT)

# veiksmu mygtukai
eql = Button(frame2, text = "=", command = equal, height=buttonHeight, width=buttonWidth)
eql.grid(column=2, row=3)
plus = Button(frame2, text = "+", command=partial(skaiciai, "+"), height=buttonHeight, width=buttonWidth)
plus.grid(column=3, row=0)
minus = Button(frame2, text = "-", command=partial(skaiciai, "-"), height=buttonHeight, width=buttonWidth)
minus.grid(column=3, row=1)
multiply = Button(frame2, text = "*", command=partial(skaiciai, "*"), height=buttonHeight, width=buttonWidth)
multiply.grid(column=3, row=2)
divide = Button(frame2, text = "/", command=partial(skaiciai, "/"), height=buttonHeight, width=buttonWidth)
divide.grid(column=3, row=3)
point = Button(frame2, text = ".", command=partial(skaiciai, "."), height=buttonHeight, width=buttonWidth)
point.grid(column=0, row=3)
delete = Button(frame2, text = "DEL", command=istrinti, height=buttonHeight, width=buttonWidth)
delete.grid(column=4, row=0)
angleBracketOpen = Button(frame2, text = "(", command=partial(skaiciai, "("), height=buttonHeight, width=buttonWidth)
angleBracketOpen.grid(column=4, row=1)
angleBracketClose = Button(frame2, text = ")", command=partial(skaiciai, ")"), height=buttonHeight, width=buttonWidth)
angleBracketClose.grid(column=4, row=2)


# skaiciu mygtukai
septini = Button(frame2, text="7", command=partial(skaiciai,"7"), height=buttonHeight, width=buttonWidth)
septini.grid(column=0, row=0)
astuoni = Button(frame2, text="8", command=partial(skaiciai,"8"), height=buttonHeight, width=buttonWidth)
astuoni.grid(column=1, row=0)
devini = Button(frame2, text="9", command=partial(skaiciai,"9"), height=buttonHeight, width=buttonWidth)
devini.grid(column=2, row=0)
keturi = Button(frame2, text="4", command=partial(skaiciai,"4"), height=buttonHeight, width=buttonWidth)
keturi.grid(column=0, row=1)
penki = Button(frame2, text="5", command=partial(skaiciai,"5"), height=buttonHeight, width=buttonWidth)
penki.grid(column=1, row=1)
sesi = Button(frame2, text="6", command=partial(skaiciai,"6"), height=buttonHeight, width=buttonWidth)
sesi.grid(column=2, row=1)
vienas = Button(frame2, text="1", command=partial(skaiciai,"1"), height=buttonHeight, width=buttonWidth)
vienas.grid(column=0, row=2)
du = Button(frame2, text="2", command=partial(skaiciai,"2"), height=buttonHeight, width=buttonWidth)
du.grid(column=1, row=2)
trys = Button(frame2, text="3", command=partial(skaiciai,"3"), height=buttonHeight, width=buttonWidth)
trys.grid(column=2, row=2)
nulis = Button(frame2, text="0", command=partial(skaiciai,"0"), height=buttonHeight, width=buttonWidth)
nulis.grid(column=1, row=3)

# padarom, kad enter veiktu kaip lygu
keyboard.add_hotkey('enter', equal)

root.mainloop()