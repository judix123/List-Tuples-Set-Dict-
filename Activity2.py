number = int(input("Enter a number: "))
order = len (str(number))
sum_number = sum(int(digit) ** order for digit in str(number))
if number == sum_number:
    print(f"{number} is an Armstrong")
else:
    print(f"{number} is not an Armstrong")
