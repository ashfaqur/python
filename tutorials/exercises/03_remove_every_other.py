'''
remove_every_other([1,2,3,4,5]) # [1,3,5]
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1]
'''

def remove_every_other2(given_list):
    indices = range(len(given_list))
    skip = False
    newList = []
    for i in indices:
        if skip:
            skip = False
            continue
        newList.append(given_list[i])
        skip = True
    return newList

def remove_every_other(given_list):
    return [item for i,item in enumerate(given_list) if i%2==0]

print(remove_every_other([1,2,3,4,5]))
print(remove_every_other([5,1,2,4,1]))
print(remove_every_other([1]))