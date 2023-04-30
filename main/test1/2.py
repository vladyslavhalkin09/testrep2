str1 = 'James'
print(str1)
print(len(str1))
print(str1[0]+str1[2]+str1[-1])

a = input('value; ')
print(a)
print(len(a))

if (a[:3] == a[3:]):
    print('xd done')
else:
    print('kekw')

# if (a[0] + a[1] + a[2] == a[-1] + a[-2] + a[-3]):
#    print('luck its a palindrom')
# else:
#    print('no luck')


def is_palindrome(a):
    return a == a[::-1]


if True:
    print('ok')
else:
    print('nah')
