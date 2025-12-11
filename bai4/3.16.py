
print("##################################")

binary_string = input("Nhập chuỗi số nhị phân, cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các số nhị phân
binary_numbers = binary_string.split(',')

# In ra các số nhị phân đã nhập
print("Các số nhị phân đã nhập:")
for binary_number in binary_numbers:
    print(binary_number.strip())   # strip() để loại bỏ khoảng trắng dư thừa
