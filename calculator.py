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

count_lab = Label(window, text = '', font = 14)
count_lab.pack(side = TOP, anchor = E)

window.mainloop()