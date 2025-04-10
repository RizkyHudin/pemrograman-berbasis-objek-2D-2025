class Hewan:
    def __init__(self, nama, jenis, habitat):
        self.nama = nama  
        self.jenis = jenis  
        self.habitat = habitat  

    def suara(self):
        pass  
    
    def informasi(self):
        print(f"Nama Hewan: {self.nama}")
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")
        self.suara()
        print("-" * 30)

class Kucing(Hewan):
    def __init__(self, nama, jenis, habitat):
        super().__init__(nama, jenis, habitat)

    def suara(self):
        print(f"{self.nama} mengatakan: Meowwwzz")

class Anjing(Hewan):
    def __init__(self, nama, jenis, habitat):
        super().__init__(nama, jenis, habitat)

    def suara(self):
        print(f"{self.nama} mengatakan: hruff hruff")

class Burung(Hewan):
    def __init__(self, nama, jenis, habitat):
        super().__init__(nama, jenis, habitat)

    def suara(self):
        print(f"{self.nama} mengatakan: crhiztt")


# Misalkan data_hewan adalah sebuah list yang berisi data seperti ini
data_hewan = [
    ("jakki", "Kucing Persia", "Kucing"),
    ("ryoo", "Anak anjing", "Anjing"),
    ("milli", "Burung lovebird", "Burung"),
    ("millu", "Kucing Anggoraa", "Kucing"),
    ("anap", "Anjing Darjo", "Anjing")
]

hewan_list = []  

for data in data_hewan:
    if data[2] == "Kucing":
        hewan_list.append(Kucing(data[0], data[1], data[2]))  
    elif data[2] == "Anjing":
        hewan_list.append(Anjing(data[0], data[1], data[2]))  
    elif data[2] == "Burung":
        hewan_list.append(Burung(data[0], data[1], data[2]))  

print("Informasi Hewan:")
for hewan in hewan_list:
    hewan.informasi()
