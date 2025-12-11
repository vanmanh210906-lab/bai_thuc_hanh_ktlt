
print("############################")

def generate_fibonacci(n):
    fibonacci_list = []
    a, b = 0, 1

    while a < n:
        fibonacci_list.append(a)
        a, b = b, a + b

    return fibonacci_list

def main():
    try:
        # Nhập số nguyên n từ bàn phím
        n = int(input("Nhập số nguyên n: "))

        # Tạo danh sách Fibonacci và in ra màn hình
        fibonacci_numbers = generate_fibonacci(n)
        print(f"Các số Fibonacci nhỏ hơn {n}:")
        print(fibonacci_numbers)
    except ValueError:
        print("Vui lòng nhập một số nguyên.")

if __name__ == "__main__":
    main()
