confirm_pass = input("confirm pass: ")
while (password != confirm_pass):
    print("confirm pass not match")
    confirm_pass = input("confirm pass again: ")
    continue