"""import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("GOLD BANK OF SHAILU")
root.geometry("760x540")
root.configure(bg="#F4C2C2")
root.resizable(False, False)
form = tk.Frame(root, bg="#F4C2C2", highlightbackground="#8B5E3C", highlightthickness=3)
form.place(relx=0.5, rely=0.5, anchor="center", width=690, height=455)
title = tk.Label(form, text="GOLD BANK OF SHAILU", font=("Arial", 24, "bold"), bg="#F4C2C2", fg="#7A3E00")
titleAmount to be deposit = entries["Amount to be Deposited"].get().strip()
    Amount.place(x=30, y=25, width=630, height=45)
tk.Frame(form, bg="#8B5E3C", height=2).place(x=30, y=80, width=630)
fields = [("Account No", 110),("Name", 175),("Amount", 240),("Amount to be Deposited", 305),("Amount Withdrawn", 370),]
entries = {}
for label_text, y in fields:
    label = tk.Label(form, text=label_text, font=("Arial", 13), bg="#F4C2C2", fg="#402010", anchor="w")
    label.place(x=30, y=y, width=220, height=35)
    entry = tk.Entry(form, font=("Arial", 13), bg="white", fg="#222222", relief="solid", bd=1)
    entry.place(x=260, y=y, width=390, height=35)
    entries[label_text] = entry
def submit():
    account_no = entries["Account No"].get().strip()
    name = entries["Name"].get().strip()
    Intial amount = entries["Amount"].get().strip()
     withdrawal = entries["Amount Withdrawn"].get().strip()
    if not account_no or not name:
        messagebox.showerror("Error","Please fill out at least Account No and Name!")
        return
    messagebox.showinfo(
        "GOLD BANK OF SHAILU",
        f"Account No: {account_no}\n"
        f"Name: {name}\n"
        f"Amount: {amount}\n"
        f"Amount to be Deposited: {deposit}\n"
        f"Amount Withdrawn: {withdrawal}")
submit_button = tk.Button(form, text="Submit", command=submit, font=("Arial", 12, "bold"), bg="#D4AF37", fg="#402010", activebackground="#C49A2C", relief="raised", cursor="hand2")
submit_button.place(x=275, y=415, width=140, height=30)
root.mainloop()"""


from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Login Form")
win.geometry("400x180")
win.configure(bg="pink")

def login():
    if username.get() == "shailesh2612" and password.get() == "Shailugold@2006":
        show_bank_form()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")
def depositamount():
    try:
        n1 = int(e3.get())
        n2 = int(e4.get() or 0)
        n3 = int(e5.get() or 0)
        set(n1 + n2 - n3)
        print("Account number =", e1.get())
        print("Name =", e2.get())
        print("Initial Amount =", e3.get())
        print("Amount to be deposited =", e4.get())
        print("Amount to be withdrawn =", e5.get())
    except ValueError:
        messagebox.showerror("Invalid Amount", "Enter valid whole numbers for the amounts")
def show_bank_form():
    for widget in win.winfo_children():
        widget.destroy()

    win.title("GOLD BANK OF SHAILU")
    win.geometry("400x330")

    Label(win, text="GOLD BANK OF SHAILU", font=("Arial", 16, "bold"), bg="pink").grid(row=0, column=1)

    Label(win, text="Account No", bg="pink").grid(row=1, column=0)
    global e1
    e1 = Entry(win)
    e1.grid(row=1, column=1)
    Label(win, text="Name", bg="pink").grid(row=2, column=0)
    global e2
    e2 = Entry(win)
    e2.grid(row=2, column=1)
    Label(win, text="Initial Amount", bg="pink").grid(row=3, column=0)
    global e3
    e3 = Entry(win)
    e3.grid(row=3, column=1)
    Label(win, text="Amount to be deposited", bg="pink").grid(row=4, column=0)
    global e4
    e4 = Entry(win)
    e4.grid(row=4, column=1)
    Label(win, text="Amount to be withdrawn", bg="pink").grid(row=5, column=0)
    global e5
    e5 = Entry(win)
    e5.grid(row=5, column=1)
    global S
    S = StringVar()
    Label(win, text="Final Amount", bg="pink").grid(row=6, column=0)
    Entry(win, textvariable=S, bg="yellow").grid(row=6, column=1)
    Button(win, text="Submit", command=depositamount).grid(row=7, column=1)

username = StringVar()
password = StringVar()
Label(win, text="Username", bg="red").grid(row=0, column=0)
Entry(win, textvariable=username).grid(row=0, column=1)
Label(win, text="Password", bg="yellow").grid(row=1, column=0)
Entry(win, textvariable=password, show="*").grid(row=1, column=1)
Button(win, text="Login",bg="green", command=login).grid(row=2, column=1)
win.mainloop()
