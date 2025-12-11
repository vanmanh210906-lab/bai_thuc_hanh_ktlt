
print("############################")

def check_divisible_by_5(binary_numbers):
    divisible_by_5 = [binary for binary in binary_numbers if int(binary, 2) % 5 == 0]
    return divisible_by_5


def main():
    try:
        # Nhập chuỗi số nhị phân từ bàn phím, phân tách bởi dấu phẩy
        binary_string = input("Nhap chuoi so nhi phan, cach nhau boi dau phay: ")

        # Tách chuỗi thành danh sách các số nhị phân
        binary_numbers = binary_string.split(',')

        # Kiểm tra và in ra các số chia hết cho 5
        divisible_by_5 = check_divisible_by_5(binary_numbers)
        print("Cac so nhi phan chia het cho 5:")
        print(','.join(divisible_by_5))
    except ValueError:
        print("Vui long nhap chuoi so nhi phan hop le.")


if __name__ == "__main__":
    main()
