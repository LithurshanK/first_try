a = int(input("Enter angle 1: " ))
b = int(input("Enter angle 2: " ))
c = int(input("Enter angle 3: " ))

if a==0 or b==0 or c==0 or a+b+c!=180:
    print ('Angles do not form a triangle')
elif a==90 or b==90 or c==90:
    print ('Right angled')
elif a>90 or b>90 or c>90:
    print ('Obtuse angled')
else:
    print ('Acute angled')
