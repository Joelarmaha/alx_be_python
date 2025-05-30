number = input("Enter a number to see its multiplication table:")
for n in range(1,11):
    result = int(number) * n
    print(f" {number} * {n} = {result}")
