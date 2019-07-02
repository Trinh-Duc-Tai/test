from math import*
a=eval(input("Nhập cạnh a vào: "))
b=eval(input("Nhập cạnh b vào: "))
c=eval(input("Nhập cạnh c vào: "))
if (a+b>=c) and (a+c>=b) and (b+c>=a):
    if (a==b==c):
        print("Đó là tam giác đều!")
    elif (a==b) or (b==c) or (c==a):
        if (b*b + c*c == a*a) :
            print("Đó là tam giác vuông cân")
        else:
            print("Đó là tam giác cân!")
    elif (a*a+b*b==c*c) or (b*b+c*c==a*a) or (a*a+c*c==b*b):
        print("Đó là tam giác vuông")
    elif (a*a>b*b+c*c)or (b*b>a*a+c*c) or (c*c >a*a+b*b):
        print("Đó là tam giác tù")
    else:
        print("Đó là tam giác nhọn")
else:
    print("Đó không phải 3 cạnh")
print(b*b+c*c)
print(a*a)
              