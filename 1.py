"""Convert string into capital letters."""
try:
    ans = []
    for _ in range(int(input("Enter Number of Test Cases: "))):
        string = input("Enter String: ")
        string_upper = ""

        for each in string:
            asc = ord(each)
            if asc >= 97 and asc <= 122:
                string_upper += chr(asc-32)
            else:
                string_upper += each

        ans.append(string_upper)
    print("\n\nString(s) after Converting to Upper Case\n")
    print("\n".join(ans))
    print()
except Exception:
    print("Invalid Input Supplied... Please Try Again...")
