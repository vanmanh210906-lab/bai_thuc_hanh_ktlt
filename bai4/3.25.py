
print("################################")
numbers = input("Nhập danh sách số, cách nhau bởi dấu phẩy: ").split(',')
odd_numbers = [num for num in numbers if int(num) % 2 != 0]
print(','.join(odd_numbers))
