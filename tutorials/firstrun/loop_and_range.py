# Add up all odd numbers between 10 and 20
numbers = list(range(10,21))
print(f'numbers {numbers}')
# Store the result in x:
x = 0

for ele in numbers:
    if ele % 2 != 0:
        x += ele


print(f'Sum is {x}')
