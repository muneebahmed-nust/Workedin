import re

def not_letter(string):
    for c in string:
        if not ('a'<=c<='z' or 'A'<=c<='Z' or ' ' in c):
            return True
    return False

def not_numeric(string):
    return not(is_number_only(string))

def is_number_only(string):
    for n in string:
        if not('0'<=n<='9' or n==' '):
            return False
    return True

def dob_checker(dob):
    num=dob.split("/")
    for n in num:
        if not_numeric(n):
            return False
    return True