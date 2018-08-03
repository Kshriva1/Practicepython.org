str1 = input("Enter the string input: ")


def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

if str1 == reverse(str1):
    print("String is palindrome")
else:
    print("String is not palindrome")
