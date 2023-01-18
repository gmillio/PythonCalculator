def calculator():
    while True:
        expression = input("Enter an expression (or 'q' to quit): ")
        if expression == 'q':
            break
        try:
            result = eval(expression)
            print(result)
        except:
            print("Invalid expression. Please try again.")

calculator()