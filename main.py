from tkinter import ttk, Tk, StringVar, IntVar
import random


def only_digits(char):
    return char.isdigit() or char == ""

def think_number():
    return random.randint(1, 10)

def check(event=False):
    try:
        if unknown_number.get() == "****":
            if random_number.get() == answer.get():
                style.configure("Custom.TSpinbox", fieldbackground="green")
                count.set(count.get() + 1)
            else:
                style.configure("Custom.TSpinbox", fieldbackground='red')
            unknown_number.set(str(random_number.get()))
            root.after(2000, new_step)
        else:
            pass
    except:
        print("Ошибка!")

def new_step():
    random_number.set(think_number())
    unknown_number.set("****")
    answer.set(1)
    style.configure("Custom.TSpinbox", fieldbackground='white')


root = Tk()
vcmd = (root.register(only_digits), '%P')
root.geometry("400x300+600+250")
root.title("Угадай число")
root.resizable(False, False)

style = ttk.Style()
style.theme_use('clam')
style.configure('Custom.TFrame', relief='sunken')
style.configure('Custom.TLabel', font=("Times New Roman", 12))
style.configure("Custom.TSpinbox", fieldbackground="white")

frame1 = ttk.Frame(root, border=10, style='Custom.TFrame')
frame1.place(relx=0.5, relwidth=0.9, rely=0.25, relheight=0.4, anchor="center")

frame2 = ttk.Frame(root, border=10, style='Custom.TFrame')
frame2.place(relx=0.3, relwidth=0.5, rely=0.74, relheight=0.4, anchor="center")

frame3 = ttk.Frame(root, border=10, style='Custom.TFrame')
frame3.place(relx=0.8, relwidth=0.3, rely=0.74, relheight=0.4, anchor="center")


unknown_number = StringVar(value="****")
answer = IntVar(value=1)
random_number = IntVar(value=think_number())
count = IntVar(value=0)

label11 = ttk.Label(frame1, text='ТАИНСТВЕННОЕ ЧИСЛО', style="Custom.TLabel", anchor="center", foreground="red")
label11.place(relx=0.5, relwidth=1, rely=0.2, anchor="center")
label12 = ttk.Label(frame1, textvariable=unknown_number, style="Custom.TLabel", anchor="center",)
label12.place(relx=0.5, relwidth=1, rely=0.6, anchor="center")
label14 = ttk.Label(frame1, textvariable=count, style="Custom.TLabel", anchor="center", foreground="blue")
label14.place(relx=0.1, relwidth=0.1, rely=0.2, anchor="center")

label21 = ttk.Label(frame2, text='Введите предположение', style="Custom.TLabel", anchor="center", foreground="blue")
label21.place(relx=0.5, relwidth=1, rely=0.2, anchor="center")
spin22 = ttk.Spinbox(frame2, from_=1, to=10, width=20, textvariable=answer, style="Custom.TSpinbox", state="readonly", wrap=True)
spin22.place(relx=0.5, rely=0.6, anchor="center")

button31 = ttk.Button(frame3, text='Проверить', command=check)
button31.pack(fill="both", expand=True)

spin22.bind('<Return>', check)

def clear_focus(event):
    event.widget.selection_clear()
    root.focus()

spin22.bind("<FocusIn>", clear_focus)
button31.bind("<FocusIn>", clear_focus)

root.mainloop()