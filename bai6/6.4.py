
print("###################################")
class LaMaToInteger:
    def __init__(self):
        self.roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def convert_to_integer(self, roman_numeral):
        result = 0
        prev_value = 0
        for numeral in reversed(roman_numeral):
            current_value = self.roman_numerals[numeral]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value
        return result

# Sử dụng class LaMaToInteger
converter = LaMaToInteger()
roman_numeral = "XIV" # Thay đổi số La Mã ở đây
integer_value = converter.convert_to_integer(roman_numeral)
print(f"số nguyên tương ứng với số La Mã '{roman_numeral}' là: {integer_value}")
