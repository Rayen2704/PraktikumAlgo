print ("---PROGRAM KONVERSI BILANGAN---")
print ()
print ("1 -> Desimal ke Biner")
print ("2 -> Biner ke Desimal")
print ("3 -> Exit")

menu = 0
while menu != 3:
    menu = int(input("silahkan pilih menu: "))
    if menu == 1:
        a = int(input("Masukan bilangan desimal: "))
        bineri = bin(a).replace("0b","")
        print("Nilai binarnya adalah {0}".format(bineri))
    elif menu == 2:
        c = int(input("Masukan bilangan biner: "),2)
        print ("Nilai desimalnya adalah {0}".format(c))
print("Terimakasih telah menggunakan program ini")