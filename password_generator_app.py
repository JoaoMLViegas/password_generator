from tkinter import*
import random

# ASCII TABLE CONSTANTS

ASCII_DIGIT_ZERO = 48
ASCII_DIGIT_NINE = 57
ASCII_CHAR_A = 65
ASCII_CHAR_Z = 90
ASCII_CHAR_a = 97
ASCII_CHAR_z = 122


root = Tk()
root.title("Password Generator")
root.resizable(False, False)


def copy():
    root.clipboard_append(display.cget("text"))

def generate():
    global display

    special_characters = []
    for i in range(33, 47): special_characters.append(i)
    for i in range(58, 64): special_characters.append(i)
    for i in range(91, 96): special_characters.append(i)
    for i in range(123, 126): special_characters.append(i)

    num = num_characters.get()

    password = ""
    for i in range(num):
        case = random.randint(0, 3)

        if case == 0:  # upper letter case
            password += chr(random.randint(ASCII_CHAR_A, ASCII_CHAR_Z))
        elif case == 1:  # lower letter case
            password += chr(random.randint(ASCII_CHAR_a, ASCII_CHAR_z))
        elif case == 2:  # digits case
            password += chr(random.randint(ASCII_DIGIT_ZERO, ASCII_DIGIT_NINE))
        else:  # special character letter case
            password += chr(random.choice(special_characters))

    display = Label(root, text=password, width=30, relief=GROOVE)
    display.grid(row=0, column=0, columnspan=2, padx=40, pady=10)


init_display = Label(root, width=30, relief=GROOVE)
init_display.grid(row=0, column=0, columnspan=2, padx=40, pady=10)

b = Button(root, text="Generate", width=10, command=generate)
b.grid(row=1, column=0, padx=10, pady=10)

c = Button(root, text="Copy", width=10, command=copy)
c.grid(row=1, column=1, padx=10, pady=10)

info_on_slider = Label(root, text="Choose the number os characters for the password:")
info_on_slider.grid(row=2, column=0, columnspan=2, padx=10)

num_characters = Scale(root, from_=1, to=24, orient=HORIZONTAL)
num_characters.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
