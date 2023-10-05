def thoughts():
    x = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    x.lower()
    match x:
        case "42" | "forty-two" | "Forty-two" | "Forty-Two" | "forty two":
            print("Yes")
        case _:
            print("No")
thoughts()