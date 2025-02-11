from collections import deque
import string


def rotate(text, key):
    rotate_list = []
    for x in text:
        if x.islower():
            rotate_list.append(chr(((ord(x) - 97 + key) % 26) + 97))
        elif x.isupper():
            rotate_list.append(chr(((ord(x) - 65 + key) % 26) + 65))
        elif x.isdigit():
            rotate_list.append(x)
        elif x in string.punctuation:
            rotate_list.append(x)
        elif x == ' ':
            rotate_list.append(x)


    return ''.join(rotate_list)

code = input()
key = input()

print(rotate(code,int(key)))
