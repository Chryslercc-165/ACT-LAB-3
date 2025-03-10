while True:
    num = int(input("Enter Number: "))

    if num == 0:
        print(num,"is an Even number")
    elif num > 0:
        if num % 2 == 0:
            print(num,"is an Even number")
        else:
            print(num,"is an Odd number")
    else:
        if num % 2 == 0:
            print(num,"is an Even number")
        else:
            print(num,"is an Odd number")

    b = input("\nDo you want to try again? (y/n): ")
    if b == "n":
        print("Goodbye!")
        break

