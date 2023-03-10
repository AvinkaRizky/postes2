# list data yang akan dicari
var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# fungsi pencarian jump search
def jump_search(arr, x):
    # iterasi setiap elemen pada list
    for i in range(len(arr)):
        # jika elemen sama dengan nilai yang dicari, kembalikan indeksnya
        if arr[i] == x:
            return i
        # jika elemen merupakan list, lakukan pencarian search lagi pada list tersebut
        elif type(arr[i]) == list:
            sub_result = jump_search(arr[i], x)
            # jika nilai ditemukan pada list yang lebih dalam, tambahkan indeks kolomnya
            if sub_result != -1:
                return str(i) + "," + str(sub_result)
    # jika nilai tidak ditemukan pada seluruh list, kembalikan -1
    return -1
# pencarian data yang dicari dan menampilkannya
print("1. Arsel di Index: {}".format(jump_search(var, "Arsel")))
print ( "Avivah di Index: {}".format(jump_search(var, "Avivah")))
print("Daiva di Index: {}".format(jump_search(var, "Daiva")))
print("2. Wahyu di Index: {} pada kolom 0".format(jump_search(var, "Wahyu")))
print("3. Wibi di Index: {} pada kolom 1".format(jump_search(var, "Wibi")))

Program ini dibuat untuk mencari dan menampilkan banyak data yang telah diberikan pada sebuah list.
Merupakan algoritma pencarian yang bekerja dengan cara mengecek setiap elemen pada suatu list secara berurutan.
