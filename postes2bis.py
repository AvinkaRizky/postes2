# list data yang akan dicari
var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def jump_search(arr, x): # fungsi pencarian jump search
    for i in range(len(arr)):    # iterasi setiap elemen pada list
        if arr[i] == x: # jika elemen sama dengan nilai yang dicari, kembalikan indeksnya
            return i
        elif type(arr[i]) == list: # jika elemen merupakan list, lakukan pencarian search lagi pada list tersebut
            sub_result = jump_search(arr[i], x)
            if sub_result != -1:            # jika nilai ditemukan pada list yang lebih dalam, tambahkan indeks kolomnya
                return str(i) + "," + str(sub_result)
    return -1     # jika nilai tidak ditemukan pada seluruh list, kembalikan -1
# pencarian data yang dicari dan menampilkannya
print("1. Arsel di Index: {}".format(jump_search(var, "Arsel")))
print ( "Avivah di Index: {}".format(jump_search(var, "Avivah")))
print("Daiva di Index: {}".format(jump_search(var, "Daiva")))
print("2. Wahyu di Index: {} pada kolom 0".format(jump_search(var, "Wahyu")))
print("3. Wibi di Index: {} pada kolom 1".format(jump_search(var, "Wibi")))

