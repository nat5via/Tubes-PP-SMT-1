#Soal bagian a
def baca_data(filename):
    #baca data line pertama dari file txt
    file = open(filename, "r")
    teks = file.readline().replace("\n","")
    
    #buat list kosong
    penjualan = []

    while teks != "":
        dict = {}
        #lakukan split di sini pada teks
        a = teks.split()
        #susun data yang dibaca ke dalam dictionary
        b = {"nama": a[0],
             "senin": a[1],
             "selasa": a[2],
             "rabu": a[3],
             "kamis": a[4],
             "jumat": a[5]} #list nilai hari
        dict[a[0]] = b #menambahkan key dan value
        #kemudian dictionary diappend ke dalam list
        penjualan.append(b) #dict[key] = value
        #baca data baris selanjutnya
        teks = file.readline().replace("\n","")
    #print(penjualan)

    return penjualan

#fungsi utk menampilkan data penjualan
def print_data(data):
    list_orang = ["Aradea", "Safwan", "Fatima"]
    i = 0
    for elemen in data: #elemen = dictionary dari list penjualan
        print(">",list_orang[i])
        for key in elemen: #key dari setiap dict yang ada di list penjualan
            if key != "nama":
                print("---","Hari",key,"=",elemen[key])
        print()
        i += 1

#run dari soal a
nama_file = "daftarpramuniaga.txt"
penjualan = baca_data(nama_file)

#Hapus key[nama] dalam list
penjualan = [{k: v for k, v in d.items() if k != 'nama'} for d in penjualan]

#valuenya dijadiin int
def convert_to_int(lst):
    result = [dict([a, int(x)] for a, x in b.items()) for b in lst]
    return result

new_penjualan = convert_to_int(penjualan)

#soal bagian b
#value dari senin hingga jumat dijumlah
def penghasilan():
    #Total penjualan
    print("-Total Penjualan setiap pramuniaga di akhir minggu (tanpa upah):")
    
    #Total Aradea
    dict_aradea = new_penjualan[0]
    values_aradea = dict_aradea.values()
    total_aradea = sum(values_aradea)

    #Total Safwan
    dict_safwan = new_penjualan[1]
    values_safwan = dict_safwan.values()
    total_safwan = sum(values_safwan)

    #Total Fatima
    dict_fatima = new_penjualan[2]
    values_fatima = dict_fatima.values()
    total_fatima = sum(values_fatima)

    print(">","Aradea:", total_aradea*1000)
    print(">","Safwan:", total_safwan*1000)
    print(">","Fatima:", total_fatima*1000)
    print()

    #Gaji tetap (not include insentif + bonus)
    print("-Penghasilan pramuniaga di akhir minggu (tidak termasuk insentif + bonus):")
    total_aradea = (sum(values_aradea) + 100)*1000
    total_safwan = (sum(values_safwan) + 100)*1000
    total_fatima = (sum(values_fatima) + 100)*1000
    print(">","Aradea:", total_aradea)
    print(">","Safwan:", total_safwan)
    print(">","Fatima:", total_fatima)
    print()

    #insentif
    #cek Aradea
    if total_aradea > 0:
        insentif_aradea = total_aradea*25/100
        total_aradea = total_aradea + insentif_aradea
    #cek Safwan
    if total_safwan > 0:
        insentif_safwan = total_aradea*25/100
        total_safwan = total_safwan + insentif_safwan
    #cek Fatima
    if total_fatima > 0:
        insentif_fatima = total_aradea*25/100
        total_fatima = total_fatima + insentif_fatima
    
    #Gaji tetap + insentif (not include bonus)
    print("-Penghasilan pramuniaga di akhir minggu + insentif (tidak termasuk bonus):")
    print(">","Aradea:", int(total_aradea))
    print(">","Safwan:", int(total_safwan))
    print(">","Fatima:", int(total_fatima))
    print()

#soal bagian c
def bonus():
    print("-Pramuniaga yang mendapatkan bonus:")
   #cek Aradea
    dict_aradea = new_penjualan[0]
    values_aradea = dict_aradea.values()
    total_aradea = sum(values_aradea)
    total_aradea = (sum(values_aradea) + 100)*1000
    if total_aradea > 20000000:
        bonus_aradea = int(total_aradea + 1000000)
        print("> Aradea mendapatkan bonus sebesar:", bonus_aradea)
        print("\tTotal penghasilan akhir: ", total_aradea + bonus_aradea)

    #cek Safwan
    dict_safwan = new_penjualan[1]
    values_safwan = dict_safwan.values()
    total_safwan = sum(values_safwan)
    total_safwan = (sum(values_safwan) + 100)*1000
    if total_safwan > 20000000:
        bonus_safwan = int(total_safwan + 1000000)
        print("> Safwan mendapatkan bonus sebesar:", bonus_safwan)
        print("\tTotal penghasilan akhir: ", total_safwan + bonus_safwan)

    #cek Fatima
    dict_fatima = new_penjualan[2]
    values_fatima = dict_fatima.values()
    total_fatima = sum(values_fatima)
    total_fatima = (sum(values_fatima) + 100)*1000
    if total_fatima > 20000000:
        bonus_fatima = int(total_fatima + 1000000)
        print("> Fatima mendapatkan bonus sebesar:", bonus_fatima)
        print(" ", "Total penghasilan akhir: ", total_fatima + bonus_fatima)

#Main program
print("Diketahui Total Penjualan Masing-masing Pramuniaga:")
print_data(penjualan) #print data dari flie teks
print("*"*55) #pembatas antar soal
print()
penghasilan()
print("*"*55) #pembatas antar soal
bonus()
