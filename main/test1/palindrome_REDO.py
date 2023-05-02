a = input('value: ')
print(a)
print(len(a))


def is_palindrome(a):
    return a == a[::-1]
# works only for 1 word, not for sencences


if a == a[::-1]:
    True
    print('oki')
else:
    print('no')
