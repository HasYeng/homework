'''homework2'''

#1.11 recursion

def func1(num):
    '''this function returns f(n) = n, if  n < 3
    f(n) = f(n - 1) + f(n - 2) + f(n - 3), if n >= 3
    '''
    if num <= 3:
        return num
    return func1(num - 1) + func1(num - 2) + func1(num - 3)

print("f(n)=", func1(8))


#1.12 iteration

def func2(num):
    '''this function returns f(n) = n, if  n < 3
    f(n) = f(n - 1) + f(n - 2) + f(n - 3), if n >= 3
    '''
    if num <= 3:
        return num
    num1 = 0
    num2 = 1
    num3 = 2
    while num - 2:
        _sum = num1 + num2 + num3
        num1 = num2
        num2 = num3
        num3 = _sum
        num -= 1
    return _sum

print("f(n)=", func2(8))



#1.11 tail recursion

def func3(num, num1 = 1, num2 = 2, num3 = 3):
    '''this function returns f(n) = n, if  n < 3
    f(n) = f(n - 1) + f(n - 2) + f(n - 3), if n >= 3
    '''
    if num == 1:
        return num1
    if num == 2:
        return num2
    if num == 3:
        return num3
    return func3(num - 1, num2, num3, num1 + num2 + num3)

print("f(n)=", func3(8))


#1.12

def pascal(row, pos):
    '''this function returns a number from Pascal's triangle by given row and position'''
    if pos in (1, row):
        return 1
    return pascal(row - 1, pos) + pascal(row - 1, pos -1)

print("a number from Pascal's triangle", pascal(6, 3))



# 1.13

def is_even(num):
    '''this function checks if the number is even'''
    if num%2==0:
        return True
    return False

def fast_pow(base, deg):
    '''this function returns base raised by given degree'''
    if deg  == 0:
        return 1
    res = 1
    count = 0
    if is_even(deg):
        count1 = 0
        while is_even(deg):
            count1 += 1
            deg /= 2
        while count < deg:
            res *= base
            count += 1
        while count1:
            res **= 2
            count1 -= 1
    while count < deg:
        res *= base
        count += 1
    return res

print("power", fast_pow(3,4))


#1.14

def double(num):
    '''this function returns doubled the number'''
    return num*2

def fast_mul(num1, num2):
    '''this function returns num1 multiplied by num2'''
    if num2 == 0:
        return 0
    if is_even(num2):
        return double(fast_mul(num1, num2 / 2))
    return num1 + fast_mul(num1, num2 - 1)

print("multiplication", fast_mul(3,8))
