k = open('D:/a.txt', 'r')

char = 0      # đếm ký tự
wc = 0        # đếm từ (word count)
lc = 0        # đếm dòng

for line in k:
    for i in range(0, len(line)):
        char += 1
        if line[i] == ' ':
            wc += 1
        if line[i] == '\n':
            wc += 1
            lc += 1

print("The no. of chars is %d \nThe no. of words is %d \nThe no. of lines is %d" 
      % (char, wc, lc))

k.close()
