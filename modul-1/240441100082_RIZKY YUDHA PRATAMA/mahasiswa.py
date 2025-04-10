class Manusia:
    def __init__(self, nama, umur, alamat):  
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        return f"{self.nama} sedang berjalan."

    def berlari(self):
        return f"{self.nama} sedang berlari."

    def tampilkan_umur_dan_alamat(self):
        return f"Umur {self.nama}: {self.umur} tahun, Alamat: {self.alamat}"

# membuat objek
manusia1 = Manusia("RAFLY", 20, "SIDOARJO")
manusia2 = Manusia("ISMA", 20, "SURABAYA")
manusia3 = Manusia("FAHRI", 20, "JOMBANG")
manusia4 = Manusia("YOGA", 20, "SIDOARJO")
manusia5 = Manusia("HAIDAR", 20, "SIDOARJO")

# output-nya
print(manusia1.berjalan())
print(manusia1.tampilkan_umur_dan_alamat())

print(manusia2.berlari())
print(manusia2.tampilkan_umur_dan_alamat())

print(manusia3.berjalan())
print(manusia3.tampilkan_umur_dan_alamat())

print(manusia4.berlari())
print(manusia4.tampilkan_umur_dan_alamat())

print(manusia5.berjalan())
print(manusia5.tampilkan_umur_dan_alamat())
