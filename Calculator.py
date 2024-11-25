def calculate():

    while True:
        no1 = float(input("First Number: "))
        operator = input("Enter operator (+, -, /, *): ")
        no2 = float(input("Second Number: "))


        if operator == '+':
            answer = no1 + no2
            print("Answer:", (answer))
        elif operator == '-':
            answer = no1 - no2
            print("Answer:", (answer))
        elif operator == '/':
            if no2 != 0:
                answer = no1 / no2
                print("Answer:", (answer))
            else:
                print("Error: Division by zero")
        elif operator == '*':
            answer = no1 * no2
            print("Answer:", (answer))
        else:
            print("Invalid operator")

        repeat = input("Do you want to perform another calculation? (yes/no): ")
        if repeat.lower() != 'yes':
            break


calculate()