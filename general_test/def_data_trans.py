import random

def exChange(list, low, high):
    list[low], list[high] = list[high], list[low]
    print(list)
    #list = list[::-1]
    #list[high-1] = 5
    random.shuffle(list)
    print(list)


data = [1,2,3,4]

print('original data is:', data)
exChange(data, 0, 1)
print('after precess :  ', data)