A = input()

# Please write your code here.

def is_palindrome(string):
    if string[::-1] == string:
        print('Yes')
    else:
        print('No')


is_palindrome(A)