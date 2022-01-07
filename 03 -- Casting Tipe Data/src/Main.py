# Kita belajar Casting
# Casting adalah merubah dari satu tipe ke tipe yang lain
# Tipe data = int, float, str, bool

## INTEGER
print("====INTEGER===")
data_int = 9
print("data = ", data_int, ",type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))

# Nilai boolean selain 0 adalah true. Jika nilai boolean adalah 0 maka artinya false

## FLOAT
print("====FLOAT===")
data_float = 9.5
print("data = ", data_float, ",type = ", type(data_float))

data_int = int(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))
## FLOAT
print("====FLOAT===")
data_float = 9.5
print("data = ", data_float, ",type = ", type(data_float))

data_int = int(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))

# Nilai boolean selain 0 adalah true. Jika nilai boolean adalah 0 maka artinya false
 
## BOOLEAN
print("====BOOLEAN===")
data_bool = False
print("data = ", data_bool, ",type = ", type(data_bool))

data_int = int(data_bool) # jika nilai false maka hasilnya 0. jika nilai true maka hasilnya 1
data_str = str(data_bool)
data_float = float(data_bool)
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_float, ",type = ", type(data_float))

## STRING
print("====STRING===")
data_str = "10"
print("data = ", data_str, ",type = ", type(data_str))

data_int = int(data_str) 
data_bool = bool(data_str)
data_float = float(data_str)
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_bool, ",type = ", type(data_bool))
print("data = ", data_float, ",type = ", type(data_float))

# Jika nilai merupakan karakter maka tidak akan bisa dirubah ke tipe int
# Jika nilai berupa angka maka dapat dirubah ke int
# Jika ingin membuat nilai menjadi flase maka nilainya harus kosong