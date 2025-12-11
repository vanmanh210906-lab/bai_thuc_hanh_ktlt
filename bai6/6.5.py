
print("########################################")
class ReverseString:
    def reverse_words(self, s):
        words = s.split() # Tách chuỗi thành danh sách các từ
        reversed_string = ' '.join(reversed(words)) # Đảo ngược thứ tự của các từ
        return reversed_string

# Sử dụng
reverser = ReverseString()
input_string = 'hello .py'
reversed_output = reverser.reverse_words(input_string)
print("Dữ liệu vào:", input_string)
print("Đầu ra:", reversed_output)
