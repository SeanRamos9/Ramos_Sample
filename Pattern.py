numbers = int(input("Enter the number or rows: "))
print(f"Number of rows: {numbers}")
num = 1
for i in range(1, numbers + 1):
    for j in range(i):
        if num <= numbers * (numbers + 1) // 2:
            print(num, end=' ')
            num += 1
    print ( )        