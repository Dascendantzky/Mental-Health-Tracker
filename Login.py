from tkinter import *
import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk


window = tk.Tk()
window.configure(bg="#F8F1C7")
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry(f"{width}x{height}")
window.resizable(False,False)
window.title('Login')

def masuk():
    namapengguna=user.get()
    katakunci=code.get()

    if namapengguna =='admin' and katakunci=='1234':
        screen = Toplevel(window)
        screen.title("App")
        screen.geometry('925x500')
        screen.configure(bg="#C8E8F5")
        screen.resizable(False,False)
        label = Label(screen,text = 'Lets Go!!!', bg='#C8E8F5', font =('Calibri(Body)',50,'bold'))
        label.pack(expand=True)

        screen.mainloop()

    elif namapengguna != 'admin' and katakunci != '1234':
        messagebox.showerror("Invalid","Nama pengguna dan Kata kunci salah")
    elif namapengguna != 'admin' and katakunci == '1234':
        messagebox.showerror("Invalid","Nama pengguna salah")
    elif namapengguna == 'admin' and katakunci != '1234':
        messagebox.showerror("Invalid","Kata kunci salah")

img_bg_login= Image.open('login jernih.png')
img_rentang2 = img_bg_login.resize((1550, 870))  
photo_bg_login = ImageTk.PhotoImage(img_rentang2)

label_img1_login = tk.Label(window, image=photo_bg_login, bg='white', bd=0)
label_img1_login.place(x=0, y=0)

# window = Frame(window, width = 320, height = 360, bg="#F8F1C7")
# frame.place(x=580, y=400)

# heading = Label(window, text = '', fg='black', bg='#F8F1C7', font=('Microsoft YaHei UI Light', 23,'bold'))
# heading.place(x = 580, y = 400)

# Buat tempat input nama pengguna
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name =='':
        user.insert(0,'Username')
user = Entry(window, width=25, fg='black', border =0, bg='#F8F1C7', font=('Microsoft YaHei UI Light',11))
user.place(x=630, y=470)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

# Frame(window,width=250,height=3,bg='white').place(x=55,y=107)
# Buat tempat input password
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    kata=code.get()
    if kata =='':
        code.insert(0,'Password')
code = Entry(window, width=25, fg='black', border =0, bg='#F8F1C7', font=('Microsoft YaHei UI Light',11))
code.place(x= 630, y=560)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

# Frame(window,width=250,height=3,bg='white').place(x=55,y=187)

# Tombol button
Button(window, width=15, pady =1, text='Login',bg='#B6B4C6', border = 0, command = masuk, font = ("Arial", 14, "bold"), activebackground= "#B6B4C6" ).place(x = 694,y=625)
label=Label(window, text="Belum memiliki akun?",fg='black',bg='#F8F1C7',font=('Microsoft YaHei UI Light',9))
label.place(x=690,y=675)

sign_up = Button(window, width=6, text='Registrasi', border=0, bg='#F8F1C7', cursor='hand2', fg='#FEB13D' )
sign_up.place(x=830,y=675)

window.mainloop()


