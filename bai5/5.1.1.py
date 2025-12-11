# File: main_script.py
import mymath # Ghi chú: không có .py

values = [2, 4, 6, 8, 10]

print('Squares:')
for v in values:
    print(mymath.square(v))

print('Cubes:')
for v in values:
    print(mymath.cube(v))

print('Average: ' + str(mymath.average(values)))

# Sử dụng cú pháp đổi tên module
import mymath as mt
print(mt.square(2))
print(mt.square(3))
