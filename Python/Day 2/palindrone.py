num = int(input("Enter the number: "))
original_num = num
reversed_num = 0

while num > 0:
    rem = num % 10
    reversed_num = reversed_num * 10 + rem
    num = num // 10

if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")
