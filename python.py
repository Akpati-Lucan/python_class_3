# Create a function that would return this: i-am-a-boy
# from I am a boy meaning convert it to lowercase and replace
# the space with hyphen

# def header_change(a):
#     b = a.lower()
#     c = b.replace(' ','+')
#     print(c)

# you = 'I am a Boy'
# header_change(you)

# def header(a):
#     print(a.replace(' ','-').lower())

# header('yUo aRE NOT A boy')


# def username(a,b):
#     c = a[:-2]
#     d = b[2:]
#     e = c+d
#     return(e)

# print(username('harry','maguire'))

# in index [:2] = return first two
# in index [2:] = return everything but first two
# in index [-2:] = return last two
# in index [:-2] = return evrything but last two


# a = lambda x : x + 15
# print(a(2)) 

# b = lambda x,y : x*y
# # print(b(3,4))
# str = 'RRRRrrrrr'
# print(str.swapcase())



# num = lambda string : string.isnumeric()

# print(num('5'))

# a = input('Enter filename here > ')
# b = a.split('.')
# print(b[1])


# def factorial(x):
#     if x == 1:
#         return 1
#     return x * factorial(x-1)

# print(factorial(5))

# arr = [23,45,12,44,9]
# a = map(lambda x : x*3 , arr)
# b = map(lambda y : y**2 , arr)

# print(list(a))
# print(list(b)) 

# a = [0, 1, 22, 3, 10, 5, 61, 7, 8, 9]
# x = [0, 56, 34, 32, 4, 9, 55, 5]

# print(a[4])
# print(a[0:7:2])
# a[4] = 0
# print(a[4])
# a[4] = 4

# print(a+x)

# my_list = [2,3,4,2,[2,3,4,5, [4,52,2],5],24]

# print(my_list[4][4][1] + my_list[5])

# a.sort(reverse=True)
# print(a)
# print(a[1])
# print(a[-2])

# print(a[-3:])
# print(a[:3])


# t = ['a', 'B', 'c', 'D', 'e', 'F']

# print(list(filter(lambda x : x.isupper() , t)))


# write a programme that takes input from the user.The number should
# be separated by comma. Then print only odd numbers

# a = input('Enter numbers > ')
# b = a.split(',')
# print(b)
# c = map(int,b)
# print(list(filter(lambda x : (x % 2) == 1 , c)))

# x = 'bananna'
# y = 'bananna'
# print(x==y)
# print(x is y)


# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a==b)
# print(a is b)

# d = [4, 7, 9]
# e = d
# f = d.copy()
# print(e is d)
# print(f is d)

# create a function that takes in a list and returns all elements
# but the first and last

# def my_function(a):
#     print(a[1:-1])
#     return a[1:-1]

# lit = [0, 1, 2, 3, 4]
# my_function(lit)


# def my_function_1(a):
#     a.sort()
#     b = len(a)//2
#     return a[b]

# print(my_function_1(lit))


# num = -1

# if num > 5:
#     print('it is greater than 5')
# elif num == 5:
#     print('it is equal to 5')
# elif num < 5:
#     if num > 0:
#         print('num is positive but less than 5')
#     else:
#         print('num is negative therefore less than 5')


# from dataclasses import replace
# from itertools import count
import random 

a = [2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'select any number from {a}. \nWe hope it doesn\'t end up in tears' )
while True:
    comp_choice = random.choice(a)
    random.shuffle(a)
    print('Guess the number:')
    user_choice = int(input('>'))
    print(f'the computer choose {comp_choice}')

    if user_choice in a :
        if user_choice == comp_choice:
            print('All power belongs to you comerade.')
        else:
            print('Arhhh, comerade. Be like you go try again o.')
    else:
        print('Comerade, no be so!!!!')

    c = input('do you want to keep playing \n >')
    if c == 'y':
        continue
    else:
        break




# text = 'I am a very good boy'

# sub_text = input('Enter text to search for:\n > ')

# lowercase_text = text.lower()
# found = lowercase_text.find(sub_text)
# count = lowercase_text.count(sub_text)
# if found != -1:
#     print(f'{count} result(s) found!')
#     new_text = text.replace(sub_text, sub_text.upper())
#     print(new_text)
# else:
#     print(f'{count} result(s) found')



# def check_format():
#     a = int(input('Value for A > '))
#     b = int(input('Value for B > '))
#     c = int(input('Value for C > '))
#     n = int(input('Value for N > '))

#     ans_1 = (a**n) + (b**n) 
#     ans_2 = (c**n)

#     if n > 2 :
#         if ans_1 == ans_2 :
#             print('Holy smokes, Fermat was wrong!')
#         else:
#             print('No, that doesn’t work.')
#     else: 
#         print('N must be greater than 2 change your value for N')



