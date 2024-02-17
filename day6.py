#factorial of a number
while True:
    num = input("Enter a number for factorial: ")
    a = int(num)
    p = 1

    for i in range(a,0,-1):
        print(f"{p} X {i}")
        p = p*i
    print(p)
    
