'''homework1'''

#1.3
def squere_sum(num1, num2):
    '''returns the sum of the squares of the given numbers'''
    return num1**2 + num2**2

def squere_sum2(num1, num2, num3):
    '''this function returns sum of the squares of two largest numbers from given three'''
    if num1 < num2 and num1 < num3:
        return squere_sum(num2, num3)
    if num2 < num1 and num2 < num3:
        return squere_sum(num1, num3)
    return squere_sum(num1, num2)

print("sum of the squares:", squere_sum2(4, 2, 5))


#1.5 , 1.6
def bigger(num1, num2):
    '''returns the sum of numbers between the given,
    even if the first is the smaller one
    '''
    if num1 < num2:
        return between_sum(num1, num2)
    return between_sum(num2, num1)

def between_sum(num1, num2):
    '''returns the sum of numbers between the given'''
    num_sum=0
    while num1 != num2:
        num_sum = num1 + num2
        num1 += 1
    return num_sum

print("sum of numbers between the given:", bigger(10 ,5))



#1.7
def _pow(base, exp):
    '''raising a number to a given power'''
    if base == 0 and exp <= 0:
        raise ZeroDivisionError("division by zero")
    if exp > 0:
        return base**exp
    if exp < 0:
        return 1 / base**(-exp)
    return 1

print(_pow(4, -3))


#1.8
def approx(num, app):
    '''approximation'''
    return ((num / (app**2)) + (2*app)) / 3

def check(test,num):
    '''comparing the approximation to the cubic root '''
    if abs(test**3 - num) < 0.00001:
        return True
    return False

def cube_root(num):
    '''finding an approximate cubic root'''
    app = 1
    while check(approx(num, app), num) is False:
        app = approx(num, app)
    return app

print ('cubic root is:', cube_root(27))
