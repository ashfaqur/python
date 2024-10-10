import functions

print(functions.partition([1,2,3,4],functions.is_even))

cube = lambda number: number * number * number


def decrement_list(numbers):
    return list(map(lambda number: number - 1, numbers))


def is_all_strings(things):
    return all(type(thing) == str for thing in things)
