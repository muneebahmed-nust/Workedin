import re

def is_aplph_only(string):
    for c in string:
        if not ('a'<=c<='z' or 'A'<=c<='Z' or ' ' in c):
            return False
    return True

def is_number_only(string):
    for n in string:
        if not('0'<=n<='9' or n==' '):
            return False
    return True


