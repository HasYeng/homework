'''homework4'''

def triple(num):
    '''this function multiplies by 3'''
    return num*3

def _map(func, lst):
    '''this function maps function to list's elements'''
    i = 0
    res = [None]*len(lst)
    while i < len(lst):
        res[i] = func(lst[i])
        i += 1
    return res

lst1 = [4, 5, 6, 8]
print(_map(triple, lst1))



def funcion(num1, num2, num3):
    '''this function sums 3 numbers'''
    return num1 + num2 + num3

def map3(func, data1, data2, data3):
    '''this function maps function to lists'''
    data_res = [None]*len(data1)
    for i in range(len(data1)):
        data_res[i] = func(data1[i], data2[i], data3[i])
    return data_res

_data1 =[4, 5, 6, 8]
_data2 =[40, 50, 60, 80]
_data3 =[14, 15, 16, 18]
print(map3(funcion, _data1, _data2, _data3))


def deg(base, exp):
    '''this function raises a number to a given power'''
    return base**exp

def map2(func, data1, data2):
    '''this function maps function to lists' elements'''
    data_res = [None]*len(data1)
    for i in range(len(data1)):
        data_res[i] = func(data1[i], data2[i])
    return data_res

data4=[2, 3, 4, 1]
data5=[3, 2, 1, 4]
print(map2(deg, data4, data5))
