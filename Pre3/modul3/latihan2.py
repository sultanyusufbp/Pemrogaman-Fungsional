def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

data_list = ["3 minggu 3 hari 7 jam 21 menit",
             "5 minggu 5 hari 8 jam 11 menit",
             "7 minggu 1 hari 5 jam 33 menit"]

# Membuat daftar nilai integer dari setiap data
integer_values = []

for data in data_list:
    data_parts = data.split()
    integers = list(filter(is_integer, data_parts))
    integer_values.append(integers)

for values in integer_values:
    print(values)