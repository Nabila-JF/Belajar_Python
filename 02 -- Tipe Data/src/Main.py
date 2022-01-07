#tipe data: Angka satuan yang gak ada komanya (integer)
data_integer = 11
print ("data : ", data_integer)
print("-bertipe : ", type(data_integer))

#tipe data: Angka dengan koma (float)
data_float = 1.71
print ("data : ", data_float)
print("-bertipe : ", type(data_float))

#tipe data: Kumpulan karakter (string)
data_string = "Apa maumu siapa dirinya~"
print ("data : ", data_string)
print("-bertipe : ", type(data_string))

#tipe data: biner True/False (boolean)
data_boolean = True
print ("data : ", data_boolean)
print("-bertipe : ", type(data_boolean))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("-bertipe : ", type(data_complex))

# pemanggilan tipe data dari bahasa C
from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("-bertipe : ", type(data_c_double))