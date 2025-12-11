def are_all_digits_even(number):
    return all(int(digit) % 2 == 0 for digit in str(number))

start, end = 1000, 3000
even_digit_number = [str(num) for num in range(start, end+1) if are_all_digits_even(num)]

print(','.join('even_digit_numbers'))
