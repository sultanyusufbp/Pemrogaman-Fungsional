random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Inisialisasi str_list sebagai list untuk menyimpan data string
str_list = []

# Inisialisasi float_tuple sebagai tuple untuk menyimpan data float
float_tuple = ()

# Inisialisasi int_dict sebagai dictionary untuk menyimpan data integer
int_dict = {}

for item in random_list:
    if isinstance(item, int):
        satuan = item % 10
        puluhan = (item % 100) // 10
        ratusan = item // 100
        int_dict[item] = {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}
    elif isinstance(item, float):
        float_tuple += (item,)
    elif isinstance(item, str):
        str_list.append(item)

# Menampilkan hasil pemisahan
print("List String:", str_list)
print("Tuple Float:", float_tuple)
print("Dictionary Integer:", int_dict)
