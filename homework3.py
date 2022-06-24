'''homework3'''

def contain(data, val):
    '''this function checks if the given value is in list'''
    i = 0
    while i < len(data):
        if data[i] == val:
            return True
        i += 1
    return False

data1=[1, 5, 7, 8]
print(contain(data1, 2))




def _pop(data, i = None):
    '''this function deletes the number with index i and returnes it as a result'''
    if i is None:
        _len = len(data) - 1
        data.remove(data[_len])
        return data
    save = data[i]
    data.remove(data[i])
    return save

data2=[1, 5, 7, 8]
print("deleted", _pop(data2, 2), "data", data2)



def contain1(data, value):
    '''this function returns how many times is the number in the list'''
    i = 0
    _contain = 0
    while i < len(data):
        if data[i] == value:
            _contain += 1
        i += 1
    return _contain

def remave_all(data, val):
    '''this function deletes all numbers in the data with value equal to given'''
    count = contain1(data, val)
    if count == 0:
        raise ValueError('remove_all(x): x not in list')
    while count:
        data.remove(val)
        count -= 1
    return data

lst1 = [5, 2, 5, 5, 9, 5, 5, 5, 7, 5]
print(remave_all(lst1, 5))



def reverse(data):
    '''this function reverses the list'''
    j = len(data) - 1
    i = 0
    while i < j:
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1
    return data

lst2 = [1, 2, 3, 4, 5, 8, 8]
print("reversed list = ", reverse(lst2))



def _max(data):
    '''this function returns max element of the list'''
    i = 1
    _max = data[0]
    while i < len(data):
        if data[i] > _max:
            _max = data[i]
        i += 1
    return _max

data3 = [1, 7, 8, -1, 9, 3]
print("max=", _max(data3))



def _min(data):
    '''this function returns min element of the list'''
    i = 1
    _min = data[0]
    while i < len(data):
        if data[i] < _min:
            _min = data[i]
        i +=1
    return _min

data4 = [1, 7, 8, -1]
print("min=", _min(data4))
