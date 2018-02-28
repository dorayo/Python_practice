#!/usr/bin/env python3

def is_palindrome0(n):
    s = str(n)
    for i  in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome0, range(1, 1000))
print(list(output))
