palindrome = int(input("Enter the Number : "))
num = 1
while(num<=palindrome):
    rem = palindrome % 10
    num += 1
    print(rem)