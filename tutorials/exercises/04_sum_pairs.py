'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

def sum_pairs(num_list, total):
    visited_number = set()

    for num in num_list:
        require = total-num
        if require in visited_number:
            return [require, num]
        visited_number.add(num)
    return []