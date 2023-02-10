from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def get_value():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops!', message='You have left some empty fields')
    else:
        is_ok = messagebox.askokcancel(title=web, message=f'These are the details entered:\n '
                                                 f'Email: {email} \n Password: {password} \n Is it ok to save?')
        if is_ok:
            with open('saved_password.txt', 'a') as saved_password:
                saved_password.write(f'{web}| {email}| {password}\n')
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='White')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_text = Label(text="Website:", bg='white', fg='black')
website_text.grid(row=2, column=0)
website_entry = Entry(width=35, bg='white')
website_entry.focus()
website_entry.grid(row=2, column=1, columnspan=2)

Email_text = Label(text="Email/Username:", bg='white', fg='black')
Email_text.grid(row=3, column=0)
email_entry = Entry(width=35, bg='white', fg='black')
email_entry.insert(0, 'sample@gmail.com')
email_entry.grid(row=3, column=1, columnspan=2)

password_text = Label(text="Password:", bg='white', fg='black')
password_text.grid(row=4, column=0)
password_entry = Entry(width=21, bg='white', fg='black')
password_entry.grid(row=4, column=1, columnspan=1)

generate_password_button = Button(text='Generate Password', width=10, command=generate_password)
generate_password_button.grid(row=4, column=2)

add_button = Button(text='Add', width=34, command=get_value)
add_button.grid(row=5, column=1, columnspan=2)


window.mainloop()


