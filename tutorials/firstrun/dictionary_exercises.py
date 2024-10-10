list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer1 = {list1[index]: list2[index] for index in range(0, 3)}

print(answer1)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answer2 = {item[0]: item[1] for item in person}

print(answer2)

answer3 = dict(person)

print(answer3)

answer = {number: chr(number) for number in range(65, 91)}
print(answer)
