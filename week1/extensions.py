def main():
    user_input = input("Enter file name: ").strip()
    new_user_input = user_input.lower().split(".")
    file_extension = new_user_input[-1]

    match file_extension:
        case 'gif':
            print("image/gif")
        case 'png':
            print("image/png")
        case 'jpg' |'jpeg':
            print("image/jpeg")
        case 'pdf' | 'zip':
            print("application/" + file_extension)
        case 'txt':
            print("text/plain")
        case _:
            print("application/octet-stream")

main()
