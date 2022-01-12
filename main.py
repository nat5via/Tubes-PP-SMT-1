#UI pilihan menu
print("="*58)
print("\t\t    Selamat Datang!")
print("\t    Silakan pilih menu di bawah ini!")
print("="*58)
print("\t (1) Lihat Daftar Penjualan")                      #Melihat list "penjualan"
print("\t (2) Lihat Daftar Penghasilan Setiap Pramuniaga")  #Melihat fungsi penghasilan
print("\t (3) Lihat Daftar Bonus Pramuniaga")               #Melihat fungsi bonus
print("\t (4) Keluar")                                      #Keluar dari program
print("="*58)
print("\t  Created by: Novia Natasya (1301213259)")
print("="*58)
pilihan_menu = input("Pilih menu: ") # Meminta user untuk memilih menu yang tersedia
print()

#Soal bagian a
def baca_data(filename):
    file = open(filename, "r")  # baca data line pertama dari file txt
    teks = file.readline() # ganti readlines

    penjualan = [] #buat list kosong
    while teks != "": #for item in teks
        dict_penjualan = {}
        a = teks.split() # ubah file teks per baris menjadi list 
        b = {"nama": a[0],    # susun data yang dibaca ke dalam dictionary
             "senin": int(a[1]),
             "selasa": int(a[2]),
             "rabu": int(a[3]),
             "kamis": int(a[4]),
             "jumat": int(a[5])} 
        dict_penjualan[a[0]] = b  # menambahkan key dan value
        penjualan.append(b) # dictionary diappend (ditambahkan) ke dalam list
        teks = file.readline() # baca data baris selanjutnya
    #print(penjualan)
    return penjualan

nama_file = "daftarpramuniaga.txt"
penjualan = baca_data(nama_file)  # Memanggil fungsi baca_data

#fungsi untuk mengakses pasangan key:value nama (list comprehension)
def print_name():
    names = [names["nama"] for names in penjualan]
    return names

list_nama = print_name() # Membuat list nama pramuniaga = [orang 1, orang 2, orang 3]

#fungsi utk menampilkan data penjualan
def print_data(data):
    i = 0
    for elemen in data: #elemen = dictionary dari list penjualan
        print(">",list_nama[i])
        for key in elemen: #key dari setiap dict yang ada di list penjualan
            if key != "nama":
                print("---","Hari",key,"=",elemen[key])
        print()
        i += 1

new_penjualan = [{k: v for k, v in d.items() if k != 'nama'} for d in penjualan] #Hapus key nama di setiap dict dalam list

#soal bagian b
def penghasilan(): #value dari senin hingga jumat dijumlah
    #Total penjualan
    print("Total Penjualan setiap pramuniaga di akhir minggu (tanpa upah):")
    print("-"*63)
    
    #Total Aradea
    nama1 = list_nama[0]
    dict_orang1 = new_penjualan[0]
    values_orang1 = dict_orang1.values()
    total_orang1 = sum(values_orang1)

    #Total Safwan
    nama2 = list_nama[1]
    dict_orang2 = new_penjualan[1]
    values_orang2 = dict_orang2.values()
    total_orang2 = sum(values_orang2)

    #Total Fatima
    nama3 = list_nama[2]
    dict_orang3 = new_penjualan[2]
    values_orang3 = dict_orang3.values()
    total_orang3 = sum(values_orang3)

    print(">", nama1, ":", total_orang1*1000)
    print(">", nama2, ":", total_orang2*1000)
    print(">", nama3, ":", total_orang3*1000)
    print()

    #Gaji tetap (not include insentif + bonus)
    print("Penghasilan pramuniaga di akhir minggu (tidak termasuk insentif + bonus):")
    print("-"*73)
    total_orang1 = (sum(values_orang1) + 100*5)*1000
    total_orang2 = (sum(values_orang2) + 100*5)*1000
    total_orang3 = (sum(values_orang3) + 100*5)*1000
    print(">", nama1, ":", total_orang1)
    print(">", nama2, ":", total_orang2)
    print(">", nama3, ":", total_orang3)
    print()

    #insentif
    #cek Aradea
    if total_orang1 > 0:
        insentif_orang1 = total_orang1*25/1000
        total_orang1 = total_orang1 + insentif_orang1
    #cek Safwan
    if total_orang2 > 0:
        insentif_orang2 = total_orang2*25/1000
        total_orang2 = total_orang2 + insentif_orang2
    #cek Fatima
    if total_orang3 > 0:
        insentif_orang3 = total_orang3*25/1000
        total_orang3 = total_orang3 + insentif_orang3
    
    #Gaji tetap + insentif (not include bonus)
    print("Penghasilan pramuniaga di akhir minggu + insentif (tidak termasuk bonus):")
    print("-"*73)
    print(">", nama1, ":", int(total_orang1))
    print(">", nama2, ":", int(total_orang2))
    print(">", nama3, ":", int(total_orang3))
    print()

#soal bagian c
def bonus():
    print("\tPramuniaga yang mendapatkan bonus:")
    print("-"*55)
   #cek Aradea
    nama1 = list_nama[0]
    dict_orang1 = new_penjualan[0]
    values_orang1 = dict_orang1.values()
    total_orang1 = sum(values_orang1)
    total_orang1 = (sum(values_orang1) + 100)*1000
    if total_orang1 > 20000000:
        bonus_orang1 = int(total_orang1 + 1000000)
        print(">", nama1, "mendapatkan bonus sebesar:", bonus_orang1)
        print("\tTotal penghasilan akhir: ", total_orang1 + bonus_orang1)

    #cek Safwan
    nama2 = list_nama[1]
    dict_orang2 = new_penjualan[1]
    values_orang2 = dict_orang2.values()
    total_orang2 = sum(values_orang2)
    total_orang2 = (sum(values_orang2) + 100)*1000
    if total_orang2 > 20000000:
        bonus_orang2 = int(total_orang2 + 1000000)
        print(">", nama2, "mendapatkan bonus sebesar:", bonus_orang2)
        print("\tTotal penghasilan akhir: ", total_orang2 + bonus_orang2)

    #cek Fatima
    nama3 = list_nama[2]
    dict_orang3 = new_penjualan[2]
    values_orang3 = dict_orang3.values()
    total_orang3 = sum(values_orang3)
    total_orang3 = (sum(values_orang3) + 100)*1000
    if total_orang3 > 20000000:
        bonus_orang3 = int(total_orang3 + 1000000)
        print(">", nama3, "mendapatkan bonus sebesar:", bonus_orang3)
        print(" ", "Total penghasilan akhir: ", total_orang3 + bonus_orang3)
    print()
    
#Main program (run)
while pilihan_menu != "4":  #Fungsi while untuk looping multiple choices
    if pilihan_menu == "1":
        print("\tDaftar Penjualan Pramuniaga Selama 5 Hari")
        print("-"*55)
        print_data(penjualan)
        pilihan_menu = input("Pilih menu: ")
        print()
    elif pilihan_menu == "2":
        penghasilan()
        pilihan_menu = input("Pilih menu: ")
        print()
    elif pilihan_menu == "3":
        bonus()
        pilihan_menu = input("Pilih menu: ")
        print()
    else:
        print("Angka yang dimasukkan tidak valid!")
        print()
        pilihan_menu = input("Pilih menu: ")
        print()
print("Terima Kasih!")
        
        