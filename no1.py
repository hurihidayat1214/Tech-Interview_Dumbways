
user_value = int(input("Angka :"))
binary = ''
hitung_kata =len (binary)
while user_value>0:
    rem = user_value % 2
    binary = binary + str(rem)
    user_value = user_value //2
    print(binary[::-1])

    print("jumlah 0 :", len(binary  ))

