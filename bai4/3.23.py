
print("###################################")
sentence = input("Nhập một câu: ")

letter_count = sum(c.isalpha() for c in sentence)
digit_count = sum(c.isdigit() for c in sentence)

print(f"số chữ cái là: {letter_count}")
print(f"Số chữ số là: {digit_count}")
