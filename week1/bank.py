def greeting():
    greet = input("Greetings: ")
    new_greet = greet.lower().strip()
    if'hello' in new_greet:
        print("$0")
    elif 'h' == new_greet[0]:
        print("$20")
    else:
        print("$100")
greeting()