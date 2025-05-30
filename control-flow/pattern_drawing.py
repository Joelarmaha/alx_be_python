x = int(input("Enter the size of the pattern: "))
i = 0
while i < x:
    j = 0
    while j < x:
        print("*", end="")
        j += 1
    print()
    i += 1