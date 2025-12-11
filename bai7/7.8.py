def viet_danh_sach_vao_tep(danh_sach, ten_tep):
    try:
        with open(ten_tep, 'w', encoding='utf-8') as f:
            for phan_tu in danh_sach:
                f.write(str(phan_tu) + '\n')
    except IOError:
        print("Lỗi khi ghi vào tệp.")

# Sử dụng hàm
du_lieu = ["dòng 1", "dòng 2", 123, "dòng 4"]
ten_tep_viet = "danh_sach.txt"
viet_danh_sach_vao_tep(du_lieu, ten_tep_viet)
print(f"Đã ghi danh sách vào tệp \"{ten_tep_viet}\".")
