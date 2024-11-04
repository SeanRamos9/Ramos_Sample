numberrows = int(input("enter the number of rows: "))
print(f"number of rows: {numberrows}")

num= 1

for i in range(1, numberrows + 1):
    for j in range(i):
        if num <= numberrows * (numberrows + 1) // 2:
            print(num, end= ' ')
            num+=1
    print()