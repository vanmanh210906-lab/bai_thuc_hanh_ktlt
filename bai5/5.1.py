def square(n):
    return n*n

def cube(n):
    return n*n*n

def average(values):
    nvals = len(values)
    sum_val = 0.0 # Đổi tên biến 'sum' để tránh trùng với hàm built-in
    for v in values:
        sum_val += v
    return float(sum_val)/nvals
