#FINDING FACTORS OF A NUMBER
while True:
    num = int(input("Enter a num: "))
    fac = [num]
    for i in range (1,num):
        if num % i == 0:
            fac.append(i)
    fac.sort()
    print(fac)
    