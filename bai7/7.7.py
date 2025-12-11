def dem_so_dong(ten_tep):
    try:
        with open(ten_tep, 'r', encoding='utf-8') as f:
            so_dong = 0
            for _ in f:
                so_dong += 1
        return so_dong
    except FileNotFoundError:
        return "Tệp không tồn tại."

# Sử dụng hàm
ten_tep_can_dem = "tep_cua_toi.txt"
print(f"Số dòng trong tệp \"{ten_tep_can_dem}\" là: {dem_so_dong(ten_tep_can_dem)}")
