#PRUEBA
print ('Hello, world!')
name = 'What is your name?'
print ('Hi, %s.',name)

import keyword
print(keyword.kwlist)

for i in range(1,11):
    if i == 5:
        break
    print(i)
print('fin for')
num = 3
if num > 0:
    print(num, 'is a positive number.')
print('This is always printed.')

num = -1
if num > 0:
    print(num, 'is a positive number.')
print('This is also always printed.')

A = [1,2,3,4]
print(A[1])
print(A)
print(A[-1])
