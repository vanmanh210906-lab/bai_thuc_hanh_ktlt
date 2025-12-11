import numpy as np

# Định nghĩa kiểu dữ liệu cho mảng có cấu trúc
# 'S15' nghĩa là một chuỗi byte có độ dài tối đa 15 ký tự (S là string, 15 là độ dài)
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Dữ liệu chi tiết của sinh viên
# Lưu ý: Sửa lỗi chính tả '42.10' thành 42.10, '40.11' thành 40.11 để đảm bảo kiểu float hợp lệ
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]

# Tạo mảng có cấu trúc từ dữ liệu và kiểu dữ liệu đã cho
students = np.array(students_details, dtype=data_type)

print("Mảng gốc:")
print(students)

# Sắp xếp mảng dựa trên trường 'height'
# np.sort trả về một mảng mới đã sắp xếp
sorted_students = np.sort(students, order='height')

print("\nMảng sau khi sắp xếp theo chiều cao:")
print(sorted_students)
