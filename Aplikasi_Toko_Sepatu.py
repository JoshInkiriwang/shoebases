# Function Jenis Sepatu yang mendapat Kode Jenis Sepatu dari main code
def get_jenis_sepatu_by_code(kode_jenis):
    jenis_mapping = {
        "SP" : "Sport",
        "KR" : "Korean",
        "SO" : "Slipon"
    }

    # Melempar kembali kepanjangan dari Kode Jenis Sepatu ke dalam main code
    return jenis_mapping.get(kode_jenis, "Unknown") 

# Function Warna Sepatu yang mendapat Kode Warna Sepatu dari main code
def get_warna_sepatu_by_code(kode_warna) :
    color_mapping = {
        "DB" : "Dragon Ball",
        "HP" : "Hitam Putih",
        "CL" : "Colorful"
    }

    # Melempar kembali kepanjangan dari Kode Warna Sepatu ke dalam main code
    return color_mapping.get(kode_warna, "Unknown") 

# Function Harga Sepatu yang mendapat Kode Jenis Sepatu dan Kode Warna Sepatu dari Main Code
def get_harga_satuan(jenis_sepatu, warna_sepatu, products) :
    for item in products :
        if item[0] == jenis_sepatu and item[1] == warna_sepatu :
            return item[2] # Mengembalikan harga sepatu ke main code
    return 0  # Handle case where product is not found

    '''
    item[0] itu kolom pertama yang isine jenis sepatu
    item[1] itu kolom kedua yang isine warna_sepatu
    item[2] itu kolom ketiga yang isine harga_sepatu
    '''

''' Ini list isinya informasi seputar sepatu
Struktur List :
[jenis_sepatu, warna_sepatu, harga]
Data Types :
[string, string, integer]
'''
product_list = [
    ["SP", "DB", 150000],
    ["SP", "HP", 160000],
    ["SP", "CL", 170000],
    ["KR", "DB", 80000],
    ["KR", "HP", 10000],
    ["KR", "CL", 120000],
    ["SO", "DB", 120000],
    ["SO", "HP", 140000],
    ["SO", "CL", 160000]
]

store_name = "Shoebases"

# Variabel ini untuk Grand Total Harga Sepatu
total_bayar = 0

# Variabel ini untuk banyak jenis sepatu yang mau dibeli
banyak = 0

# Header dari program pembelian sepatu
header = "\n    " + 5*"=" + store_name + 5*"="

# Pembatas antar elemen tampilan
pembatas = 45*"="

# Print out header yang sudah dibuat sebelumnya
print(header)

# Input angka untuk banyak jenis sepatu yang mau dibeli
# Input validation for banyak_beli
while True:
    try:
        banyak_beli = int(input("Masukkan jumlah sepatu yang mau dibeli = "))
        if banyak_beli > 0:
            break
        else:
            print("Jumlah sepatu harus lebih dari 0. Silahkan coba lagi.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Pembatas (=) panjang
print(pembatas)  

for banyak in range(banyak_beli) :
    # Input validation for kode_sepatu
    while True:
        kode_sepatu = input("Masukkan Kode Sepatu = ")
        if len(kode_sepatu) == 7:
            break
        else:
            print("Kode Sepatu tidak valid. Silahkan coba lagi.")

    # Memotong Data dari Input Kode Sepatu
    jenis = kode_sepatu[0:2]
    warna = kode_sepatu[3:5]
    nomor_prod = int(kode_sepatu[6::]) #Dijadikan integer karena nomor / jumlah produksi per hari
    
    #Variabel Harga Satuan Sepatu
    #harga_satuan itu nama function diatas
    harga = get_harga_satuan(jenis, warna, product_list)

    print("Jenis Sepatu         =", get_jenis_sepatu_by_code(jenis)) # Kode Jenis di kirim ke Function Jenis Sepatu
    print("Warna Sepatu         =", get_warna_sepatu_by_code(warna)) # Kode Warna di kirim ke Function Warna Sepatu
    print("Nomor Produksi       =", nomor_prod)

    # ===== Print Out Harga Satuan 
    print("Harga Sepatu         = Rp", harga)
    
    # ===== Banyak unit sepatu yang ingin dibeli 
    print("Jumlah Beli          =", end = ' ') # end= ' ' biar ga ada beda line antara tulisan jumlah beli dan inputan nya
    jumlah_beli = int(input())

    # ===== Sub Total ===== 
    harga_subtotal = jumlah_beli * harga
    print("Sub Total            = Rp", harga_subtotal)

    # ===== Menjumlahkan pembelian skrg ke Grand Total
    total_bayar += harga_subtotal

    # =======================
    print(pembatas)

# ===== Akan muncul ketika sudah selesai belanja sepatu
print("Total Bayar          = Rp", total_bayar)
