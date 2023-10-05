def remove_vowels(input_str):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    result = ""
    for char in input_str:
        if char not in vowels:
            result += char
    return result
def main():
    user_input = input("Input: ")
    output = remove_vowels(user_input)
    print(output)
if __name__ == "__main__":
    main()