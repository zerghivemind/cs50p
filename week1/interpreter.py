def main():
    expression = input("Enter an expression: ")
    x, y, z = expression.split(" ")
    calculate(x, y, z)

def calculate(a, b, c):
    num1 = float(a)
    num2 = float(c)
    match b:
        case '+' :
            print(num1 + num2)
        case '-' :
            print(num1 - num2)
        case '*' :
            print(num1 * num2)
        case '/' :
            print(num1 / num2)
    
main()