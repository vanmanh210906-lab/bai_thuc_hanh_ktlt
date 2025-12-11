
import math
#Nhap cac he so a, b, c tu ban phim
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))

#Tinh delta
delta = "k"
k = b**2 - 4*a*c

#Kiem tra delta de xac dinh so nghiem va tim nghiem
if k>0 :
    x1= (-b + math.sqrt(k))/(2*a)
    x2= (-b - math.sqrt(k))/(2*a)
    print("Phuong tirnh co hai nghiem phan biet: ")
    print("x1= ", x1)
    print("x2= ", x2)
elif k == 0:
    x1 = -b/(2*a)
    print("Phuong trinh co nghiem kep: ")
    print("x1= ",x1)
else:
    print("phuong trinh ko co nghiem thuc")
    
    
