'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''


def week():
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    for day in days:
        yield day

def yes_or_no():
    say = 'yes'
    while True:
        yield say
        say = 'no' if say == 'yes' else 'yes'

def make_song(count = 99, beverage = 'soda'):
    while count >= 0:
        if count == 0:
            yield 'No more ' + beverage + '!'
        elif count == 1:
            yield 'Only 1 bottle of '+ beverage + ' left!'
        else:
            yield str(count) + ' bottles of '+ beverage + ' on the wall.'
        count -= 1

def get_multiples(num = 1, count = 10):
    start = 1
    while start <= count:
        yield num * start
        start +=1
