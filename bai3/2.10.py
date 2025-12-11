
print("###########################")

import math

def Tinh(R):
    if R > 0:
        chu_vi = 2 * math.pi * R
        dien_tich = math.pi * R ** 2
        return chu_vi, dien_tich
    else:
        return "Bán kính không hợp lệ, vui lòng nhập bán kính dương."

# Nhập bán kính từ người dùng
R = float(input("Nhập bán kính hình tròn: "))

# Gọi hàm Tinh và kiểm tra giá trị trả về
result = Tinh(R)

if isinstance(result, tuple):
    chu_vi, dien_tich = result
    print("Chu vi của hình tròn là:", chu_vi)
    print("Diện tích của hình tròn là:", dien_tich)
else:
    print(result)
