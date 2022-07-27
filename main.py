list = [] 
# maksimal stack harus 10 elemen

while True:
    input_data = int(input('masukkan angka : '))
    if input_data == 999: # jika data yang diinputkan bernilai 999, proses selesai
        print("Program selesai")
        break
    elif input_data >= 60:      # inputan data yang dimasukkan >= 60, periksa kondisi stack,
        list.append(input_data) # bila stack masih bisa diisi maka simpan data tersebut
    elif len(list) == 10:       # bila stack penuh data tidak jadi disimpan, lalu tampilkan (isinya,"stack penuh"), proses selesai
        print(list)
        print('stack penuh')
        break
    elif input_data < 60:       # inputan data yang dimasukkan < 60 ,periksa kondisi stack
        if list == []:          # bila stack kosong ("tampilkan : Stack kosong"), proses selesai
            print('Stack Kosong')
            break
        else:                   # bila ada isinya (tampilkan),kemudian proses diulang kembali
            print(list)
