numeri=input("input two numbers you want to multiply separated by commas")
num=numeri.split(",")
tot=0
try:
    for x in range(int(num[0])):
        tot+=int(num[1])

except:
    print("I said numbers")

finally:
    print(tot)

