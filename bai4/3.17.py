
print("##################################")
def tong_uoc_so(n):
    return sum([i for i in range(1, n) if n % i == 0])

def main():
    try:
        #nhap so nguyen n tu ban phim
        n = int(input("nhap so nguyen n: "))

        #in rs csc do nguyen duong nho hon n co tong uoc lon hon chinh no
        print(f"cca so nguyen duong nho hon (n) co tong uoc so lon hon chinh no:")
        for i in range(1, n):
            if tong_uoc_so(i) > i:
                print(i)
    except ValueError:
        print("Vui long nhap mot so nguyen.")
if _name_=="_main_":
    main()
