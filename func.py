import os #mengimport library os untuk berinteraksi dengan os 

# penampungan data 
namamahasiswa = [] #list untuk menampung inputan nama mahasiswa                                                                                 
nilaialgo = [] #list untuk menampung nilai dari mata kuliah algo
nilaiprpl = [] #list untuk menampung nilai dari mata kuliah prpl
nilaimatdas = [] #list untuk menampung nilai dari mata kuliah matdas
matkul = ["ALGO", "PRPL", "MATDAS"] #list untuk menampung matkul yang tersedia 
 
def clear (): #fungsi dengan nama clear
    os.system("cls") #menulis cls di terminal secara otomatis

def garis (): #fungsi dengan nama garis 
    print ("=" * 74) #mencetak "=" sebanyak 74 kali

def cover(): #fungsi dengan nama cover 
    garis() # memanggil fungsi garis yang mencetak "=" sebanyak 74 kali
    print ("\t\t       SISTEM PENILAIAN SEDERHANA") #mencetak tulisan sistem penilaian sederhana
    garis() #memanggil fungsi garis

def enter (): #fungsi dengan nama enter 
    enter = input ("tekan [ENTER] untuk melanjutkan") #membuat sebuah variabel enter yang berisi inputan apabila user menekan enter maka program akan berlanjut 

def menu (): #fungsi dengan nama menu, sebagai menu utama dalam program ini
    clear() #memanggil fungsi clear untuk membersihkan terminal dengan mengetik cls secara otomatis
    cover() #memanggil fungsi cover sebagai pemanis 
    print ("""
    MENU :
    1. INPUT NILAI MAHASISWA 
    2. DAFTAR NILAI MAHASISWA
    3. NILAI RATA RATA MATAKULIAH KESELURUHAN
    4. LAPORAN AKHIR
    5. TENTANG PEMBUAT PROGRAM
    6. KELUAR PROGRAM   
    """) #mencetak opsi opsi yang tersedia dalam program ini 
    garis () #memanggil fungsi garis untuk membatasi opsi dengan inputan user
    pilih = int (input ("masukkan pilihan program >>")) # membuat sebuah variabel bernama pilih yang berisi inputan nomor dari opsi yang dipilih user, inputan dalam bentuk integer
    if pilih == 1 : # jika input dari user berupa angka 1 
        inputan () # maka akan menjalankan atau memanggil fungsi inputan
    elif pilih == 2 : #jika input dari user berupa angka 2 
        daftar_nilai() #maka akan memanggil atau menjalankan fungsi daftar_nilai
    elif pilih == 3 : #jika inputan dari user berup angka 3 
        rata_rata_mata_kuliah() #maka akan memanggil atau menjalankan fungsi rata_rata_mata_kuliah
    elif pilih == 4 : #jika inputan user berupa angka 4
        tampilkan_laporan() #maka akan memanggil atau menjalankan fungsi tampilkan_laporan 
    elif pilih == 5 :
        pembuat() #memanggil fungsi pembuat untuk dijalankan
    else : #jika semua kondisi tidak terpenuhi 
        clear() # memanggil fungsi clear untuk clear terminal
        print ("terima kasih telah menggunakan program ini") #mencetak tulisan terima kasih

def inputan (): #fungsi dengan nama inputan, berisi berbagai inputan untuk user
    while True : #pengulangan tidak terbatas selama tidak bertemu break
        clear() # memanggil fungsi clear untuk membersihkan terminal
        cover() # memanggil fungsi cover sebagai pemanis
        namamhs = input ("masukkan nama mahasiswa :").upper() #membuat sebuah variabel dengan nama namamhs yang berisi inputan untuk nama mahasiswa, dengan huruf full kapital
        a = int (input ("masukkan nilai ALGO :")) #membuat variabel a yang berisi inputan niali matkul algo, dalam bentuk integer
        b = int (input ("masukkan nilai PRPL :")) # membuat variabel b yang berisi inputan nilai matkul prpl, dalam bentuk integer
        c = int (input ("masukkan nilai MATDAS :")) #membuat variabel c yang berisi inputan nilai matkul matdas, dalam bentuk integer
        namamahasiswa.append(namamhs) #memasukkan inputan nama mahasiswa ke dalam list namamahasiswa
        nilaialgo.append(a) #memasukkan inputan nilai matkul algo kedalam list nilaialgo
        nilaiprpl.append(b) #memasukkan inputan nilai prpl ke dalam list nilaiprpl
        nilaimatdas.append(c) #memasukkan inputan nilai matdas ke dalam list nilaimatdas
        print ("nilai berhasil di inputkan") # mencetak nilai berhaasil di input 
        garis() # memanggil fungsi garis sebagai pembatas 
        pilih = input ("Tambah data lagi atau tidak ? [y]/[t] >>").lower() #membuat variabel pilih yang berisi inputan user untuk melanjutkan input nama atau tidak
        if pilih == "y": # jika input dari user adalah 'y'
            continue #program akan terus berlanjut
        elif pilih == "t": #jika inputan dari user adalah 'n'
            break #pengulangan berhenti 
    enter() #memanggil fungsi enter sebagai pembatas, sebelum ke fungsi menu  
    menu () #kembali ke menu, memanggil fungsi menu 

def daftar_nilai(): # fungsi dengan nama daftar_nilai, yang dapat menampilkan inputan yang telah diberikan oleh user 
    clear() # memanggil fungsi clear untuk membersihkan terminal
    cover() # memanggil fungsi cover untuk pemanis
    nama = namamahasiswa #memanggil atau memasukkan list namamahasiswa ke dalam variabel nama
    algo = nilaialgo # memanggil atau memasukkan list nilaialgo ke dalam variabel algo
    prpl = nilaiprpl # memanggil atau memasukkan list nilaiprpl ke dalam variabel prpl
    matdas = nilaimatdas # memanggil atau memasukkan list nilaimatdas ke dalam variabel matdas
    border = ["NO", "NAMA MAHASISWA", "NILAI ALGO", "NILAI PRPL", "NILAI MATDAS"] #membuat list yang berisi tentang nama mahasiswa dan matkul yang akan ditampilkan sebagai border dari tabel
    garis () #memanggil fungsi garis sebagai garis atas dari tabel
    print (f"|{border[0]:>3}|{border[1]:>20}|{border[2]:>15}|{border[3]:>15}|{border[4]:>15}|") #menampilkan setiap value index awal hingga akhir pada variabel border dan membentuk menyerupai tabel yang masing masing luasnya telah diatur dengan code dibelakang variabel border 
    garis () #memanggil fungsi garis sebagai pembatas border dengan isi tabel 
    for i in range (len(nama)): #pengulangan dengan range 0 sampai dengan jumlah value yang ada pada list nama, pengulangan ini berfungsi sebagai index untuk memanggil value dalam list yang ada di code selanjutnya
        print (f"|{i+1:>3}|{nama[i]:>20}|{algo[i]:>15}|{prpl[i]:>15}|{matdas[i]:>15}|") #mencetak isi dari tabel yang berupa list nama, algo, prpl, matdas pada index ke i(0 sampai dengan jumlah value yang ada pada list nama )
        print ("-"*74) #mencetak "-" sebanyak 74 kali, sebagai pembatas antara isi dengan isi yang lain
    garis() #memanggil fungsi garis, sebagai pembatas paling bawah tabel
    enter() #memanggil fungsi enter sebagai pembatas, sebelum kembali ke fungsi menu 
    menu() #kembali ke menu, memanggil kembali fungsi menu

    
def hitung_rata_rata (): #fungsi dengan nama hitung rata rata yang befungsi mengolah nilai yang telah di inputkan untuk menjadi nilai rata rata mahasiswa
    ratamhs = [] #variabel berupa list dengan nama ratamhs yang berfungsi menampung nilai rata rata mahasiswa yang telah di olah
    for i in range (len(nilaialgo)): #pengulangan yang memiliki kegunaan yang sama seperti pengulangan pada fungsi daftar_nilai, yaitu sebagai index untuk pemanggilan value dalam list pada code dibawah 
        jml = nilaialgo[i] + nilaimatdas[i] + nilaiprpl[i] #membuat variabel dengan nama jumlah yang berisi penjumlahan dari nilaialgo, nilaimatdas, nilai prpl  pada index ke i
        rata = jml/3  #membuat variabel dengan nama rata yang berisi hasil dari pembagian jumlah nilai matkul dengan 3 matkul
        ratamhs.append(rata) #memasukkan hasil dari variabel rata ke dalam list ratamhs
    return ratamhs #mengembalikan nilai pada variabel ratamhs ke fungsi hitung_rata_rata, sehingga jika fungsi ini dipanggil akan memunculkan nilai rata rata dari mahasiswa


def tentukan_grade (): #fungsi bernama tentukan_grade yang berfungsi untuk menentukan grade dari nilai rata rata mahasiswa
    grademhs = [] #variabel dengan nama grademhs yang berfungsi untuk menampung grade dari mahasiswa 
    ratamhs = hitung_rata_rata() #memanggil fungsi hitung_rata_rata dan dimasukkan ke dalam variabel ratamhs
    for i in range (len(ratamhs)): #pengulangan yang memiliki kegunaan yang sama seperti pengulangan pada fungsi daftar_nilai, melakukan pengungalan  dari 0 sampai dengan jumlah value yang ada pada list ratamhs, pengulangan ini berfungsi sebagai index  untuk memanggil value dalam list pada code dibawah
        if ratamhs[i] >= 85 : #jika nilai ratamhs pada index ke i >= 85 
            grade = "A"  #membuat variabel dengan nama grade yang berisi nilai "A" jika nilai ratamhs >= 85
        elif ratamhs[i] < 85 and ratamhs[i] >= 70 : #jika nilai ratamhs pada index ke i berada pada range 70 sampai 85 
            grade = "B" #variabel grade akan  berisi nilai "B" jika nilai ratamhs pada index ke i berada pada range yang telah disebutkan
        elif ratamhs[i] >= 50 and ratamhs[i] < 70 :  #jika nilai ratamhs pada index ke i berada pada range 50 sampai dengan 70 
            grade = "C"  #variabel grade akan berisi nilai "C" jika nilai ratamhs pada index ke i berada pada range yang telah disebutkan
        elif ratamhs[i] < 50 : #jika ratamhs lebih kecil dari 50
            grade = "D"  #variabel grade akan berisi nilai "D" jika nilai ratamhs pada index ke i lebih kecil dari 50
        grademhs.append(grade) #memasukkan nilai dari variabel grade ke dalam list grademhs
    return grademhs #mengembalikan nilai grademhs ke fungsi tentukan_grade, jika fungsi tersebut dipanggil akan menghasilkan nilai yang sama dengan nilai dari grademhs

        
def rata_rata_mata_kuliah (): #fungsi dengan nama rata_rata_mata_kuliah yang berisi rata rata nilai dari setiap mata kuliah yaitu algo, prpl dan matdas
    clear() #memanggil fungsi clear, untuk membersihkan terminal
    cover () # memanggil fungsi cover sebagai pemanis 
    nilai_rata_matkul = [] #variabel dalam bentuk list bernama nilai_rata_matkul yang berfungsi untuk menammpung nilai rata rata dari setiap mata kuliah
    listmatkul = matkul #memanggil list matkul ke dalam  variabel listmatkul
    algo = nilaialgo  #memanggil list nilai algo ke dalam variabel algo
    prpl = nilaiprpl #memanggil list nilai prpl ke dalam variabel prpl
    matdas = nilaimatdas  #memanggil list nilai matdas ke dalam variabel matdas
    rata_algo = (sum(algo))/len(algo)  #membuat variabel dengan nama rata_algo yang berisi hasil dari penjumlahan smeua value dalam variabel algo dan membaginya dengan banyaknya value dalam variabel algo
    rata_prpl = (sum(prpl))/len(prpl)   #membuat variabel dengan nama rata_prpl yang berisi hasil dari penjumlahan semua value dalam variabel prpl dan membaginya dengan banyaknya value dalam variabel prpl
    rata_matdas = (sum(matdas))/len(matdas) #membuat variabel dengan nama rata_matdas yang berisi hasil dari penjumlahan semua value dalam variabel matdas dan membaginya dengan banyaknya value dalam variabel matdas
    nilai_rata_matkul.append(rata_algo)  #memasukkan nilai dari variabel rata_algo ke dalam list nilai_rata_matkul
    nilai_rata_matkul.append(rata_prpl) #memasukkan nilai dari variabel rata_prpl ke dalam list nilai_rata_matkul
    nilai_rata_matkul.append(rata_matdas) #memasukkan nilai dari variabel rata_matdas ke dalam list nilai_rata_matkul
    for i in range (len (nilai_rata_matkul)): #pengulangan yang berfungsi sebagai index untuk memanggil setiap nilai dalam list dibawahnya, dimulai dari index ke 0 hingga banyaknya value pada list nilai_rata_matkul
        nilai_rata_matkul[i] = f"{nilai_rata_matkul[i]:.2f}" #memanggil setiap value dari variabel nilai _rata_matkul dan mengubah menjadi hanya ada 2 angka dibelakang koma
    border = ["NO","MATA KULIAH", "NILAI RATA RATA"] #membuat list border, yang berfungsi menampung value untuk isi dari border 
    garis() #memanggil fungsi garis sebagai pembatas bagian atas tabel
    print(f"|{border[0]:>3}|{border[1]:>32} |{border[2]:>33}|") #mencetak isi dari list border ke dalam bentuk tabel, sbeagai border dari tabel tersebut
    garis() #memanggil fungsi garis pembatas antara border dengan isi dari tabel
    for i in range (len (nilai_rata_matkul)): #pengulangan yang memiliki kegunaan yang sama pada pengulangan pada  fungsi daftar_nilai, yaitu sebagai index untuk memanggil setiap value dalam list dibawah ini
        print (f"|{i+1:>3}|{listmatkul[i]:>32} |{nilai_rata_matkul[i]:>33}|") #mencetak isi dari tabel berupa list matakuliah dan nilai rata rata nya. dipanggil dengan menggunakan index ke i 
        print ("-"*74) #mencetak "-"sebanyak 74 kali sebagai pembatas antara isi dengan isi yang lain
    garis() #memanggil fungsi garis  sebagai pembatas bagian bawah tabel
    enter () #memanggil fungsi enter sebagai pembatas dengan fungsi menu
    menu() # kembali ke menu, memanggil ulang fungsi menu
    
def tampilkan_laporan (): #fungsi dengan nama tampilkan_laporan yang berisi laporan akhir dari nilai rata rata mahassiswa dan grade dari mahasiswa
    clear() #memanggil fungsi clear untuk membersihkan terminal
    cover() # memanggil fungsi cover untuk pemanis
    ratamhs = hitung_rata_rata() #memanggil fungsi hitung_rata_rata ke dalam variabel ratamhs
    for i in range (len(ratamhs)):  #pengulangan yang memiliki kegunaan yang sama seperti pengulangan pertama pada fungsi rata_rata_mata_kuliah , yaitu sebagai index untuk memanggil setiap value dalam list, dimulai dari index 0 hingga banyak value dalam variabel ratamhs
        ratamhs[i] = f"{ratamhs[i]:.2f}" #memanggil setiap value dari list ratamhs  dan mengubah menjadi hanya ada 2 angka dibelakang koma
    grade = tentukan_grade() #memanggil fungsi tentukan_grade ke dalam variabel grade
    nama = namamahasiswa #memanggil variabel namamahasiswa ke dalam variabel nama
    border = ["NO", "NAMA MAHASISWA", "NILAI RATA RATA MAHASISWA","GRADE" ] #membuat list border yang berfungsi sebagai pembatas tabel
    garis() #memanggil fungsi garis untuk pembatas atas dari tabel
    print (f"|{border[0]:>3}|{border[1]:>25}|{border[2]:>30}|{border[3]:>10}|") #mencetak isi dari list border menjadi border dari tabel
    garis() #memanggil  fungsi garis sebagai pembatas antara border dengan isi tabel
    for i in range (len(namamahasiswa)): #pengulangan untuk memanggil index  setiap value dalam list dibawahnya, dimulai dari index 0 hingga banyak value dari list nama mahasiswa
        print (f"|{i+1:>3}|{nama[i]:>25}|{ratamhs[i]:>30}|{grade[i]:>10}|") #mencetak isi dari tabel yang meliputi no, nama mahasiswa, nilai rata rata mahasiswa, dan grade nya, dicetak menggunakan index dari perulangan berupa i 
        print ("-"*74) #menceatk  "-" sebanyak 74 kali sebagai pembatas antara isi tabel dengan isi tabel yang lain
    garis() #memanggil  fungsi garis sebagai pembatas bagian bawah tabel
    enter() #memanggil fungsi enter sebagai pembatas sebelum kembali ke fungsi menu
    menu () #kembali ke menu, memanggil kembali fungsi menu 

def pembuat():
    clear() #memanggil fungsi clear untuk membersihkan terminal
    cover() # memanggil fungsi cover sebagai pemanis
    garis() #memanggil fungsi garis sebagai pembatas bagian atas 
    print ("""
PEMBUAT PROGRAM :
           
NAMA  : TUNGGUL ABDUL MAJID 
PRODI : TEKNOLOGI INFORMASI - UNIVERSITAS JEMBER
NIM   : 242410102058
""") #mencetak informasi tentang pembuat program
    garis()  #memanggil fungsi garis sebagai pembatas bagain bawah
    enter() #memanggil fungsi enter sebagai pembatas sebelum kembali ke fungsi menu
    menu() #kembali ke menu, memanggil kembali fungsi menu
    
if __name__ == "__main__": #pembatas antara program utama (program yang akan dijalankan pertama kali) dengan program yang berisi fungsi fungsi  
    menu () #memanggil fungsi menu untuk dijalankan pertama kali, sebagai awal dari program utama

    