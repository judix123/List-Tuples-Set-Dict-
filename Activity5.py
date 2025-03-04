def check_palindromee(num):
    str_num = str(num)
    reverse_str = str_num[::-1]

    if str_num == reverse_str:
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not palindrome")

num = int(input("Enter a number: "))
check_palindromee(num)