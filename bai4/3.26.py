
print("################################")
transactions = input("Nhập nhật ký giao dịch, cách nhau bởi dấu phẩy: ").split(',')
account_balance = sum(map(float, transactions))
print(f"số tiền thực trong tài khoản: {account_balance}")
