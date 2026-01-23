def main():
    print("Simple Addition Program")
    try:
        # Get input from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Calculate the sum
        result = num1 + num2
        
        # Display the result
        print(f"The sum of {num1} and {num2} is: {result}")
        
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
