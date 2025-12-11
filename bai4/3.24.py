
print("################################################")
sentence = input("Nhập một câu: ")

uppercase_count = sum(c.isupper() for c in sentence)
lowercase_count = sum(c.islower() for c in sentence)

print(f"Chữ hoa: {uppercase_count}")
print(f"Chữ thường: {lowercase_count}")
