import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

total_skor_intro = 0
pertanyaan_index_intro = 0
pertanyaan_index_ekstro = 0
total_skor_ekstro = 0


tes_kepribadian = tk.Tk()
tes_kepribadian.title("Mental Health Tracker")
tes_kepribadian.geometry("925x500")
tes_kepribadian.configure(bg="white")
tes_kepribadian.resizable(False, False)

def hasil_kepribadian(tingkat_stres, jawaban_pertanyaan):
    hasil_tes_kepribadian = tk.Toplevel(tes_kepribadian)
    hasil_tes_kepribadian.title("Hasil dan Rekomendasi")
    hasil_tes_kepribadian.geometry("925x500")
    hasil_tes_kepribadian.resizable(False, False)
        
    def tes_mental():
        halaman_tes_mental = tk.Toplevel(hasil_tes_kepribadian)
        halaman_tes_mental.title("Mental Health Test")
        halaman_tes_mental.geometry("925x500")
        halaman_tes_mental.resizable(False, False)

    #  Awal tes kesehatan mental introvert
        def mental_introvert():
            tes_kesehatan_mental_intro = tk.Toplevel(halaman_tes_mental)
            tes_kesehatan_mental_intro.title("Mental Health Tracker")
            tes_kesehatan_mental_intro.geometry("925x500")
            tes_kesehatan_mental_intro.configure(bg="white")
            tes_kesehatan_mental_intro.resizable(False,False)
    
            # Def rekomendasi bisa diisi rekomendasinya pake label
            def hasil_rekomendasi_intro(tingkat_stres):
              
                hasil_jendela = tk.Toplevel(tes_kesehatan_mental_intro)
                hasil_jendela.title("Hasil dan Rekomendasi")
                hasil_jendela.geometry("925x500")
                hasil_jendela.resizable(False,False)

                hasil_label = tk.Label(hasil_jendela, text=f"Tingkat stres Anda: {tingkat_stres}")
                hasil_label.pack(pady=10)

                rekomendasi_label = tk.Label(hasil_jendela, text=f"Rekomendasi: {rekomendasi_pengobatan_intro(tingkat_stres)}")
                rekomendasi_label.pack(pady=10)


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

            def hitung_tingkat_stres(total_skor_intro):
                # Hitung tingkat stres berdasarkan total skor
                return total_skor_intro

            def rekomendasi_pengobatan_intro(tingkat_stres):
                # Tentukan rekomendasi pengobatan berdasarkan tingkat stres
                if tingkat_stres <= 20:
                    return "Tingkat stres sangat rendah 😊"
                elif 20 < tingkat_stres <= 50:
                    return "Tingkat stres rendah 🙂"
                elif 50 < tingkat_stres <= 80:
                    return "Tingkat stres tinggi 😐"
                else:
                    return "Tingkat stres sangat tinggi 😫"

            # Buat tes_kesehatan_mental_intro utama
            label_soal = tk.Label(tes_kesehatan_mental_intro,text ="Tes Gangguan Mental", font = ("Arial", 14, "bold" ) )
            label_soal.place(x=10,y=20)

            label_soal = tk.Label(tes_kesehatan_mental_intro,text ="Terdapat 10 butir pertanyaan. Baca dan pahami baik-baik setiap pertanyaan. Tidak ada jawaban benar dan salah. Anda diminta untuk memilih\n jawaban yang paling sesuai dengan kondisi Anda dengan pilihan jawaban skala 1.0 sampai 10.0:", font = ("Times New Roman", 12 ), anchor = "w", justify= "left" )
            label_soal.place(x=10,y=50)
            # Pertanyaan
            label_pertanyaan = tk.Label(tes_kesehatan_mental_intro, text=pertanyaan_intro[pertanyaan_index_intro], font=("Arial", 12,"bold"))
            label_pertanyaan.place(x= 10,y=230)

            # Gambar Rentang
            img_rentang = Image.open('Rentang.png')
            img_rentang1 = img_rentang.resize((500, 110))  
            photo_rentang = ImageTk.PhotoImage(img_rentang1)

            label_img1 = tk.Label(tes_kesehatan_mental_intro, image=photo_rentang, bg='white', bd=0)
            label_img1.place(x=200, y=100)

            # Slideer jawaban
            skala_var = tk.DoubleVar()
            skala_var.set(1.0)  # Default nilai pertanyaan adalah 5.0

            skala_intro = tk.Scale(tes_kesehatan_mental_intro, from_=1.0, to=10.0, orient=tk.HORIZONTAL, variable=skala_var, resolution=0.1)
            skala_intro.place(x= 800, y=210)

            tombol_next = tk.Button(tes_kesehatan_mental_intro, text= "selanjutnya", command=selanjutnya)
            tombol_next.place(x=440, y=400)

            # Jalankan aplikasi
            tes_kesehatan_mental_intro.mainloop()
    # Akhir tes kesehatan mental introvert
    
    # Awal tes kesehatan mental ekstrovert
        def mental_ekstrovert():

            tes_kesehatan_mental_ekstro = tk.Toplevel(halaman_tes_mental)
            tes_kesehatan_mental_ekstro.title("Mental Health Tracker")
            tes_kesehatan_mental_ekstro.geometry("925x500")
            tes_kesehatan_mental_ekstro.configure(bg="white")
            tes_kesehatan_mental_ekstro.resizable(False,False)

            # Def rekomendasi bisa diisi rekomendasinya pake label
            def hasil_jendela_ekstro(tingkat_stres_ekstro):

                hasil_ekstro = tk.Toplevel(tes_kesehatan_mental_ekstro)
                hasil_ekstro.title("Hasil dan Rekomendasi")
                hasil_ekstro.geometry("925x500")
                hasil_ekstro.resizable(False,False)

                hasil_label_ekstro = tk.Label(hasil_ekstro, text=f"Tingkat stres Anda: {tingkat_stres_ekstro}")
                hasil_label_ekstro.pack(pady=10)

                rekomendasi_label_ekstro = tk.Label(hasil_ekstro, text=f"Rekomendasi: {rekomendasi_ekstro(tingkat_stres_ekstro)}")
                rekomendasi_label_ekstro.pack(pady=10)


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

            def hitung_tingkat_stres_ekstro(total_skor_ekstro):
                # Hitung tingkat stres berdasarkan total skor
                return total_skor_ekstro

            def rekomendasi_ekstro(tingkat_stres_ekstro):
                # Tentukan rekomendasi pengobatan berdasarkan tingkat stres
                if tingkat_stres_ekstro <= 20:
                    return "Tingkat stres sangat rendah 😊"
                elif 20 < tingkat_stres_ekstro <= 50:
                    return "Tingkat stres rendah 🙂"
                elif 50 < tingkat_stres_ekstro <= 80:
                    return "Tingkat stres tinggi 😐"
                else:
                    return "Tingkat stres sangat tinggi 😫"

            # Buat tes_kesehatan_mental_ekstro utama
            label_soal_ekstro = tk.Label(tes_kesehatan_mental_ekstro,text ="Tes Gangguan Mental", font = ("Arial", 14, "bold" ) )
            label_soal_ekstro.place(x=10,y=20)

            label_soal_ekstro = tk.Label(tes_kesehatan_mental_ekstro,text ="Terdapat 10 butir pertanyaan. Baca dan pahami baik-baik setiap pertanyaan. Tidak ada jawaban benar dan salah. Anda diminta untuk memilih\n jawaban yang paling sesuai dengan kondisi Anda dengan pilihan jawaban skala 1.0 sampai 10.0:", font = ("Times New Roman", 12 ), anchor = "w", justify= "left" )
            label_soal_ekstro.place(x=10,y=50)
            # Pertanyaan
            label_pertanyaan = tk.Label(tes_kesehatan_mental_ekstro, text=pertanyaan_ekstro[pertanyaan_index_ekstro], font=("Arial", 12,"bold"))
            label_pertanyaan.place(x= 10,y=230)

            # Gambar Rentang
            img_rentang_ekstro = Image.open('Rentang.png')
            img_rentang2 = img_rentang_ekstro.resize((500, 110))  
            photo_rentang_ekstro = ImageTk.PhotoImage(img_rentang2)

            label_img1 = tk.Label(tes_kesehatan_mental_ekstro, image=photo_rentang_ekstro, bg='white', bd=0)
            label_img1.place(x=200, y=100)

            # Slideer jawaban
            skala_var_ekstro = tk.DoubleVar()
            skala_var_ekstro.set(1.0)  # Default nilai pertanyaan adalah 5.0

            skala_ekstro = tk.Scale(tes_kesehatan_mental_ekstro, from_=1.0, to=10.0, orient=tk.HORIZONTAL, variable=skala_var_ekstro, resolution=0.1)
            skala_ekstro.place(x= 650, y=210)

            tombol_next_ekstro = tk.Button(tes_kesehatan_mental_ekstro, text= "selanjutnya", command=selanjutnya)
            tombol_next_ekstro.place(x=440, y=400)

            # Jalankan aplikasi
            tes_kesehatan_mental_ekstro.mainloop()

        label_mental = tk.Label(halaman_tes_mental, text = "Tes Kesehatan Mental", bg= 'white', font = ("Arial", 25, "bold"))
        label_mental.place(x=280, y=60)

        label_mental_2 = tk.Label(halaman_tes_mental, text = "Tes kesehatan mental dilakukan untuk mengukur dan memahami kondisi kesehatan mental seseorang. Termasuk\ngangguan mental seperti stres, depresi dan kecemasan. Carl Rogers, tokoh utama psikoterapi, menekankan\nbahwa pentingnya pemahaman, empati, dan penerimaan tanpa syarat dalam mendukung pertumbuhan individu.", bg= 'white', font = ("Arial", 12), anchor = "w", justify= "left")
        label_mental_2.place(x=70, y=150)

        label_hal3_3 = tk.Label(halaman_tes_mental, text = "Yuk langsung \"mulai\" sesuai kepribadianmu untuk mengikuti tesnya!", bg= 'white', font = ("Arial", 16, "bold"))
        label_hal3_3.place(x=120, y=250)

        label_introvert = tk.Button(halaman_tes_mental, text = "Introvert", font = ("Arial", 14, "bold" ), bg ="#C8E8F5", command = mental_introvert)
        label_introvert.place(x= 350, y= 400)

        label_introvert = tk.Button(halaman_tes_mental, text = "Ekstrovert", font = ("Arial", 14, "bold" ), bg ="#C8E8F5", command= mental_ekstrovert)
        label_introvert.place(x= 500, y= 400)

    jawaban_label = tk.Label(hasil_tes_kepribadian, text=f"Jawaban Pertanyaan:\n{', '.join(jawaban_pertanyaan)}", font=("Arial", 12))
    jawaban_label.pack(pady=10)

    hasil_label = tk.Label(hasil_tes_kepribadian, text=f"Hasil Tes: {tingkat_stres}")
    hasil_label.pack(pady=10)

    rekomendasi_label = tk.Label(hasil_tes_kepribadian, text=f"Rekomendasi: {rekomendasi_pengobatan(tingkat_stres)}")
    rekomendasi_label.pack(pady=10)

    tes_selanjutnya = tk.Button(hasil_tes_kepribadian, text=" Tes Gangguan Mental", command= tes_mental)
    tes_selanjutnya.place(x=420, y=400)
    hasil_tes_kepribadian.mainloop()

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
jawaban_pertanyaan = []
def kembali():
    global pertanyaan_index
    if pertanyaan_index > 0:
        pertanyaan_index -= 1
        label_pertanyaan.config(text=pertanyaan[pertanyaan_index])
        

def selanjutnya():
    global pertanyaan_index, total_yes, total_no, jawaban_pertanyaan
    jawaban = answer_var.get()
  
    jawaban_pertanyaan.append(jawaban)
    if jawaban == "Yes":
        total_yes += 1
    elif jawaban == "No":
        total_no += 1

    pertanyaan_index += 1

    if pertanyaan_index < len(pertanyaan):
        label_pertanyaan.config(text=pertanyaan[pertanyaan_index])
        answer_var.set(None)  # Reset radio button selection
        if pertanyaan_index == len(pertanyaan) - 1:
            tombol_selanjutnya.config(text = "Submit")
    else:
        hasil_tes = hitung_hasil_tes(total_yes, total_no)
        hasil_kepribadian(hasil_tes)
        messagebox.showinfo("Saved", f"Jawaban Anda telah tersimpan")

        pertanyaan_index = 0
        total_yes = 0
        total_no = 0
        jawaban_pertanyaan = []
        label_pertanyaan.config(text=pertanyaan[pertanyaan_index])

def hitung_hasil_tes(total_yes, total_no):
    if total_yes > total_no:
        return "Introvert"
    elif total_yes < total_no:
        return "Ekstrovert"
    else:
        return "Anda tidak menjawab satupun soal"

def rekomendasi_pengobatan(hasil_tes):
    if hasil_tes == "Introvert":
        return "Rekomendasi pengobatan untuk Introvert."
    elif hasil_tes == "Ekstrovert":
        return "Rekomendasi pengobatan untuk Ekstrovert."
    else:
        return "Tidak ada rekomendasi."

# Label label
label_soal = tk.Label(tes_kepribadian, text="Tes Kepribadian", font=("Arial", 14, "bold"))
label_soal.place(x=10, y=20)

label_soal = tk.Label(tes_kepribadian, text="Terdapat 15 butir pertanyaan. Baca dan pahami baik-baik setiap pertanyaan. Tidak ada jawaban benar dan salah. Anda diminta untuk memilih\n jawaban yang paling sesuai dengan kondisi Anda dengan pilihan jawaban 'Yes' dan 'No':", font=("Times New Roman", 12), anchor="w", justify="left")
label_soal.place(x=10, y=50)

label_pertanyaan_2 = tk.Label(tes_kepribadian, height= 6, width= 500, text="", bg = "#C8E8F5")
label_pertanyaan_2.place(x=0, y=230)

label_pertanyaan = tk.Label(tes_kepribadian, text=pertanyaan[pertanyaan_index], font=("Arial", 12, "bold"), bg = "#C8E8F5")
label_pertanyaan.place(x=10, y=230)

answer_var = tk.StringVar()
# Radio Button Yes dan No
yes_radio = tk.Radiobutton(tes_kepribadian, text="Yes", variable=answer_var, value="Yes", font=("Arial", 12), bg = "#C8E8F5" )
yes_radio.place(x=50, y=260)

no_radio = tk.Radiobutton(tes_kepribadian, text="No", variable=answer_var, value="No", font=("Arial", 12), bg= "#C8E8F5"  )
no_radio.place(x=50, y=290)
# Tombol selanjutnya dan back
tombol_selanjutnya = tk.Button(tes_kepribadian, text="Next", command= selanjutnya, font= ("Arial", 11) )
tombol_selanjutnya.place(x=500, y=400)

tombol_back = tk.Button(tes_kepribadian, text="Back", command= kembali, font=("Arial", 11))
tombol_back.place(x=400, y=400)

tes_kepribadian.mainloop()


