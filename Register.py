from tkinter import *
import tkinter as tk 
from tkinter import messagebox
import ast

window = tk.Tk()
window.title("Registrasi")
window.geometry('925x500')
window.configure(bg="#C8E8F5")
window.resizable(False,False)

def registrasi():
    namapengguna = user.get()
    katakunci = code.get()
    konfirmasikatku = confirm.get()

    if katakunci == konfirmasikatku:
        try:
            file = open('databest.txt', 'r+')
            baca = file.read()
            r = ast.literal_eval(baca)

            dict2 = {namapengguna: katakunci}
            r.update(dict2)
            file.seek(0)  # Move the cursor to the beginning of the file
            file.write(str(r))
            file.truncate()  # Truncate the file to the current position
            file.close()

            messagebox.showinfo('Signup', 'Registrasi berhasil')

        except:
            file = open('databest.txt', 'w')
            tulis = str({namapengguna: katakunci})
            file.write(tulis)
            file.close()
    else:
        messagebox.showerror('Invalid', 'Kedua password tidak sama')

def sign():
    window.destroy()

img = PhotoImage(file = 'Register.png')
img = img.subsample(2, 2)
Label(window,image=img, bg='white', bd = 0).place(x=-15,y=-20)

frame = Frame(window, width = 320, height = 360, bg="#C8E8F5")
frame.place(x=580, y=70)

heading = Label(frame, text = 'Registrasi', fg='black', bg='#C8E8F5', font=('Microsoft YaHei UI Light', 23,'bold'))
heading.place(x = 90, y = 5)
# Nama pengguna
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name =='':
        user.insert(0,'Nama Pengguna')
user = Entry(frame, width=25, fg='black', border =0, bg='#C8E8F5', font=('Microsoft YaHei UI Light',11))
user.place(x=67, y=70)
user.insert(0,"Nama Pengguna")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=250,height=3,bg='white').place(x=55,y=107)
# Password
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    kata=code.get()
    if kata =='':
        code.insert(0,'Kata Kunci')
code = Entry(frame, width=25, fg='black', border =0, bg='#C8E8F5', font=('Microsoft YaHei UI Light',11))
code.place(x=67, y=150)
code.insert(0,'Kata Kunci')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=250,height=3,bg='white').place(x=55,y=187)
# Konfirmasi kata kunci
def on_enter(e):
    confirm.delete(0,'end')

def on_leave(e):
    kata=confirm.get()
    if kata =='':
        confirm.insert(0,'Konfirmasi Kata Kanci')
confirm = Entry(frame, width=25, fg='black', border =0, bg='#C8E8F5', font=('Microsoft YaHei UI Light',11))
confirm.place(x=67, y=230)
confirm.insert(0,'Konfirmasi Kata Kunci')
confirm.bind('<FocusIn>', on_enter)
confirm.bind('<FocusOut>', on_leave)

Frame(frame,width=250,height=3,bg='white').place(x=55,y=267)

Button(frame, width=35, pady =1, text='Registrasi',bg='white', border = 0, command = registrasi).place(x = 55,y=285)
label=Label(frame, text="Sudah memiliki akun?",fg='black',bg='#C8E8F5',font=('Microsoft YaHei UI Light',9))
label.place(x=85,y=315)

sign_in = Button(frame, width=6, text='Masuk', border=0, bg='#C8E8F5', cursor='hand2', fg='#FEB13D', command = sign )
sign_in.place(x=212,y=317)

window.mainloop()