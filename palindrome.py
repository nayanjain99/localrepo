def isPalindrome(s):
    return s == s[::-1]
s = input("Enter a String:")
ans = isPalindrome(s)

if ans:
    print("String is palindrome")
else:
    print("Not palindrome")