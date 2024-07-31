print("==========================")
print("KALKULATOR SEDERHANA")
print("==========================\n")

# menginput nilai
angka_1 = float(input("Angka pertama \t:"))
operator = input("operator \t:")
angka_2 = float(input("Angka kedua \t:"))

# output
if operator == "+" :
    hasil = angka_1 + angka_2
    print("hasil dari",angka_1,"+",angka_2,"=",hasil)

elif operator == "-" :
    hasil = angka_1 - angka_2
    print(f"hasil dari {angka_1} + {angka_2} = {hasil}")

elif operator == "*" :
    hasil = angka_1 * angka_2
    print("hasil dari",angka_1,"*",angka_2,"=",hasil)

elif operator == "/" :
    hasil = angka_1 / angka_2
    print("hasil dari",angka_1,"**",angka_2,"=",hasil)

elif operator == "**" :
    hasil = angka_1 ** angka_2
    print("hasil dari",angka_1,"**",angka_2,"=",hasil)

elif operator == "%" :
    hasil = angka_1 % angka_2
    print("hasil dari",angka_1,"%",angka_2,"=",hasil)

elif operator == "//" :
    hasil = angka_1 // angka_2
    print("hasil dari",angka_1,"//",angka_2,"=",hasil)

else :
    print("ERROR !!!")
