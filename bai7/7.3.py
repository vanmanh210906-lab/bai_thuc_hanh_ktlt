# Tên tệp bạn muốn đọc
ten_tep = "ten_file_cua_ban.txt"

try:
    # Mở tệp ở chế độ đọc ('r') bằng khối 'with'
    with open(ten_tep, 'r', encoding='utf-8') as file:
        # Đọc toàn bộ nội dung của tệp
        noi_dung = file.read()
        
        # In ra nội dung đã đọc
        print(noi_dung)

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy tệp '{ten_tep}'.")
except Exception as e:
    print(f"Đã xảy ra lỗi khác: {e}")
