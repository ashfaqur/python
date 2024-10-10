nameList = ['Elie', 'Tim', 'Matt']

answer = [name[0] for name in nameList]

print(answer)

numberList = [1, 2, 3, 4, 5, 6]

answer2 = [number for number in numberList if number % 2 == 0]

print(answer2)

firstNumberList = [1, 2, 3, 4]
secondNumberList = [3, 4, 5, 6]

answer3 = [number for number in firstNumberList if number in secondNumberList]

print(answer3)

answer4 = [name[-1::-1].lower() for name in nameList]

print(answer4)

answer5 = [number for number in range(1, 101) if number % 12 == 0]
print(answer5)

answer6 = [char for char in "amazing" if char not in ['a', 'e', 'i', 'o', 'u']]

print(answer6)

answer7 = [[number for number in range(0, 3)] for number in range(0, 3)]
print(answer7)

answer8 = [[i for i in range(0, 10)] for num in range(0, 10)]
print(answer8)
