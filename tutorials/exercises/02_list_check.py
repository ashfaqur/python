'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

def list_check2(given_list):
    if isinstance(given_list, list):
        bool_check = map(lambda item : isinstance(item, list),given_list)
        for bool in bool_check:
            if not bool:
                return False
        return True
    return False

def list_check(given_list):
    if isinstance(given_list, list):
        return all([isinstance(item, list) for item in given_list])
    return False

print(list_check([[1,2,3]]))