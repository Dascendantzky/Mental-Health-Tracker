from tkinter import *
import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk
import ast
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
# import speech_recognition
total_yes = 0
total_no = 0
pertanyaan_index = 0
total_skor_intro = 0
pertanyaan_index_intro = 0
total_skor_ekstro = 0
pertanyaan_index_ekstro = 0

window_loop = tk.Tk()
window_loop.configure(bg="#C8E8F5")
width, height = window_loop.winfo_screenwidth(), window_loop.winfo_screenheight()
window_loop.geometry(f"{width}x{height}")
window_loop.resizable(False,False)
window_loop.title('Login')

# Code masuk ke halaman pertama
def masuk():
    namapengguna=user.get()
    katakunci=code.get()
    file = open('databest.txt','r')
    baca = file.read()
    r = ast.literal_eval(baca)
    file.close()
    print(r.keys())
    print(r.values())
    window_loop.destroy()

    if namapengguna in r.keys() and katakunci==r[namapengguna]:

        hal1 = tk.Tk()
        width, height = hal1.winfo_screenwidth(), hal1.winfo_screenheight()
        hal1.geometry(f"{width}x{height}")
        hal1.configure(bg="#C8E8F5")
        hal1.resizable(False, False)
        hal1.title('Main Page')

        img_hal1 = Image.open('Main page.png')
        img_hal = img_hal1.resize((1550,850))
        photo_bg_login = ImageTk.PhotoImage(img_hal)

        label_img1_login = tk.Label(hal1, image=photo_bg_login, bg='white', bd=0)
        label_img1_login.place(x=0, y=0)

        # Gambar 1 dan masuk ke menu alur
        def alur():
            hal2_alur= tk.Toplevel(hal1)
            hal2_alur.title("Registrasi")
            width, height = hal2_alur.winfo_screenwidth(), hal2_alur.winfo_screenheight()
            hal2_alur.geometry(f"{width}x{height}")
            hal2_alur.configure(bg="#C8E8F5")
            hal2_alur.resizable(False,False)
            hal2_alur.title("Alur dan Petunjuk")

            img_alur = Image.open('desain alur.png')
            img_bg_alur = img_alur.resize((1550,850))
            photo_bg_alur = ImageTk.PhotoImage(img_bg_alur)
            label_img_alur = tk.Label(hal2_alur, image=photo_bg_alur, bg='white', bd=0)
            label_img_alur.place(x=0, y=0)
            def back():
                hal2_alur.destroy()

                # Tombol back sementara
            kembali = tk.Button (hal2_alur, text ="Kembali", font=('Arial', 12),  bg ="#B6B4C6", fg = "black", border= 0, command = back )
            kembali.place(x= 1410, y= 36)  

            def test():
                hal3_test= tk.Toplevel(hal1)
                hal3_test.title("Registrasi")
                width, height = hal3_test.winfo_screenwidth(), hal3_test.winfo_screenheight()
                hal3_test.geometry(f"{width}x{height}")
                hal3_test.configure(bg="white")
                hal3_test.resizable(False,False)
    # PDF KUNCI
                nama_pengguna_var = tk.StringVar()

                def mulai():
                    hal3_test.destroy()
                    tes_kepribadian = tk.Toplevel(hal1)
                    tes_kepribadian.title("Mental Health Tracker")
                    width, height = tes_kepribadian.winfo_screenwidth(), tes_kepribadian.winfo_screenheight()
                    tes_kepribadian.geometry(f"{width}x{height}")
                    tes_kepribadian.configure(bg="white")
                    tes_kepribadian.resizable(False, False)

                    def hasil_kepribadian(tingkat_stres):
                        tes_kepribadian.destroy()
                        hasil_tes_kepribadian = tk.Toplevel(hal1)
                        hasil_tes_kepribadian.title("Hasil dan Rekomendasi")
                        width, height = hasil_tes_kepribadian.winfo_screenwidth(), hasil_tes_kepribadian.winfo_screenheight()
                        hasil_tes_kepribadian.geometry(f"{width}x{height}")
                        hasil_tes_kepribadian.resizable(False, False)

                        def tes_mental():
                            hasil_tes_kepribadian.destroy()
                            halaman_tes_mental = tk.Toplevel(hal1)
                            halaman_tes_mental.title("Mental Health Test")
                            width, height = halaman_tes_mental.winfo_screenwidth(), halaman_tes_mental.winfo_screenheight()
                            halaman_tes_mental.geometry(f"{width}x{height}")
                            halaman_tes_mental.resizable(False, False)

                        #  Awal tes kesehatan mental introvert
                            def mental_introvert():
                                halaman_tes_mental.destroy()
                                tes_kesehatan_mental_intro = tk.Toplevel(hal1)
                                tes_kesehatan_mental_intro.title("Mental Health Tracker")
                                width, height = tes_kesehatan_mental_intro.winfo_screenwidth(), tes_kesehatan_mental_intro.winfo_screenheight()
                                tes_kesehatan_mental_intro.geometry(f"{width}x{height}")
                                tes_kesehatan_mental_intro.configure(bg="white")
                                tes_kesehatan_mental_intro.resizable(False,False)

                                img_mental_intro = Image.open('desain tes mental.png')
                                img_bg_mental_intro = img_mental_intro.resize((1550,850), Image.Resampling.BICUBIC)
                                photo_mental_intro =ImageTk.PhotoImage(img_bg_mental_intro)

                                label_mental_intro = tk.Label(tes_kesehatan_mental_intro, image=photo_mental_intro, bg='white', bd=0)
                                label_mental_intro.place(x=0, y=0)
                                
                                # Def rekomendasi bisa diisi rekomendasinya pake label
                                def hasil_rekomendasi_intro(tingkat_stres):
                                    tes_kesehatan_mental_intro.destroy()
                                    hasil_jendela = tk.Toplevel(hal1)
                                    hasil_jendela.title("Hasil dan Rekomendasi")
                                    width, height = hasil_jendela.winfo_screenwidth(), hasil_jendela.winfo_screenheight()
                                    hasil_jendela.geometry(f"{width}x{height}")
                                    hasil_jendela.resizable(False,False)
                                    def tutup2():
                                        hasil_jendela.destroy()

                                    def pin():
                                        messagebox.showinfo("Save","PDF tersimpan")

                                    if tingkat_stres <= 20:
                                        img_hasil_intro1 = Image.open('desain hijau.png')
                                        img_bg_hasil_intro1 = img_hasil_intro1.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_intro1 =ImageTk.PhotoImage(img_bg_hasil_intro1)

                                        label_hasil_intro1 = tk.Label(hasil_jendela, image=photo_hasil_intro1, bg='white', bd=0)
                                        label_hasil_intro1.place(x=0, y=0)

                                        hasil_label_intro1 = tk.Label(hasil_jendela, text=f"{tingkat_stres}%", font = ("Arial", 22, "bold"), bg = "#7DFB48")
                                        hasil_label_intro1.pack(pady=216, padx=215)

                                        label_hal1 = tk.Button(hasil_jendela, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup2, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal1.place(x= 66, y=52)

                                        label_save1 = tk.Button(hasil_jendela, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save1.place(x=688, y=728)

                                    elif 20 < tingkat_stres <= 50:
                                        img_hasil_intro2 = Image.open('desain kuning.png')
                                        img_bg_hasil_intro2 = img_hasil_intro2.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_intro2 =ImageTk.PhotoImage(img_bg_hasil_intro2)

                                        label_hasil_intro2 = tk.Label(hasil_jendela, image=photo_hasil_intro2, bg='white', bd=0)
                                        label_hasil_intro2.place(x=0, y=0)

                                        hasil_label_intro2 = tk.Label(hasil_jendela, text=f"{tingkat_stres}%", font = ("Arial", 22, "bold"), bg="#F7D54B")
                                        hasil_label_intro2.pack(pady=216, padx=215)

                                        label_hal2 = tk.Button(hasil_jendela, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup2, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal2.place(x= 66, y=52)

                                        label_save2 = tk.Button(hasil_jendela, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save2.place(x=688, y=728)

                                    elif 50 < tingkat_stres <= 80:
                                        img_hasil_intro3 = Image.open('desain orange.png')
                                        img_bg_hasil_intro3 = img_hasil_intro3.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_intro3 =ImageTk.PhotoImage(img_bg_hasil_intro3)

                                        label_hasil_intro3 = tk.Label(hasil_jendela, image=photo_hasil_intro3, bg='white', bd=0)
                                        label_hasil_intro3.place(x=0, y=0)

                                        hasil_label_intro3 = tk.Label(hasil_jendela, text=f"{tingkat_stres}%", font = ("Arial", 22, "bold"), bg ="#E09645")
                                        hasil_label_intro3.pack(pady=216, padx=215)

                                        label_hal3 = tk.Button(hasil_jendela, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup2, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal3.place(x= 66, y=52)

                                        label_save3 = tk.Button(hasil_jendela, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save3.place(x=688, y=728)

                                    else:
                                        img_hasil_intro4 = Image.open('desain merah.png')
                                        img_bg_hasil_intro4 = img_hasil_intro4.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_intro4 =ImageTk.PhotoImage(img_bg_hasil_intro4)

                                        label_hasil_intro4 = tk.Label(hasil_jendela, image=photo_hasil_intro4, bg='white', bd=0)
                                        label_hasil_intro4.place(x=0, y=0)

                                        hasil_label_intro4 = tk.Label(hasil_jendela, text=f"{tingkat_stres}%", font = ("Arial", 22, "bold"), bg = "#FC7A65")
                                        hasil_label_intro4.pack(pady=216, padx=215)

                                        label_hal4 = tk.Button(hasil_jendela, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup2, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal4.place(x= 66, y=52)

                                        label_save4 = tk.Button(hasil_jendela, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save4.place(x=688, y=728)
                                    save_to_pdf(tingkat_stres)
                                    hasil_jendela.mainloop()
                                    
    # KUNCI PDF
                                def save_to_pdf(tingkat_stres):
                                    pdf_filename = "hasil_introvert.pdf"

                                    nama_pengguna = nama_pengguna_var.get()

                                    c = canvas.Canvas(pdf_filename, pagesize=(1060, 630))
                                    c.setFont("Helvetica-Bold", 30)

                                    img_path = 'introvert.png'
                                    c.drawImage(img_path, 0, 0,width=1060, height=630) 
                                    c.drawString(67, 287, f"{tingkat_stres}%")

                                    c.drawString(67, 452, f"{nama_pengguna}")
                                    
                                    c.save()


                                pertanyaan_index_intro = 0
                                pertanyaan_intro = [
                                        "1. Seberapa sering Anda merasa cemas atau stress saat berada di lingkungan sosial yang ramai? ",
                                        "2. Seberapa sering Anda merasa sedih dan tak berdaya? ",
                                        "3. Seberapa sering Anda mengalami gangguan makan seperti tidak nafsu makan? ",
                                        "4. Seberapa sering Anda merasa overthinking dalam kegiatan sehari-hari? ",
                                        "5. Seberapa sering Anda merasa tertekan dengan keadaan sosial yang terjadi di sekitar Anda? ",
                                        "6. Seberapa sering Anda tidak bisa tidur atau insomnia? ",
                                        "7. Seberapa sering Anda merasa ingin melukai diri sendiri? ",
                                        "8. Seberapa sering Anda ingin mengkritisi diri sendiri? ",
                                        "9. Seberapa sering Anda ingin mengisolasi diri dari dunia luar? ",
                                        "10. Seberapa sering Anda merasa ketakutan dan ingin mengakhiri hidup? "
                                ]
                                def kembali_intro():
                                    global pertanyaan_index_intro
                                    if pertanyaan_index_intro > 0:
                                        pertanyaan_index_intro -= 1
                                        label_pertanyaan.config(text=pertanyaan_intro[pertanyaan_index_intro])

                                def selanjutnya():
                                    global pertanyaan_index_intro, total_skor_intro
                                    skor_pertanyaan = skala_var.get()
                                    total_skor_intro += skor_pertanyaan

                                    # Pindah ke pertanyaan berikutnya
                                    pertanyaan_index_intro += 1

                                    if pertanyaan_index_intro < len(pertanyaan_intro):
                                        label_pertanyaan.config(text=pertanyaan_intro[pertanyaan_index_intro])
                                        skala_var.set(1.0)  # Reset nilai slider ke default
                                        if pertanyaan_index_intro == len(pertanyaan_intro) - 1:
                                            tombol_next.config(text="Submit")
                                    else:
                                        # Hitung tingkat stres berdasarkan total skor
                                        tingkat_stres = hitung_tingkat_stres(total_skor_intro)

                                        # Tampilkan pesan hasil dan rekomendasi
                                        hasil_rekomendasi_intro(tingkat_stres)
                                        # messagebox.showinfo("Saved", f"Jawaban Anda telah tersimpan")

                                        # Reset tracker untuk pertanyaan selanjutnya
                                        pertanyaan_index_intro = 0
                                        total_skor_intro = 0
                                        label_pertanyaan.config(text=pertanyaan_intro[pertanyaan_index_intro])

                                        save_to_pdf(tingkat_stres)

                                def hitung_tingkat_stres(total_skor_intro):
                                    # Hitung tingkat stres berdasarkan total skor
                                    return total_skor_intro

                                # Buat tes_kesehatan_mental_intro utama

                                # Pertanyaan
                                label_pertanyaan = tk.Label(tes_kesehatan_mental_intro, text=pertanyaan_intro[pertanyaan_index_intro], font=("Arial", 20,"bold"), bg= '#FAD5A6', fg='#545454')
                                label_pertanyaan.place(x= 50,y=443)

                                # Slideer jawaban
                                skala_var = tk.DoubleVar()
                                skala_var.set(1.0)  # Default nilai pertanyaan adalah 5.0

                                skala_intro = tk.Scale(tes_kesehatan_mental_intro, from_=1.0, to=10.0, orient=tk.HORIZONTAL, width = 20, variable=skala_var, resolution=0.1, bg = '#FAD5A6')
                                skala_intro.place(x= 1375, y=443)

                                tombol_next = tk.Button(tes_kesehatan_mental_intro, text= "Next", command=selanjutnya, font=("Arial", 16, "bold"), bg = '#A98F73', border=0, activebackground='#A98F73')
                                tombol_next.place(x=1365, y=725)

                                tombol_back_intro = tk.Button(tes_kesehatan_mental_intro, text="Back", command= kembali_intro, font=("Arial", 16, 'bold'),bg = '#A98F73', border=0, activebackground= '#A98F73' )
                                tombol_back_intro.place(x=1170, y=725)

                                # Jalankan aplikasi
                                tes_kesehatan_mental_intro.mainloop()
                        # Akhir tes kesehatan mental introvert
                        
                        # Awal tes kesehatan mental ekstrovert
                            def mental_ekstrovert():
                                halaman_tes_mental.destroy()
                                tes_kesehatan_mental_ekstro = tk.Toplevel(hal1)
                                tes_kesehatan_mental_ekstro.title("Mental Health Tracker")
                                width, height = tes_kesehatan_mental_ekstro.winfo_screenwidth(), tes_kesehatan_mental_ekstro.winfo_screenheight()
                                tes_kesehatan_mental_ekstro.geometry(f"{width}x{height}")
                                tes_kesehatan_mental_ekstro.configure(bg="white")
                                tes_kesehatan_mental_ekstro.resizable(False,False)

                                img_mental_ekstro = Image.open('desain tes mental.png')
                                img_bg_mental_ekstro = img_mental_ekstro.resize((1550,850
                                ), Image.Resampling.BICUBIC)
                                photo_mental_ekstro =ImageTk.PhotoImage(img_bg_mental_ekstro)

                                label_mental_ekstro = tk.Label(tes_kesehatan_mental_ekstro, image=photo_mental_ekstro, bg='white', bd=0)
                                label_mental_ekstro.place(x=0, y=0)
                                
                                # Def rekomendasi bisa diisi rekomendasinya pake label
                                def hasil_jendela_ekstro(tingkat_stres_ekstro):
                                    tes_kesehatan_mental_ekstro.destroy()
                                    hasil_ekstro = tk.Toplevel(hal1)
                                    hasil_ekstro.title("Hasil dan Rekomendasi")
                                    width, height =hasil_ekstro.winfo_screenwidth(),hasil_ekstro.winfo_screenheight()
                                    hasil_ekstro.geometry(f"{width}x{height}")
                                    hasil_ekstro.resizable(False,False)
                                    def tutup():
                                        hasil_ekstro.destroy()

                                    def pin():
                                        messagebox.showinfo("Save","PDF tersimpan")

                                    if tingkat_stres_ekstro <= 20:
                                        img_hasil_ekstro1 = Image.open('desain hijau.png')
                                        img_bg_hasil_ekstro1 = img_hasil_ekstro1.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_ekstro1 =ImageTk.PhotoImage(img_bg_hasil_ekstro1)

                                        label_hasil_ekstro1 = tk.Label(hasil_ekstro, image=photo_hasil_ekstro1, bg='white', bd=0)
                                        label_hasil_ekstro1.place(x=0, y=0)

                                        hasil_label_ekstro1 = tk.Label(hasil_ekstro, text=f"{tingkat_stres_ekstro}%", font = ("Arial", 20, "bold"), bg = "#7DFB48")
                                        hasil_label_ekstro1.pack(pady=216, padx=215)

                                        label_hal1 = tk.Button(hasil_ekstro, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal1.place(x= 66, y=52)

                                        label_save1 = tk.Button(hasil_ekstro, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save1.place(x=688, y=728)

                                    elif 20 < tingkat_stres_ekstro <= 50:
                                        img_hasil_ekstro2 = Image.open('desain kuning.png')
                                        img_bg_hasil_ekstro2 = img_hasil_ekstro2.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_ekstro2 =ImageTk.PhotoImage(img_bg_hasil_ekstro2)

                                        label_hasil_ekstro2 = tk.Label(hasil_ekstro, image=photo_hasil_ekstro2, bg='white', bd=0)
                                        label_hasil_ekstro2.place(x=0, y=0)

                                        hasil_label_ekstro2 = tk.Label(hasil_ekstro, text=f"{tingkat_stres_ekstro}%", font = ("Arial", 22, "bold"), bg = "#F7D54B")
                                        hasil_label_ekstro2.pack(pady=216, padx=215)

                                        label_hal2 = tk.Button(hasil_ekstro, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal2.place(x= 66, y=52)

                                        label_save2 = tk.Button(hasil_ekstro, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save2.place(x=688, y=728)

                                    elif 50 < tingkat_stres_ekstro <= 80:
                                        img_hasil_ekstro3 = Image.open('desain orange.png')
                                        img_bg_hasil_ekstro3 = img_hasil_ekstro3.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_ekstro3 =ImageTk.PhotoImage(img_bg_hasil_ekstro3)

                                        label_hasil_ekstro3 = tk.Label(hasil_ekstro, image=photo_hasil_ekstro3, bg='white', bd=0)
                                        label_hasil_ekstro3.place(x=0, y=0)

                                        hasil_label_ekstro3 = tk.Label(hasil_ekstro, text=f"{tingkat_stres_ekstro}%", font = ("Arial", 22, "bold"), bg = "#E09645")
                                        hasil_label_ekstro3.pack(pady=216, padx=215)

                                        label_hal3 = tk.Button(hasil_ekstro, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal3.place(x= 66, y=52)

                                        label_save3 = tk.Button(hasil_ekstro, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save3.place(x=688, y=728)

                                    else:
                                        img_hasil_ekstro4 = Image.open('desain merah.png')
                                        img_bg_hasil_ekstro4 = img_hasil_ekstro4.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_ekstro4 =ImageTk.PhotoImage(img_bg_hasil_ekstro4)

                                        label_hasil_ekstro4 = tk.Label(hasil_ekstro, image=photo_hasil_ekstro4, bg='white', bd=0)
                                        label_hasil_ekstro4.place(x=0, y=0)

                                        hasil_label_ekstro4 = tk.Label(hasil_ekstro, text=f"{tingkat_stres_ekstro}%", font = ("Arial", 22, "bold"), bg="#FC7A65")
                                        hasil_label_ekstro4.pack(pady=216, padx=215)

                                        label_hal4 = tk.Button(hasil_ekstro, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup, bg='#B4B19C', border= 0, activebackground='#B4B19C' )
                                        label_hal4.place(x= 66, y=52)

                                        label_save4 = tk.Button(hasil_ekstro, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save4.place(x=688, y=728)

                                    save_to_pdf(tingkat_stres_ekstro)
                                    hasil_ekstro.mainloop()
    # KUNCI PDF
                                def save_to_pdf(tingkat_stres_ekstro):
                                    pdf_filename = "hasil_ekstrovert.pdf"

                                    nama_pengguna = nama_pengguna_var.get()

                                    c = canvas.Canvas(pdf_filename, pagesize=(1060, 630))
                                    c.setFont("Helvetica-Bold", 30)

                                    img_path = 'ekstrovert.png'
                                    c.drawImage(img_path, 0, 0, width=1060, height=630) 
                                    c.drawString(67, 287, f"{tingkat_stres_ekstro}%")

                                    c.drawString(67, 452, f"{nama_pengguna}")
                                    
                                    c.save()


                                global total_skor_ekstro
                                pertanyaan_index_ekstro = 0
                                total_skor_ekstro = 0
                                pertanyaan_ekstro = [
                                        "1. Seberapa sering Anda merasa lelah hari-hari ini: ",
                                        "2. Sejauh mana Anda sering mencemaskan tentang masa depan: ",
                                        "3. Seberapa sering Anda merasa kesepian dalam sehari-hari: ",
                                        "4. Seberapa sering anda tidur larut malam diatas jam 10: ",
                                        "5. Bagaimana Anda menilai tingkat detak jantung dalam segala situasi: ",
                                        "6. Seberapa harmonis hubungan keluarga, kerabat, dan pasangan Anda: ",
                                        "7. Sejauh mana Anda merasa tidak dapat mengatasi tekanan hidup: ",
                                        "8. Seberapa sering Anda merasa insecure dengan orang lain: ",
                                        "9. Seberapa sering Anda merasa sulit berkonsentrasi atau fokus: ",
                                        "10. seberapa sering Anda merasakan overthinking hari-hari ini"
                                ]

                                def kembali():
                                    global pertanyaan_index_ekstro
                                    if pertanyaan_index_ekstro > 0:
                                        pertanyaan_index_ekstro -= 1
                                        label_pertanyaan.config(text=pertanyaan_ekstro[pertanyaan_index_ekstro])

                                def selanjutnya():
                                    global pertanyaan_index_ekstro, total_skor_ekstro
                                    skor_pertanyaan_ekstro = skala_var_ekstro.get()
                                    total_skor_ekstro += skor_pertanyaan_ekstro

                                    # Pindah ke pertanyaan berikutnya
                                    pertanyaan_index_ekstro += 1

                                    if pertanyaan_index_ekstro < len(pertanyaan_ekstro):
                                        label_pertanyaan.config(text=pertanyaan_ekstro[pertanyaan_index_ekstro])
                                        skala_var_ekstro.set(1.0)  # Reset nilai slider ke default
                                        if pertanyaan_index_ekstro == len(pertanyaan_ekstro) - 1:
                                            tombol_next_ekstro.config(text="Submit")
                                    else:
                                        # Hitung tingkat stres berdasarkan total skor
                                        tingkat_stres_ekstro = hitung_tingkat_stres_ekstro(total_skor_ekstro)

                                        # Tampilkan pesan hasil dan rekomendasi
                                        hasil_jendela_ekstro(tingkat_stres_ekstro)
                                        # messagebox.showinfo("Saved", f"Jawaban Anda telah tersimpan")

                                        # Reset tracker untuk pertanyaan selanjutnya
                                        pertaanyaan_index_ekstro = 0
                                        total_skor_ekstro = 0
                                        label_pertanyaan.config(text=pertanyaan_ekstro[pertaanyaan_index_ekstro])
    # KUNCI PDF
                                        save_to_pdf(tingkat_stres_ekstro)

                                def hitung_tingkat_stres_ekstro(total_skor_ekstro):
                                    # Hitung tingkat stres berdasarkan total skor
                                    return total_skor_ekstro


                                # Pertanyaan
    # TOMBOLLLLLLLL
                                label_pertanyaan = tk.Label(tes_kesehatan_mental_ekstro, text=pertanyaan_ekstro[pertanyaan_index_ekstro], font=("Arial", 20,"bold"), bg= '#FAD5A6', fg='#545454')
                                label_pertanyaan.place(x= 50,y=443)

                                # Slideer jawaban
                                skala_var_ekstro = tk.DoubleVar()
                                skala_var_ekstro.set(1.0)  # Default nilai pertanyaan adalah 5.0

                                skala_ekstro = tk.Scale(tes_kesehatan_mental_ekstro, from_=1.0, to=10.0, orient=tk.HORIZONTAL, width = 20, variable=skala_var_ekstro, resolution=0.1, bg = '#FAD5A6')
                                skala_ekstro.place(x= 1175, y=443)

                                tombol_next_ekstro = tk.Button(tes_kesehatan_mental_ekstro, text= "Next", command=selanjutnya, font=("Arial", 16, "bold"), bg = '#A98F73', border=0, activebackground='#A98F73')
                                tombol_next_ekstro.place(x=1365, y=725)

                                tombol_back_ekstro = tk.Button(tes_kesehatan_mental_ekstro, text="Back", command= kembali, font=("Arial", 16, 'bold'),bg = '#A98F73', border=0, activebackground= '#A98F73' )
                                tombol_back_ekstro.place(x=1170, y=725)

                                tes_kesehatan_mental_ekstro.mainloop()

                                # Jalankan aplikasi
                            
                        # Akhir tes kesehatan mental ekstrovert
                            img_mental = Image.open('desain kesehatan mental.png')
                            img_bg_mental = img_mental.resize((1550,850), Image.Resampling.BICUBIC)
                            photo_mental =ImageTk.PhotoImage(img_bg_mental)

                            label_hasil_mental = tk.Label(halaman_tes_mental, image=photo_mental, bg='white', bd=0)
                            label_hasil_mental.place(x=0, y=0)

                            label_introvert = tk.Button(halaman_tes_mental, text = "Introvert", font = ("Arial", 22, "bold" ), bg ="#AB9175", command = mental_introvert, border=0, activebackground='#AB9175')
                            label_introvert.place(x= 235, y= 610)

                            label_introvert = tk.Button(halaman_tes_mental, text = "Ekstrovert", font = ("Arial", 22, "bold" ), bg ="#AB9175", command= mental_ekstrovert, border=0, activebackground='#AB9175')
                            label_introvert.place(x= 635, y= 610)

                            halaman_tes_mental.mainloop()

                        hasil_label = tk.Label(hasil_tes_kepribadian, text=f"{tingkat_stres}", font = ("Arial", 25, "bold"))
                        hasil_label.place(x=400, y=25)

                        if total_yes > total_no:
                            img_hasil_teskip = Image.open('desain ekstrovert.png')
                            img_bg_hasilteksip = img_hasil_teskip.resize((1550,850
                            ), Image.Resampling.BICUBIC)
                            photo_hasil_teksip =ImageTk.PhotoImage(img_bg_hasilteksip)

                            label_hasil_teksip = tk.Label(hasil_tes_kepribadian, image=photo_hasil_teksip, bg='white', bd=0)
                            label_hasil_teksip.place(x=0, y=0)

                            tes_selanjutnya = tk.Button(hasil_tes_kepribadian, text=" Tes Gangguan Mental", command= tes_mental, font = ("Arial", 20, 'bold'), border= 0, bg= '#AA8163', activebackground='#AA8163')
                            tes_selanjutnya.place(x=647, y=718)
                        elif total_yes < total_no:
                            img_hasil_teskip2 = Image.open('desain introvert.png')
                            img_bg_hasilteksip2 = img_hasil_teskip2.resize((1550,850
                            ), Image.Resampling.BICUBIC)
                            photo_hasil_teksip2 =ImageTk.PhotoImage(img_bg_hasilteksip2)

                            label_hasil_teksip2 = tk.Label(hasil_tes_kepribadian, image=photo_hasil_teksip2, bg='white', bd=0)
                            label_hasil_teksip2.place(x=0, y=0)

                            tes_selanjutnya2 = tk.Button(hasil_tes_kepribadian, text=" Tes Gangguan Mental", command= tes_mental, font = ("Arial", 20, 'bold'), border= 0, bg= '#AA8163', activebackground='#AA8163' )
                            tes_selanjutnya2.place(x=647, y=718)
                            
                        else:
                            messagebox.showinfo("Not Valid", f"Anda tidak mengisi jawaban")
                        hasil_tes_kepribadian.mainloop()

                    global total_yes, total_no
                    pertanyaan_index = 0
                    total_yes = 0
                    total_no = 0
                    pertanyaan = [
                        "1. Apakah Anda senang berinteraksi dengan orang lain? ",
                        "2. Apakah Anda merasa senang bekerja secara berkelompok dengan teman-teman Anda?",
                        "3. Apakah Anda mudah bergaul dengan orang lain?",
                        "4. Apakah Anda mudah terbuka terhadap perubahan dan hal baru? ",
                        "5. Apakah Anda merasa diri Anda adalah orang yang sangat bersemangat dan energik? ",
                        "6. Apakah Anda lebih senang bercerita kepada teman Anda mengenai kegiatan sehari-hari Anda? ",
                        "7. Apakah Anda suka datang ke pesta ulang tahun dan bersenang-senang dengan teman Anda? ",
                        "8. Apakah Anda lebih suka telepon dengan orang lain dari pada chatting dengan orang lain? ",
                        "9. Apakah Anda lebih suka mengutarakan apa yang Anda pikirkan dari pada memendamnya sendiri? ",
                        "10. Apakah Anda sering menjadi ketua dalam tugas kelompok? ",
                        "11. Apakah Anda sering mengeluarkan pendapat Anda meskipun harus berdebat dengan orang lain?",
                        "12. Apakah Anda lebih suka berbincang dengan topik ringan dari pada topik berat?",
                        "13. Apakah fokus Anda sering pecah saat ada sesuatu yang mendistraksi Anda?",
                        "14. Apakah Anda pandai mencari topik dan mencairkan suasana?",
                        "15. Apakah teman Anda sering mengatakan bahwa Anda memiliki public speaking yang bagus?"
                    ]
                    def kembali():
                        global pertanyaan_index
                        if pertanyaan_index > 0:
                            pertanyaan_index -= 1
                            label_pertanyaan.config(text=pertanyaan[pertanyaan_index])
                            

                    def selanjutnya():
                        global pertanyaan_index, total_yes, total_no
                        jawaban = answer_var.get()

                        if jawaban == "Yes":
                            total_yes += 1
                        elif jawaban == "No":
                            total_no += 1

                        pertanyaan_index += 1

                        if pertanyaan_index < len(pertanyaan):
                            label_pertanyaan.config(text=pertanyaan[pertanyaan_index])
                            answer_var.set(0)  # Reset radio button selection
                            if pertanyaan_index == len(pertanyaan) - 1:
                                tombol_selanjutnya.config(text = "Submit")
                        else:
                            hasil_tes = hitung_hasil_tes(total_yes, total_no)
                            hasil_kepribadian(hasil_tes)
                            messagebox.showinfo("Saved", f"Jawaban Anda telah tersimpan")

                    def hitung_hasil_tes(total_yes, total_no):
                        if total_yes > total_no:
                            return "Ekstrovert"
                        elif total_yes < total_no:
                            return "Introvert"
                        else:
                            return "Tidak Valid"

                    # Bg desain tes kepribadian
                    img_teskep = Image.open('desain tes kepribadian.png')
                    img_bg_teskep = img_teskep.resize((1550,850
                    ), Image.Resampling.BICUBIC)
                    photo_bg_teskep =ImageTk.PhotoImage(img_bg_teskep)

                    label_teskep = tk.Label(tes_kepribadian, image=photo_bg_teskep, bg='white', bd=0)
                    label_teskep.place(x=0, y=0)

                    label_pertanyaan = tk.Label(tes_kepribadian, text=pertanyaan[pertanyaan_index], font=("Arial", 20, "bold"), bg = "#FAD5A6", fg = '#545454')
                    label_pertanyaan.place(x=50, y=410)

                    answer_var = tk.StringVar()
                    # Radio Button Yes dan No
                    yes_radio = tk.Radiobutton(tes_kepribadian, text="Yes", variable=answer_var, value="Yes", font=("Arial", 14), bg = "#FAD5A6", fg = '#545454' )
                    yes_radio.place(x=100, y=453)

                    no_radio = tk.Radiobutton(tes_kepribadian, text="No", variable=answer_var, value="No", font=("Arial", 14), bg= "#FAD5A6", fg ='#545454'  )
                    no_radio.place(x=100, y=483)
                    # Tombol selanjutnya dan back
                    tombol_selanjutnya = tk.Button(tes_kepribadian, text="Next", command=selanjutnya, font= ("Arial", 16, 'bold'),bg = '#A98F73', border= 0, activebackground= '#A98F73' )
                    tombol_selanjutnya.place(x=1350, y=718)

                    tombol_back = tk.Button(tes_kepribadian, text="Back", command= kembali, font=("Arial", 16, 'bold'),bg = '#A98F73', border=0, activebackground= '#A98F73' )
                    tombol_back.place(x=1170, y=718)

                    tes_kepribadian.mainloop()
                # Bg desain kepribadian
                img_kepribadian = Image.open('desain kepribadian.png')
                img_bg_kepribadian = img_kepribadian.resize((1550,850))
                photo_bg_kepribadian = ImageTk.PhotoImage(img_bg_kepribadian)

                label_img_kepribadian = tk.Label(hal3_test, image=photo_bg_kepribadian, bg='white', bd=0)
                label_img_kepribadian.place(x=0, y=0)

                mulai_tes = tk.Button(hal3_test, text ="MULAI", font=('Arial', 22, 'bold'),  bg ="#A98F73", command = mulai, border=0, activebackground='#A98F73'  )
                mulai_tes.place(x= 580, y=658)
    # KUNCI PDF
                label_nama_pengguna = tk.Label(hal3_test, text="Nama Lengkap:", font=("Arial", 12), bg ="#A98F73")
                label_nama_pengguna.place(x=487, y=572)

                entry_nama_pengguna = tk.Entry(hal3_test, textvariable=nama_pengguna_var, font=("Arial", 12), bg ="#A98F73")
                entry_nama_pengguna.place(x=627, y=572)

                hal3_test.mainloop()

            next = tk.Button (hal2_alur, text="MULAI", font=('Arial', 22), bg ="#B6B4C6", fg = "black", command = test, border= 0)
            next.place(x= 308, y=355)  
                
            hal2_alur.mainloop()

            # Tombol Tulisan

        alur = tk.Button(hal1, text ="Alur dan\n Petunjuk", font=('Arial', 12, 'bold'), bg ="#B6B4C6", border=0, command = alur, activebackground= "#B6B4C6")
        alur.place(x= 807, y=546)

            # Gambar 2 dan pengerjaan tes
        def test():
                hal3_test= tk.Toplevel(hal1)
                hal3_test.title("Registrasi")
                width, height = hal3_test.winfo_screenwidth(), hal3_test.winfo_screenheight()
                hal3_test.geometry(f"{width}x{height}")
                hal3_test.configure(bg="white")
                hal3_test.resizable(False,False)
    # PDF KUNCI
                nama_pengguna_var = tk.StringVar()

                def mulai():
                    hal3_test.destroy()
                    tes_kepribadian = tk.Toplevel(hal1)
                    tes_kepribadian.title("Mental Health Tracker")
                    width, height = tes_kepribadian.winfo_screenwidth(), tes_kepribadian.winfo_screenheight()
                    tes_kepribadian.geometry(f"{width}x{height}")
                    tes_kepribadian.configure(bg="white")
                    tes_kepribadian.resizable(False, False)

                    def hasil_kepribadian(tingkat_stres):
                        tes_kepribadian.destroy()
                        hasil_tes_kepribadian = tk.Toplevel(hal1)
                        hasil_tes_kepribadian.title("Hasil dan Rekomendasi")
                        width, height = hasil_tes_kepribadian.winfo_screenwidth(), hasil_tes_kepribadian.winfo_screenheight()
                        hasil_tes_kepribadian.geometry(f"{width}x{height}")
                        hasil_tes_kepribadian.resizable(False, False)

                        def tes_mental():
                            hasil_tes_kepribadian.destroy()
                            halaman_tes_mental = tk.Toplevel(hal1)
                            halaman_tes_mental.title("Mental Health Test")
                            width, height = halaman_tes_mental.winfo_screenwidth(), halaman_tes_mental.winfo_screenheight()
                            halaman_tes_mental.geometry(f"{width}x{height}")
                            halaman_tes_mental.resizable(False, False)

                        #  Awal tes kesehatan mental introvert
                            def mental_introvert():
                                halaman_tes_mental.destroy()
                                tes_kesehatan_mental_intro = tk.Toplevel(hal1)
                                tes_kesehatan_mental_intro.title("Mental Health Tracker")
                                width, height = tes_kesehatan_mental_intro.winfo_screenwidth(), tes_kesehatan_mental_intro.winfo_screenheight()
                                tes_kesehatan_mental_intro.geometry(f"{width}x{height}")
                                tes_kesehatan_mental_intro.configure(bg="white")
                                tes_kesehatan_mental_intro.resizable(False,False)

                                img_mental_intro = Image.open('desain tes mental.png')
                                img_bg_mental_intro = img_mental_intro.resize((1550,850), Image.Resampling.BICUBIC)
                                photo_mental_intro =ImageTk.PhotoImage(img_bg_mental_intro)

                                label_mental_intro = tk.Label(tes_kesehatan_mental_intro, image=photo_mental_intro, bg='white', bd=0)
                                label_mental_intro.place(x=0, y=0)
                                
                                # Def rekomendasi bisa diisi rekomendasinya pake label
                                def hasil_rekomendasi_intro(tingkat_stres):
                                    tes_kesehatan_mental_intro.destroy()
                                    hasil_jendela = tk.Toplevel(hal1)
                                    hasil_jendela.title("Hasil dan Rekomendasi")
                                    width, height = hasil_jendela.winfo_screenwidth(), hasil_jendela.winfo_screenheight()
                                    hasil_jendela.geometry(f"{width}x{height}")
                                    hasil_jendela.resizable(False,False)
                                    def tutup2():
                                        hasil_jendela.destroy

                                    def pin():
                                        messagebox.showinfo("Save","PDF tersimpan")

                                    if tingkat_stres <= 20:
                                        img_hasil_intro1 = Image.open('desain hijau.png')
                                        img_bg_hasil_intro1 = img_hasil_intro1.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_intro1 =ImageTk.PhotoImage(img_bg_hasil_intro1)

                                        label_hasil_intro1 = tk.Label(hasil_jendela, image=photo_hasil_intro1, bg='white', bd=0)
                                        label_hasil_intro1.place(x=0, y=0)

                                        hasil_label_intro1 = tk.Label(hasil_jendela, text=f"{tingkat_stres}%", font = ("Arial", 22, "bold"), bg = "#7DFB48")
                                        hasil_label_intro1.pack(pady=216, padx=215)

                                        label_hal1 = tk.Button(hasil_jendela, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup2, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal1.place(x= 66, y=52)

                                        label_save1 = tk.Button(hasil_jendela, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save1.place(x=688, y=728)

                                    elif 20 < tingkat_stres <= 50:
                                        img_hasil_intro2 = Image.open('desain kuning.png')
                                        img_bg_hasil_intro2 = img_hasil_intro2.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_intro2 =ImageTk.PhotoImage(img_bg_hasil_intro2)

                                        label_hasil_intro2 = tk.Label(hasil_jendela, image=photo_hasil_intro2, bg='white', bd=0)
                                        label_hasil_intro2.place(x=0, y=0)

                                        hasil_label_intro2 = tk.Label(hasil_jendela, text=f"{tingkat_stres}%", font = ("Arial", 22, "bold"), bg="#F7D54B")
                                        hasil_label_intro2.pack(pady=216, padx=215)

                                        label_hal2 = tk.Button(hasil_jendela, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup2, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal2.place(x= 66, y=52)

                                        label_save2 = tk.Button(hasil_jendela, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save2.place(x=688, y=728)

                                    elif 50 < tingkat_stres <= 80:
                                        img_hasil_intro3 = Image.open('desain orange.png')
                                        img_bg_hasil_intro3 = img_hasil_intro3.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_intro3 =ImageTk.PhotoImage(img_bg_hasil_intro3)

                                        label_hasil_intro3 = tk.Label(hasil_jendela, image=photo_hasil_intro3, bg='white', bd=0)
                                        label_hasil_intro3.place(x=0, y=0)

                                        hasil_label_intro3 = tk.Label(hasil_jendela, text=f"{tingkat_stres}%", font = ("Arial", 22, "bold"), bg ="#E09645")
                                        hasil_label_intro3.pack(pady=216, padx=215)

                                        label_hal3 = tk.Button(hasil_jendela, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup2, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal3.place(x= 66, y=52)

                                        label_save3 = tk.Button(hasil_jendela, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save3.place(x=688, y=728)

                                    else:
                                        img_hasil_intro4 = Image.open('desain merah.png')
                                        img_bg_hasil_intro4 = img_hasil_intro4.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_intro4 =ImageTk.PhotoImage(img_bg_hasil_intro4)

                                        label_hasil_intro4 = tk.Label(hasil_jendela, image=photo_hasil_intro4, bg='white', bd=0)
                                        label_hasil_intro4.place(x=0, y=0)

                                        hasil_label_intro4 = tk.Label(hasil_jendela, text=f"{tingkat_stres}%", font = ("Arial", 22, "bold"), bg = "#FC7A65")
                                        hasil_label_intro4.pack(pady=216, padx=215)

                                        label_hal4 = tk.Button(hasil_jendela, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup2, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal4.place(x= 66, y=52)

                                        label_save3 = tk.Button(hasil_jendela, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save3.place(x=688, y=728)
                                    save_to_pdf(tingkat_stres)
                                    hasil_jendela.mainloop()
                                    
    # KUNCI PDF
                                def save_to_pdf(tingkat_stres):
                                    pdf_filename = "hasil_introvert.pdf"

                                    nama_pengguna = nama_pengguna_var.get()

                                    c = canvas.Canvas(pdf_filename, pagesize=(1060, 630))
                                    c.setFont("Helvetica-Bold", 30)

                                    img_path = 'introvert.png'
                                    c.drawImage(img_path, 0, 0,width=1060, height=630) 
                                    c.drawString(67, 287, f"{tingkat_stres}%")

                                    c.drawString(67, 452, f"{nama_pengguna}")
                                    
                                    c.save()


                                pertanyaan_index_intro = 0
                                pertanyaan_intro = [
                                        "1. Seberapa sering Anda merasa cemas atau stress saat berada di lingkungan sosial yang ramai? ",
                                        "2. Seberapa sering Anda merasa sedih dan tak berdaya? ",
                                        "3. Seberapa sering Anda mengalami gangguan makan seperti tidak nafsu makan? ",
                                        "4. Seberapa sering Anda merasa overthinking dalam kegiatan sehari-hari? ",
                                        "5. Seberapa sering Anda merasa tertekan dengan keadaan sosial yang terjadi di sekitar Anda? ",
                                        "6. Seberapa sering Anda tidak bisa tidur atau insomnia? ",
                                        "7. Seberapa sering Anda merasa ingin melukai diri sendiri? ",
                                        "8. Seberapa sering Anda ingin mengkritisi diri sendiri? ",
                                        "9. Seberapa sering Anda ingin mengisolasi diri dari dunia luar? ",
                                        "10. Seberapa sering Anda merasa ketakutan dan ingin mengakhiri hidup? "
                                ]
                                def kembali_intro():
                                    global pertanyaan_index_intro
                                    if pertanyaan_index_intro > 0:
                                        pertanyaan_index_intro -= 1
                                        label_pertanyaan.config(text=pertanyaan_intro[pertanyaan_index_intro])

                                def selanjutnya():
                                    global pertanyaan_index_intro, total_skor_intro
                                    skor_pertanyaan = skala_var.get()
                                    total_skor_intro += skor_pertanyaan

                                    # Pindah ke pertanyaan berikutnya
                                    pertanyaan_index_intro += 1

                                    if pertanyaan_index_intro < len(pertanyaan_intro):
                                        label_pertanyaan.config(text=pertanyaan_intro[pertanyaan_index_intro])
                                        skala_var.set(1.0)  # Reset nilai slider ke default
                                        if pertanyaan_index_intro == len(pertanyaan_intro) - 1:
                                            tombol_next.config(text="Submit")
                                    else:
                                        # Hitung tingkat stres berdasarkan total skor
                                        tingkat_stres = hitung_tingkat_stres(total_skor_intro)

                                        # Tampilkan pesan hasil dan rekomendasi
                                        hasil_rekomendasi_intro(tingkat_stres)
                                        # messagebox.showinfo("Saved", f"Jawaban Anda telah tersimpan")

                                        # Reset tracker untuk pertanyaan selanjutnya
                                        pertanyaan_index_intro = 0
                                        total_skor_intro = 0
                                        label_pertanyaan.config(text=pertanyaan_intro[pertanyaan_index_intro])

                                        save_to_pdf(tingkat_stres)

                                def hitung_tingkat_stres(total_skor_intro):
                                    # Hitung tingkat stres berdasarkan total skor
                                    return total_skor_intro

                                # Buat tes_kesehatan_mental_intro utama

                                # Pertanyaan
                                label_pertanyaan = tk.Label(tes_kesehatan_mental_intro, text=pertanyaan_intro[pertanyaan_index_intro], font=("Arial", 20,"bold"), bg= '#FAD5A6', fg='#545454')
                                label_pertanyaan.place(x= 50,y=443)

                                # Slideer jawaban
                                skala_var = tk.DoubleVar()
                                skala_var.set(1.0)  # Default nilai pertanyaan adalah 5.0

                                skala_intro = tk.Scale(tes_kesehatan_mental_intro, from_=1.0, to=10.0, orient=tk.HORIZONTAL, width = 20, variable=skala_var, resolution=0.1, bg = '#FAD5A6')
                                skala_intro.place(x= 1375, y=443)

                                tombol_next = tk.Button(tes_kesehatan_mental_intro, text= "Next", command=selanjutnya, font=("Arial", 16, "bold"), bg = '#A98F73', border=0, activebackground='#A98F73')
                                tombol_next.place(x=1365, y=725)

                                tombol_back_intro = tk.Button(tes_kesehatan_mental_intro, text="Back", command= kembali_intro, font=("Arial", 16, 'bold'),bg = '#A98F73', border=0, activebackground= '#A98F73' )
                                tombol_back_intro.place(x=1170, y=725)

                                # Jalankan aplikasi
                                tes_kesehatan_mental_intro.mainloop()
                        # Akhir tes kesehatan mental introvert
                        
                        # Awal tes kesehatan mental ekstrovert
                            def mental_ekstrovert():
                                halaman_tes_mental.destroy()
                                tes_kesehatan_mental_ekstro = tk.Toplevel(hal1)
                                tes_kesehatan_mental_ekstro.title("Mental Health Tracker")
                                width, height = tes_kesehatan_mental_ekstro.winfo_screenwidth(), tes_kesehatan_mental_ekstro.winfo_screenheight()
                                tes_kesehatan_mental_ekstro.geometry(f"{width}x{height}")
                                tes_kesehatan_mental_ekstro.configure(bg="white")
                                tes_kesehatan_mental_ekstro.resizable(False,False)

                                img_mental_ekstro = Image.open('desain tes mental.png')
                                img_bg_mental_ekstro = img_mental_ekstro.resize((1550,850
                                ), Image.Resampling.BICUBIC)
                                photo_mental_ekstro =ImageTk.PhotoImage(img_bg_mental_ekstro)

                                label_mental_ekstro = tk.Label(tes_kesehatan_mental_ekstro, image=photo_mental_ekstro, bg='white', bd=0)
                                label_mental_ekstro.place(x=0, y=0)
                                
                                # Def rekomendasi bisa diisi rekomendasinya pake label
                                def hasil_jendela_ekstro(tingkat_stres_ekstro):
                                    tes_kesehatan_mental_ekstro.destroy()
                                    hasil_ekstro = tk.Toplevel(hal1)
                                    hasil_ekstro.title("Hasil dan Rekomendasi")
                                    width, height =hasil_ekstro.winfo_screenwidth(),hasil_ekstro.winfo_screenheight()
                                    hasil_ekstro.geometry(f"{width}x{height}")
                                    hasil_ekstro.resizable(False,False)
                                    def tutup():
                                        hasil_ekstro.destroy()
                                    def pin():
                                        messagebox.showinfo("Save","PDF tersimpan")

                                    if tingkat_stres_ekstro <= 20:
                                        img_hasil_ekstro1 = Image.open('desain hijau.png')
                                        img_bg_hasil_ekstro1 = img_hasil_ekstro1.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_ekstro1 =ImageTk.PhotoImage(img_bg_hasil_ekstro1)

                                        label_hasil_ekstro1 = tk.Label(hasil_ekstro, image=photo_hasil_ekstro1, bg='white', bd=0)
                                        label_hasil_ekstro1.place(x=0, y=0)

                                        hasil_label_ekstro1 = tk.Label(hasil_ekstro, text=f"{tingkat_stres_ekstro}%", font = ("Arial", 20, "bold"), bg = "#7DFB48")
                                        hasil_label_ekstro1.pack(pady=216, padx=215)

                                        label_hal1 = tk.Button(hasil_ekstro, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal1.place(x= 66, y=52)

                                        label_save1 = tk.Button(hasil_ekstro, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save1.place(x=688,y=728)

                                    elif 20 < tingkat_stres_ekstro <= 50:
                                        img_hasil_ekstro2 = Image.open('desain kuning.png')
                                        img_bg_hasil_ekstro2 = img_hasil_ekstro2.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_ekstro2 =ImageTk.PhotoImage(img_bg_hasil_ekstro2)

                                        label_hasil_ekstro2 = tk.Label(hasil_ekstro, image=photo_hasil_ekstro2, bg='white', bd=0)
                                        label_hasil_ekstro2.place(x=0, y=0)

                                        hasil_label_ekstro2 = tk.Label(hasil_ekstro, text=f"{tingkat_stres_ekstro}%", font = ("Arial", 22, "bold"), bg = "#F7D54B")
                                        hasil_label_ekstro2.pack(pady=216, padx=215)

                                        label_hal2 = tk.Button(hasil_ekstro, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal2.place(x= 66, y=52)

                                        label_save2 = tk.Button(hasil_ekstro, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save2.place(x=688,y=728)

                                    elif 50 < tingkat_stres_ekstro <= 80:
                                        img_hasil_ekstro3 = Image.open('desain orange.png')
                                        img_bg_hasil_ekstro3 = img_hasil_ekstro3.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_ekstro3 =ImageTk.PhotoImage(img_bg_hasil_ekstro3)

                                        label_hasil_ekstro3 = tk.Label(hasil_ekstro, image=photo_hasil_ekstro3, bg='white', bd=0)
                                        label_hasil_ekstro3.place(x=0, y=0)

                                        hasil_label_ekstro3 = tk.Label(hasil_ekstro, text=f"{tingkat_stres_ekstro}%", font = ("Arial", 22, "bold"), bg = "#E09645")
                                        hasil_label_ekstro3.pack(pady=216, padx=215)

                                        label_hal3 = tk.Button(hasil_ekstro, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup, bg='#B4B19C', border= 0, activebackground='#B4B19C')
                                        label_hal3.place(x= 66, y=52)

                                        label_save3 = tk.Button(hasil_ekstro, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save3.place(x=688,y=728)

                                    else:
                                        img_hasil_ekstro4 = Image.open('desain merah.png')
                                        img_bg_hasil_ekstro4 = img_hasil_ekstro4.resize((1550,850
                                        ), Image.Resampling.BICUBIC)
                                        photo_hasil_ekstro4 =ImageTk.PhotoImage(img_bg_hasil_ekstro4)

                                        label_hasil_ekstro4 = tk.Label(hasil_ekstro, image=photo_hasil_ekstro4, bg='white', bd=0)
                                        label_hasil_ekstro4.place(x=0, y=0)

                                        hasil_label_ekstro4 = tk.Label(hasil_ekstro, text=f"{tingkat_stres_ekstro}%", font = ("Arial", 22, "bold"), bg="#FC7A65")
                                        hasil_label_ekstro4.pack(pady=216, padx=215)

                                        label_hal4 = tk.Button(hasil_ekstro, text= "Kembali", font = ("Arial", 12, "bold"), command= tutup, bg='#B4B19C', border= 0, activebackground='#B4B19C' )
                                        label_hal4.place(x= 66, y=52)

                                        label_save4 = tk.Button(hasil_ekstro, text= "Simpan PDF", font = ("Arial", 16, "bold"), command= pin, bg='#835F4A', border= 0, activebackground='#835F4A')
                                        label_save4.place(x=688,y=728)

                                    save_to_pdf(tingkat_stres_ekstro)
                                    hasil_ekstro.mainloop()
    # KUNCI PDF
                                def save_to_pdf(tingkat_stres_ekstro):
                                    pdf_filename = "hasil_ekstrovert.pdf"

                                    nama_pengguna = nama_pengguna_var.get()

                                    c = canvas.Canvas(pdf_filename, pagesize=(1060, 630))
                                    c.setFont("Helvetica-Bold", 30)

                                    img_path = 'ekstrovert.png'
                                    c.drawImage(img_path, 0, 0, width=1060, height=630) 
                                    c.drawString(67, 287, f"{tingkat_stres_ekstro}%")

                                    c.drawString(67, 452, f"{nama_pengguna}")
                                    
                                    c.save()


                                global total_skor_ekstro
                                pertanyaan_index_ekstro = 0
                                total_skor_ekstro = 0
                                pertanyaan_ekstro = [
                                        "1. Seberapa sering Anda merasa lelah hari-hari ini: ",
                                        "2. Sejauh mana Anda sering mencemaskan tentang masa depan: ",
                                        "3. Seberapa sering Anda merasa kesepian dalam sehari-hari: ",
                                        "4. Seberapa sering anda tidur larut malam diatas jam 10: ",
                                        "5. Bagaimana Anda menilai tingkat detak jantung dalam segala situasi: ",
                                        "6. Seberapa harmonis hubungan keluarga, kerabat, dan pasangan Anda: ",
                                        "7. Sejauh mana Anda merasa tidak dapat mengatasi tekanan hidup: ",
                                        "8. Seberapa sering Anda merasa insecure dengan orang lain: ",
                                        "9. Seberapa sering Anda merasa sulit berkonsentrasi atau fokus: ",
                                        "10. seberapa sering Anda merasakan overthinking hari-hari ini"
                                ]

                                def kembali():
                                    global pertanyaan_index_ekstro
                                    if pertanyaan_index_ekstro > 0:
                                        pertanyaan_index_ekstro -= 1
                                        label_pertanyaan.config(text=pertanyaan_ekstro[pertanyaan_index_ekstro])

                                def selanjutnya():
                                    global pertanyaan_index_ekstro, total_skor_ekstro
                                    skor_pertanyaan_ekstro = skala_var_ekstro.get()
                                    total_skor_ekstro += skor_pertanyaan_ekstro

                                    # Pindah ke pertanyaan berikutnya
                                    pertanyaan_index_ekstro += 1

                                    if pertanyaan_index_ekstro < len(pertanyaan_ekstro):
                                        label_pertanyaan.config(text=pertanyaan_ekstro[pertanyaan_index_ekstro])
                                        skala_var_ekstro.set(1.0)  # Reset nilai slider ke default
                                        if pertanyaan_index_ekstro == len(pertanyaan_ekstro) - 1:
                                            tombol_next_ekstro.config(text="Submit")
                                    else:
                                        # Hitung tingkat stres berdasarkan total skor
                                        tingkat_stres_ekstro = hitung_tingkat_stres_ekstro(total_skor_ekstro)

                                        # Tampilkan pesan hasil dan rekomendasi
                                        hasil_jendela_ekstro(tingkat_stres_ekstro)
                                        # messagebox.showinfo("Saved", f"Jawaban Anda telah tersimpan")

                                        # Reset tracker untuk pertanyaan selanjutnya
                                        pertaanyaan_index_ekstro = 0
                                        total_skor_ekstro = 0
                                        label_pertanyaan.config(text=pertanyaan_ekstro[pertaanyaan_index_ekstro])
    # KUNCI PDF
                                        save_to_pdf(tingkat_stres_ekstro)

                                def hitung_tingkat_stres_ekstro(total_skor_ekstro):
                                    # Hitung tingkat stres berdasarkan total skor
                                    return total_skor_ekstro


                                # Pertanyaan
    # TOMBOLLLLLLLL
                                label_pertanyaan = tk.Label(tes_kesehatan_mental_ekstro, text=pertanyaan_ekstro[pertanyaan_index_ekstro], font=("Arial", 20,"bold"), bg= '#FAD5A6', fg='#545454')
                                label_pertanyaan.place(x= 50,y=443)

                                # Slideer jawaban
                                skala_var_ekstro = tk.DoubleVar()
                                skala_var_ekstro.set(1.0)  # Default nilai pertanyaan adalah 5.0

                                skala_ekstro = tk.Scale(tes_kesehatan_mental_ekstro, from_=1.0, to=10.0, orient=tk.HORIZONTAL, width = 20, variable=skala_var_ekstro, resolution=0.1, bg = '#FAD5A6')
                                skala_ekstro.place(x= 1175, y=443)

                                tombol_next_ekstro = tk.Button(tes_kesehatan_mental_ekstro, text= "Next", command=selanjutnya, font=("Arial", 16, "bold"), bg = '#A98F73', border=0, activebackground='#A98F73')
                                tombol_next_ekstro.place(x=1365, y=725)

                                tombol_back_ekstro = tk.Button(tes_kesehatan_mental_ekstro, text="Back", command= kembali, font=("Arial", 16, 'bold'),bg = '#A98F73', border=0, activebackground= '#A98F73' )
                                tombol_back_ekstro.place(x=1170, y=725)

                                tes_kesehatan_mental_ekstro.mainloop()

                                # Jalankan aplikasi
                            
                        # Akhir tes kesehatan mental ekstrovert
                            img_mental = Image.open('desain kesehatan mental.png')
                            img_bg_mental = img_mental.resize((1550,850), Image.Resampling.BICUBIC)
                            photo_mental =ImageTk.PhotoImage(img_bg_mental)

                            label_hasil_mental = tk.Label(halaman_tes_mental, image=photo_mental, bg='white', bd=0)
                            label_hasil_mental.place(x=0, y=0)

                            label_introvert = tk.Button(halaman_tes_mental, text = "Introvert", font = ("Arial", 22, "bold" ), bg ="#AB9175", command = mental_introvert, border=0, activebackground='#AB9175')
                            label_introvert.place(x= 235, y= 610)

                            label_introvert = tk.Button(halaman_tes_mental, text = "Ekstrovert", font = ("Arial", 22, "bold" ), bg ="#AB9175", command= mental_ekstrovert, border=0, activebackground='#AB9175')
                            label_introvert.place(x= 635, y= 610)

                            halaman_tes_mental.mainloop()

                        hasil_label = tk.Label(hasil_tes_kepribadian, text=f"{tingkat_stres}", font = ("Arial", 25, "bold"))
                        hasil_label.place(x=400, y=25)

                        if total_yes > total_no:
                            img_hasil_teskip = Image.open('desain ekstrovert.png')
                            img_bg_hasilteksip = img_hasil_teskip.resize((1550,850
                            ), Image.Resampling.BICUBIC)
                            photo_hasil_teksip =ImageTk.PhotoImage(img_bg_hasilteksip)

                            label_hasil_teksip = tk.Label(hasil_tes_kepribadian, image=photo_hasil_teksip, bg='white', bd=0)
                            label_hasil_teksip.place(x=0, y=0)

                            tes_selanjutnya = tk.Button(hasil_tes_kepribadian, text=" Tes Gangguan Mental", command= tes_mental, font = ("Arial", 20, 'bold'), border= 0, bg= '#AA8163', activebackground='#AA8163')
                            tes_selanjutnya.place(x=647, y=718)
                        elif total_yes < total_no:
                            img_hasil_teskip2 = Image.open('desain introvert.png')
                            img_bg_hasilteksip2 = img_hasil_teskip2.resize((1550,850
                            ), Image.Resampling.BICUBIC)
                            photo_hasil_teksip2 =ImageTk.PhotoImage(img_bg_hasilteksip2)

                            label_hasil_teksip2 = tk.Label(hasil_tes_kepribadian, image=photo_hasil_teksip2, bg='white', bd=0)
                            label_hasil_teksip2.place(x=0, y=0)

                            tes_selanjutnya2 = tk.Button(hasil_tes_kepribadian, text=" Tes Gangguan Mental", command= tes_mental, font = ("Arial", 20, 'bold'), border= 0, bg= '#AA8163', activebackground='#AA8163' )
                            tes_selanjutnya2.place(x=647, y=718)
                            
                        else:
                            messagebox.showinfo("Not Valid", f"Anda tidak mengisi jawaban")
                        hasil_tes_kepribadian.mainloop()

                    global total_yes, total_no
                    pertanyaan_index = 0
                    total_yes = 0
                    total_no = 0
                    pertanyaan = [
                        "1. Apakah Anda senang berinteraksi dengan orang lain? ",
                        "2. Apakah Anda merasa senang bekerja secara berkelompok dengan teman-teman Anda?",
                        "3. Apakah Anda mudah bergaul dengan orang lain?",
                        "4. Apakah Anda mudah terbuka terhadap perubahan dan hal baru? ",
                        "5. Apakah Anda merasa diri Anda adalah orang yang sangat bersemangat dan energik? ",
                        "6. Apakah Anda lebih senang bercerita kepada teman Anda mengenai kegiatan sehari-hari Anda? ",
                        "7. Apakah Anda suka datang ke pesta ulang tahun dan bersenang-senang dengan teman Anda? ",
                        "8. Apakah Anda lebih suka telepon dengan orang lain dari pada chatting dengan orang lain? ",
                        "9. Apakah Anda lebih suka mengutarakan apa yang Anda pikirkan dari pada memendamnya sendiri? ",
                        "10. Apakah Anda sering menjadi ketua dalam tugas kelompok? ",
                        "11. Apakah Anda sering mengeluarkan pendapat Anda meskipun harus berdebat dengan orang lain?",
                        "12. Apakah Anda lebih suka berbincang dengan topik ringan dari pada topik berat?",
                        "13. Apakah fokus Anda sering pecah saat ada sesuatu yang mendistraksi Anda?",
                        "14. Apakah Anda pandai mencari topik dan mencairkan suasana?",
                        "15. Apakah teman Anda sering mengatakan bahwa Anda memiliki public speaking yang bagus?"
                    ]
                    def kembali():
                        global pertanyaan_index
                        if pertanyaan_index > 0:
                            pertanyaan_index -= 1
                            label_pertanyaan.config(text=pertanyaan[pertanyaan_index])
                            

                    def selanjutnya():
                        global pertanyaan_index, total_yes, total_no
                        jawaban = answer_var.get()

                        if jawaban == "Yes":
                            total_yes += 1
                        elif jawaban == "No":
                            total_no += 1

                        pertanyaan_index += 1

                        if pertanyaan_index < len(pertanyaan):
                            label_pertanyaan.config(text=pertanyaan[pertanyaan_index])
                            answer_var.set(0)  # Reset radio button selection
                            if pertanyaan_index == len(pertanyaan) - 1:
                                tombol_selanjutnya.config(text = "Submit")
                        else:
                            hasil_tes = hitung_hasil_tes(total_yes, total_no)
                            hasil_kepribadian(hasil_tes)

                            pertanyaan_index = 0
                            total_yes = 0
                            total_no = 0
                            label_pertanyaan.config(text=pertanyaan[pertanyaan_index])
                            answer_var.delete(0,tk.END)

                    def hitung_hasil_tes(total_yes, total_no):
                        if total_yes > total_no:
                            return "Ekstrovert"
                        elif total_yes < total_no:
                            return "Introvert"
                        else:
                            return "Tidak Valid"

                    # Bg desain tes kepribadian
                    img_teskep = Image.open('desain tes kepribadian.png')
                    img_bg_teskep = img_teskep.resize((1550,850
                    ), Image.Resampling.BICUBIC)
                    photo_bg_teskep =ImageTk.PhotoImage(img_bg_teskep)

                    label_teskep = tk.Label(tes_kepribadian, image=photo_bg_teskep, bg='white', bd=0)
                    label_teskep.place(x=0, y=0)

                    label_pertanyaan = tk.Label(tes_kepribadian, text=pertanyaan[pertanyaan_index], font=("Arial", 20, "bold"), bg = "#FAD5A6", fg = '#545454')
                    label_pertanyaan.place(x=50, y=410)

                    answer_var = tk.StringVar()
                    # Radio Button Yes dan No
                    yes_radio = tk.Radiobutton(tes_kepribadian, text="Yes", variable=answer_var, value="Yes", font=("Arial", 14), bg = "#FAD5A6", fg = '#545454' )
                    yes_radio.place(x=100, y=453)

                    no_radio = tk.Radiobutton(tes_kepribadian, text="No", variable=answer_var, value="No", font=("Arial", 14), bg= "#FAD5A6", fg ='#545454'  )
                    no_radio.place(x=100, y=483)
                    # Tombol selanjutnya dan back
                    tombol_selanjutnya = tk.Button(tes_kepribadian, text="Next", command=selanjutnya, font= ("Arial", 16, 'bold'),bg = '#A98F73', border= 0, activebackground= '#A98F73' )
                    tombol_selanjutnya.place(x=1350, y=718)

                    tombol_back = tk.Button(tes_kepribadian, text="Back", command= kembali, font=("Arial", 16, 'bold'),bg = '#A98F73', border=0, activebackground= '#A98F73' )
                    tombol_back.place(x=1170, y=718)

                    tes_kepribadian.mainloop()
                # Bg desain kepribadian
                img_kepribadian = Image.open('desain kepribadian.png')
                img_bg_kepribadian = img_kepribadian.resize((1550,850))
                photo_bg_kepribadian = ImageTk.PhotoImage(img_bg_kepribadian)

                label_img_kepribadian = tk.Label(hal3_test, image=photo_bg_kepribadian, bg='white', bd=0)
                label_img_kepribadian.place(x=0, y=0)

                mulai_tes = tk.Button(hal3_test, text ="MULAI", font=('Arial', 22, 'bold'),  bg ="#A98F73", command = mulai, border=0, activebackground='#A98F73'  )
                mulai_tes.place(x= 580, y=658)
    # KUNCI PDF
                label_nama_pengguna = tk.Label(hal3_test, text="Nama Lengkap:", font=("Arial", 12), bg ="#A98F73")
                label_nama_pengguna.place(x=487, y=572)

                entry_nama_pengguna = tk.Entry(hal3_test, textvariable=nama_pengguna_var, font=("Arial", 12), bg ="#A98F73")
                entry_nama_pengguna.place(x=627, y=572)

                hal3_test.mainloop()

        test = tk.Button(hal1, text ="Pengerjaan\n Test", font=('Arial', 12, 'bold'),  bg ="#B6B4C6", border = 0,command = test, activebackground= "#B6B4C6" )
        test.place(x= 1047, y=551)

        # Gambar 3
        def hasil():
            hal4_SAD= tk.Toplevel(hal1)
            hal4_SAD.title("Registrasi")
            width, height = hal4_SAD.winfo_screenwidth(), hal4_SAD.winfo_screenheight()
            hal4_SAD.geometry(f"{width}x{height}")
            hal4_SAD.configure(bg="#C8E8F5")
            hal4_SAD.resizable(False,False)

            def stres():
                hal4_stres= tk.Toplevel(hal4_SAD)
                hal4_stres.title("Registrasi")
                width, height = hal4_stres.winfo_screenwidth(), hal4_stres.winfo_screenheight()
                hal4_stres.geometry(f"{width}x{height}")
                hal4_stres.configure(bg="#C8E8F5")
                hal4_stres.resizable(False,False)

                img_stres = Image.open('desain stres.png')
                img_stres = img_stres.resize((1550, 850))  # Resize the image
                photo_stres = ImageTk.PhotoImage(img_stres)

                label_img_stres = tk.Label(hal4_stres, image=photo_stres, bg='white', bd=0)
                label_img_stres.place(x=0, y=0)
                hal4_stres.mainloop()
            def anxiety():
                hal4_anxiety= tk.Toplevel(hal4_SAD)
                hal4_anxiety.title("Registrasi")
                width, height = hal4_anxiety.winfo_screenwidth(), hal4_anxiety.winfo_screenheight()
                hal4_anxiety.geometry(f"{width}x{height}")
                hal4_anxiety.configure(bg="#C8E8F5")
                hal4_anxiety.resizable(False,False)

                img_anxiety = Image.open('desain anxiety.png')
                img_anxiety = img_anxiety.resize((1550, 850))  # Resize the image
                photo_anxiety = ImageTk.PhotoImage(img_anxiety)

                label_img_anxiety = tk.Label(hal4_anxiety, image=photo_anxiety, bg='white', bd=0)
                label_img_anxiety.place(x=0, y=0)
                hal4_anxiety.mainloop()
            def depresi():
                hal4_depresi= tk.Toplevel(hal4_SAD)
                hal4_depresi.title("Registrasi")
                width, height = hal4_depresi.winfo_screenwidth(), hal4_depresi.winfo_screenheight()
                hal4_depresi.geometry(f"{width}x{height}")
                hal4_depresi.configure(bg="#C8E8F5")
                hal4_depresi.resizable(False,False)

                img_depresi = Image.open('desain depresi.png')
                img_depresi = img_depresi.resize((1550, 850))  # Resize the image
                photo_depresi = ImageTk.PhotoImage(img_depresi)

                label_img_depresi = tk.Label(hal4_depresi, image=photo_depresi, bg='white', bd=0)
                label_img_depresi.place(x=0, y=0)
                hal4_depresi.mainloop()

            img_SAD = Image.open('desain SAD.png')
            img_SAD = img_SAD.resize((1550, 850))  # Resize the image
            photo_SAD = ImageTk.PhotoImage(img_SAD)

            label_img_SAD = tk.Label(hal4_SAD, image=photo_SAD, bg='white', bd=0)
            label_img_SAD.place(x=0, y=0)  # Adjust the position of the image

            tombol_stres = tk.Button(hal4_SAD, text = "Stres", font=("Arial", 16, 'bold'), bg ='#F7995B', border =0, activebackground='#F7995B', command= stres)
            tombol_stres.place(x=160, y=582)

            tombol_anxiety = tk.Button(hal4_SAD, text = "Anxiety", font=("Arial", 16, 'bold'), bg ='#F7995B', border =0, activebackground='#F7995B', command = anxiety)
            tombol_anxiety.place(x=465, y=582)

            tombol_depresi = tk.Button(hal4_SAD, text = "Depresi", font=("Arial", 16, 'bold'), bg ='#F7995B', border =0, activebackground='#F7995B', command=depresi)
            tombol_depresi.place(x=765, y=582)


            hal4_SAD.mainloop()

        hasil = tk.Button(hal1, text ="SAD", font=('Arial', 13, 'bold'),  bg ="#B6B4C6", border = 0, command = hasil, activebackground= "#B6B4C6")
        hasil.place(x= 1325, y=556)

        hal1.mainloop()

    elif namapengguna != 'admin' and katakunci != '1234':
        messagebox.showerror("Invalid","Nama pengguna dan Kata kunci salah")
    elif namapengguna != 'admin' and katakunci == '1234':
        messagebox.showerror("Invalid","Nama pengguna salah")
    elif namapengguna == 'admin' and katakunci != '1234':
        messagebox.showerror("Invalid","Kata kunci salah")
    # akhir halaman pertama
# '''Mulai program Registrasi'''
def registrasi_command():
    window= Toplevel(window_loop)
    window.title("Registrasi")
    width, height = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry(f"{width}x{height}")
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

    img_bg_reg = Image.open('Register desain.png')
    img_reg = img_bg_reg.resize((1550, 870))
    photo_bg_reg =ImageTk.PhotoImage(img_reg)

    label_reg = tk.Label(window, image=photo_bg_reg, bg='white', bd=0)
    label_reg.place(x=0, y=0)

    # Nama pengguna
    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name=user.get()
        if name =='':
            user.insert(0,'Nama Pengguna')
    user = Entry(window, width=25, fg='black', border =0, bg='#F8F1C7', font=('Microsoft YaHei UI Light',11))

    user.place(x=630, y=470)
    user.insert(0,"Nama Pengguna")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(window,width=250,height=3,bg='white').place(x=55,y=107)
    # Password
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        kata=code.get()
        if kata =='*':
            code.insert(0,'Kata Kunci')
    code = Entry(window, width=25, fg='black', border =0, bg='#F8F1C7', font=('Microsoft YaHei UI Light',11))

    code.place(x=630, y=561)
    code.insert(0,'Kata Kunci')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
 
    # Konfirmasi kata kunci
    def on_enter(e):
        confirm.delete(0,'end')

    def on_leave(e):
        kata=confirm.get()
        if kata =='':
            confirm.insert(0,'Konfirmasi Kata Kanci')
    confirm = Entry(window, width=25, fg='black', border =0, bg='#F8F1C7', font=('Microsoft YaHei UI Light',11))

    confirm.place(x=630, y=655)
    confirm.insert(0,'Konfirmasi Kata Kunci')
    confirm.bind('<FocusIn>', on_enter)
    confirm.bind('<FocusOut>', on_leave)

    Button(window, width=15, pady =1, text='Register',bg='#B6B4C6', border = 0, command = registrasi, font=('Arial', 14, 'bold')).place(x = 700,y=712)
    label=Label(window, text="Sudah memiliki akun?",fg='black',bg='#F8F1C7',font=('Microsoft YaHei UI Light',9))
    label.place(x=710,y=764)

    sign_in = Button(window, width=6, text='Masuk', border=0, bg='#F8F1C7', cursor='hand2', fg='#FEB13D', command = sign )
    sign_in.place(x=840,y=764)

    window.mainloop()
# Akhir program registrasi
    
img_bg_login= Image.open('login jernih.png')
img_rentang2 = img_bg_login.resize((1550, 876))  
photo_bg_login = ImageTk.PhotoImage(img_rentang2)

label_img1_login = tk.Label(window_loop, image=photo_bg_login, bg='white', bd=0)
label_img1_login.place(x=0, y=0)

# Buat tempat input nama pengguna
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name =='':
        user.insert(0,'Nama Pengguna')
user = Entry(window_loop, width=25, fg='black', border =0, bg='#F8F1C7', font=('Microsoft YaHei UI Light',11))
user.place(x=630, y=470)
user.insert(0,'Nama Pengguna')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    kata=code.get()
    if kata =='':
        code.insert(0,'Kata Kunci') 
def show_pasword():
    if code.cget("show") == "*":
        code.config(show ='')

    else:
        code.config(show='*')

code = Entry(window_loop, width=25, fg='black', border =0, bg='#F8F1C7', font=('Microsoft YaHei UI Light',11))
code.place(x= 630, y=560)
code.insert(0,'Kata Kunci')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
check_button = Checkbutton(window_loop, text='', command= show_pasword, bg='#F8F1C7')
check_button.place(x=900, y=560)

# Tombol button
Button(window_loop, width=13, pady =1, text='Login',bg='#B6B4C6', border = 0, command = masuk, font = ("Arial", 14, "bold"), activebackground= "#B6B4C6" ).place(x = 706,y=628)
label=Label(window_loop, text="Belum memiliki akun?",fg='black',bg='#F8F1C7',font=('Microsoft YaHei UI Light',9))
label.place(x=690,y=675)

sign_up = Button(window_loop, width=6, text='Registrasi', border=0, bg='#F8F1C7', cursor='hand2', fg='#FEB13D', command= registrasi_command )
sign_up.place(x=830,y=675)

window_loop.mainloop()


