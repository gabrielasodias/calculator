from tkinter import *

# Display window
window = Tk()
window.title('Calculator')
window.geometry('350x500')
window.resizable(False, False)

count = []

# Number input function (add to 'count' list)
def num(number):
    number = number['text']
    if number == '÷':
        count.append('/')
        count_lab['text'] = count
    elif number == 'X':
        count.append('*')
        count_lab['text'] = count
    else:
        count.append(number)
        count_lab['text'] = count

# Calculation function
def calculation():
    global count
    try:
        count_lab['text'] = eval(str("".join(count)))
        count = []
    except:
        count_lab['text'] = 'E R R O R'
        count = []

# Function that clears the calculation from the screen
def clear():
    global conta
    count_lab['text'] = ' '
    count = []

# Interface, buttons and position
count_lab = Label(window, text = '', font = 14)
count_lab.pack(side = TOP, anchor = E)

n1 = Button (window, text = '1', width = 8, height = 4, command = lambda : num(n1))
n1.place(x = 10, y = 100)

n2 = Button (window, text = '2', width = 8, height = 4, command = lambda : num(n2))
n2.place(x = 90, y = 100)

n3 = Button (window, text = '3', width = 8, height = 4, command = lambda : num(n3))
n3.place(x = 170, y = 100)

n4 = Button (window, text = '4', width = 8, height = 4, command = lambda : num(n4))
n4.place(x = 10, y = 180)

n5 = Button (window, text = '5', width = 8, height = 4, command = lambda : num(n5))
n5.place(x = 90, y = 180)

n6 = Button (window, text = '6', width = 8, height = 4, command = lambda : num(n6))
n6.place(x = 170, y = 180)

n7 = Button (window, text = '7', width = 8, height = 4, command = lambda : num(n7))
n7.place(x = 10, y = 260)

n8 = Button (window, text = '8', width = 8, height = 4, command = lambda : num(n8))
n8.place(x = 90, y = 260)

n9 = Button (window, text = '9', width = 8, height = 4, command = lambda : num(n9))
n9.place(x = 170, y = 260)

n0 = Button (window, text = '0', width = 8, height = 4, command = lambda : num(n0))
n0.place(x = 10, y = 340)

point = Button(window, text = '.', width = 8, height = 4, command = lambda : num(point))
point.place(x = 170, y = 340)

result = Button (window, text = '=', width = 20, height = 4, fg = 'white', bg = 'red', command = calculation)
result.place(x = 170,y = 420)

cls = Button (window, text = 'C', width = 8, height = 4, fg = "white", bg = "black", command = clear)
cls.place(x = 90, y = 340)

sum = Button(window, text = '+', width = 8, height = 4, command = lambda : num(sum))
sum.place(x = 260, y = 100)

sub = Button(window, text = '-', width = 8, height = 4, command = lambda : num(sub))
sub.place(x = 260, y = 180)

mult = Button(window, text = 'X', width = 8, height = 4, command = lambda : num(mult))
mult.place(x = 260, y = 260)

div = Button(window, text = '÷', width = 8, height = 4, command = lambda : num(div))
div.place(x = 260, y = 340)

p1 = Button(window, text = '(', width = 8, height = 4, command = lambda : num(p1))
p1.place(x = 10, y = 420)

p2 = Button(window, text = ')', width = 8, height = 4, command = lambda : num(p2))
p2.place(x = 90, y = 420)

# To run the code
window.mainloop()