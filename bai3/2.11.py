
print("###############################")

def benefit(t, n, k):
    # Chuyển lãi suất từ phần trăm sang dạng thập phân
    t = t / 100

    # Tính số tiền sau k tháng sử dụng công thức tính lãi suất liên tục
    future_value = n * (1 + t) ** k

    return future_value


# Nhập lãi suất, số vốn ban đầu và số tháng gửi từ người dùng
t = float(input("Nhap lai suat hang thang (%): "))
n = float(input("Nhap so von ban dau: "))
k = int(input("Nhap so thang gui: "))

# Gọi hàm benefit để tính số tiền nhận được sau k tháng
result = benefit(t, n, k)

# In kết quả
print(f"So tien nhan duoc sau {k} thang la: {result:.2f}")
