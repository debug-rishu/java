a=int(input("enter the first number "))
b=int(input("enter the second number "))
c=int(input("enter the third number "))

if a>=b and a>=c:
    if b>=c:
        x,y,z=a,b,c
    else:
            x,y,z=a,c,b

            
elif b>=a and b>=c:
    if a>=c:
        x,y,z=b,a,c
    else:
            x,y,z=b,c,a

else:
    if a>b:
        x,y,z=c,a,b
    else:
            x,y,z=c,b,a

print(x,y,z)
print(x,",",x+y,",",x+y+z,)
