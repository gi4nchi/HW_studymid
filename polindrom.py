num=input("enter a polindrom")
print(num)

print(num[::-1])
string=""
if num == num[::-1]:
    print(num)
for i in range(0,10,2):
    i=str(i)
    print(i)
    string=string+i
print(string)