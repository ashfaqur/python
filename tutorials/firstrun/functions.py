def product(num1, num2):
    return num1*num2


def return_day(day):
    days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesay', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    return days.get(day)


def last_element(number_list):
    if number_list:
        return number_list[-1]
    else:
        return None


def number_compare(num1, num2):
    if num1 > num2:
        return "First is greater"
    elif num1 == num2:
        return "Numbers are equal"
    else:
        return "Second is greater"


def single_letter_count(text, find):
    return text.lower().count(find)


x = single_letter_count("Hello", 'h')
print(x)


def multiple_letter_count(text):
    return {character: text.count(character) for character in text}


def list_manipulation(numberList, command, location, value=None):
    if command == 'remove':
        if location == 'end':
            return numberList.pop()
        elif location == 'beginning':
            return numberList.pop(0)
    elif command == 'add':
        if location == 'end':
            numberList.append(value)
            return numberList
        elif location == 'beginning':
            numberList.insert(0, value)
            return numberList


def is_palindrome(text):
    """

    :type text: str
    """
    text = text.strip().count()
    palindrome = text[::-1]
    return text == palindrome


def frequency(number_list, find):
    count = 0
    for num in number_list:
        if find == num:
            count = count + 1
    return count


def contains_purple(*args):
    if 'purple' in args:
        return True
    return False


def combine_words(word, **kwargs):
    prefix = kwargs.get('prefix')
    if prefix:
        return prefix + word
    suffix = kwargs.get('suffix')
    if suffix:
        return word + suffix
    return word


combination = combine_words('child', prefix="man")
print(combination)


# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1,4,7)

result2 = count_sevens(*nums)


def compact(generic_list):
    return [item for item in generic_list if item]


def intersection(list1, list2):
    return [item for item in list1 if item in list2]


def is_even(num):
    return num % 2 == 0

def partition(a_list, func):
    list1 = [num for num in a_list if func(num)]
    list2 = [num for num in a_list if not func(num)]
    return [list1,list2]
