#print multiplication table for any value

value = input("Enter number: ")
n = int(value)
for i in range(1,13):
    print(f"{value} X {i} = {n * i}")