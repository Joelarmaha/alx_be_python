def perform_operation(num1, num2, operation ):
    match operation:
        case "add":
            return float(num1) - float(num2)
        case "subtract":
            return float(num1) - float(num2)
        case "multiply":
            return float(num1) * float(num2)
        case "divide":
            if float(num2) == 0:
                return ("not valid")
            else :
                print(float(num1)/float(num2))
def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()



