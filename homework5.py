'''homework 5'''

def split(source, sep, count = None):
    '''this function splits string by given substring'''
    if count is None:
        count = source.count(sep)
    str1 = ''
    arr1 = []
    len1 = len(sep)
    i = 0
    while i < len(source):
        if count != 0 and source[i:i+len1] == sep:
            arr1.append(str1)
            str1 = ''
            count -= 1
            i += len1
        else:
            str1 += source[i]
            i += 1
    arr1.append(str1)
    return arr1

print(split('ertyutyit','ty'))



def join(data, sep):
    '''this function joins elements of array by given string'''
    str1 = ""
    for i in data:
        str1 = str1 + i + sep
    return str1

print(join(["yu", "gf", 'df', "hjk", "8"], "#"))


def replace(source, old, new, count):
    '''this function replaces given substring with new one by given count'''
    str1 = []
    source1 = split(source, " ")
    while count:
        for i in source1:
            if count != 0 and i == old:
                str1.append(new)
                count -=1
            else:
                str1.append(i)
    return join(str1, " ")


print(replace("one one was a race horse, two two was one too.", "one", "two", 2))
