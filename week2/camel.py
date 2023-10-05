def main():
    camel_case = input("camelCase: ")
    snake_case = camel_to_snake(camel_case)
    print("snake_case: ",snake_case, end="")

def camel_to_snake(camel):
    snake = ""
    for c in camel:
        if c.islower():
            snake += c
        if c.isupper():
            snake += '_' + c.lower()
    return snake

main()