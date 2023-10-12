expenses = [
    {"tanggal": "2023-07-25", "deskripsi": "Makan Siang", "jumlah": 50000},
    {"tanggal": "2023-07-25", "deskripsi": "Transportasi", "jumlah": 25000},
    {"tanggal": "2023-07-26", "deskripsi": "Belanja", "jumlah": 100000},
]


# 1. Fungsi add_expense untuk menambahkan pengeluaran baru ke dalam expenses.
# Menggunakan pure-function
def add_expense(expenses, date, description, amount):
    new_expenses = expenses[:]
    new_expenses.append({"tanggal": date, "deskripsi": description, "jumlah": amount})
    return new_expenses


# 2. Fungsi calculate_total_expenses menggunakan lambda expression
# untuk menghitung total pengeluaran harian.
calculate_total_expenses = lambda expenses: sum(
    expense["jumlah"] for expense in expenses
)

# 3. Fungsi get_expenses_by_date menggunakan list comprehension
# untuk menyaring pengeluaran berdasarkan tanggal tertentu.
get_expenses_by_date = lambda expenses, date: [
    expense for expense in expenses if expense["tanggal"] == date
]


# 4. Fungsi generate_expenses_report sebagai generator
# untuk menghasilkan laporan pengeluaran harian dalam bentuk string.
def generate_expenses_report(expenses):
    for expense in expenses:
        yield f"{expense['tanggal']} - {expense['deskripsi']} - Rp {expense['jumlah']}"


# 6. Mengubah fungsi get_user_input ke dalam bentuk lambda
get_user_input = lambda command: int(input(command))


def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")


# 5. Memodifikasi main agar sesuai dengan perubahan fungsi-fungsi di atas
def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
            description = input("Masukkan deskripsi pengeluaran: ")
            amount = int(input("Masukkan jumlah pengeluaran: "))
            expenses = add_expense(expenses, date, description, amount)
            print("Pengeluaran berhasil ditambahkan.")
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            expenses_on_date = get_expenses_by_date(expenses, date)
            print(f"\nPengeluaran pada tanggal {date}:")
            for expense in expenses_on_date:
                print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")
        elif choice == 4:
            print("\nLaporan Pengeluaran Harian:")
            expenses_report = generate_expenses_report(expenses)
            for entry in expenses_report:
                print(entry)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")


# ... (rest of the code remains the same)

if __name__ == "__main__":
    main()