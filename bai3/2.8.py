
print("########################")

import math
pos = [0, 0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ") # Tahy doi nay
    direction = movemnt[0]
    steps = int(movemnt[1])
    if direction == "up":
        pos[0] += steps
    elif direction == "down":
        pos[0] -= steps
    elif direction =="LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        pass
####################
print(int(round(math.sqrt(pos[1] ** 2 + pos[0] ** 2))))
