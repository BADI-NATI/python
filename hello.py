print("CALCULATOR:\n")

def add(a, b):
    return print(f"The additon of {a} and {b} is {a+b}.")

def sub(a, b):
    return print(f"The subtration of {a} and {b} is {a-b}.")

def mul(a, b):
    return print(f"The multiplication of {a} and {b} is {a*b}.")

def div(a, b):
    return print(f"The division of {a} and {b} is {a/b}.")


a = int(input("Enter a number?\n"))
b = int(input("Enter another number?\n"))

lang = input("Which operation do you want to work with?\n A. Addition\n B. Subtraction\n C. Multiplication\n D. Division\n ")

match lang:
    case "A" | "a":
        add(a,b)

    case "B" | "b":
        sub(a,b)

    case "C" | "c":
        mul(a,b)
    
    case "D" | "d":
        div(a,b)







