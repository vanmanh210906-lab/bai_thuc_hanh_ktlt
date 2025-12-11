
k =[]
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 !=0:
        k.append(str(num))
#chuyen ket qua thanh chuoi va in ra
k_str = ",".join(k)
print(k_str)
