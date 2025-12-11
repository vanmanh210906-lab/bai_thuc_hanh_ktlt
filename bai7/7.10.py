import re

def tim_tu_dai_nhat(ten_tep):
    try:
        with open(ten_tep, 'r', encoding='utf-8') as f:
            van_ban = f.read()
            # Tách từ, loại bỏ dấu câu và khoảng trắng thừa
            tu = re.findall(r'\b\w+\b', van_ban.lower())
            if not tu:
                return "Không tìm thấy từ nào trong tệp."
            # Tìm từ có độ dài lớn nhất
            tu_dai_nhat = max(tu, key=len)
            return tu_dai_nhat
    except FileNotFoundError:
        return "Tệp không tồn tại."

# Sử dụng hàm
ten_tep_van_ban = "van_ban_cua_toi.txt"
print(f"Từ dài nhất trong tệp \"{ten_tep_van_ban}\" là: {tim_tu_dai_nhat(ten_tep_van_ban)}")
