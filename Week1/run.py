## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''
arr = [5,99,36,54,88]
import array as arr
a = arr.array('i', [5, 99, 36,54,88])
for i in a:
    if i%2 != 0:
        print(i, end=" ")

'''
Problem - 1
Print all the prime numbers from 0-100
'''
lower = 0
upper = 100

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

'''
Problem - 2
Print the reverse of a string
'''
string = 'Reverse Me!'
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = 'Reverse Me!'

print("Reversed string is : ", end="")
print(reverse(s))
