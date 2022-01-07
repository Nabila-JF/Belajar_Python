# Episode Input User

# data yang dimasukkan pasti string
data = input("Masukan data: ")

print("data = ", data, ",type = ", type(data))

# jika ingin mengambil int, maka
angka = int(input("Masukkan angka: "))
angka = float(input("Masukkan angka: "))
print("data = ", angka, ",type = ", type(angka))

# bagaimana dengan boolean
biner = bool(input(int("Masukkan nilai boolean (0/1): ")))
print("data = ", biner, ",type = ", type(biner))
