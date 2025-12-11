
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

# Sử dụng class Hinhchunhat
chieu_dai = 5
chieu_rong = 3

hinh = Hinhchunhat(chieu_dai, chieu_rong)
dien_tich = hinh.tinh_dien_tich()
print("Diện tích hình chữ nhật là:", dien_tich)
