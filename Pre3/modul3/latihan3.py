import random

# Membuat daftar acak yang berisi nilai int, float, dan string
random_list = [1, 2.7, "Hello", 3, "World", 4.7, 5.5, "AI"]

# Memisahkan nilai float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

print("Data Float:")
print(tuple(float_values))

print("Data Int:")
int_data = []
for value in int_values:
    units = value % 10
    tens = (value // 10) % 10
    hundreds = (value // 100) % 10
    int_data.append({'ratusan': hundreds, 'puluhan': tens, 'satuan': units})
for data in int_data:
    print(data)

print("Data String:")
print(string_values)