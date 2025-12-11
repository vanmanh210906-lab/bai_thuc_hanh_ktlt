
print("#########################")

def generate_pascal_triangle(n):
    return [[1] * (i + 1) for i in range(n)]

def main():
    try:
        n = int(input("Nhap so nguyen n: "))
        pascal_triangle = generate_pascal_triangle(n)

        for row in pascal_triangle:
            print(row)
    except ValueError:
        print("Vui long nhap mot so nguyen.")

if __name__ == "__main__":
    main()
