
input_file = open('D:/a.txt', 'r')
for line in input_file:
    # Loại bỏ ký tự xuống dòng ở cuối mỗi dòng
    line = line.strip('\n') 
    s = ''
    l = len(line)
    while (l >= 0):
        s = s + line[l-1]
        l = l - 1
    print(s)
input_file.close()
