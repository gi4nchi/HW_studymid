multiplication=[]
for i in range(0,11,1):
    for j in range (0,11,1):
        n=i*j
        if n not in multiplication:
            multiplication.append(n)
            print(i,"x",j,"=",n)
multiplication.sort()
print(multiplication)