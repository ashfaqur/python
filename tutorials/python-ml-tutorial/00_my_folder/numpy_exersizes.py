import numpy as np

num_list = list(range(0,10))
print(num_list)

np_array = np.array(num_list)
print(np_array)

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

np_matrix = np.array(my_matrix)
print(np_matrix)

np_range = np.arange(0,10)
print(np_range)

random_array = np.random.randint(10,51,20)
print(f'random_array {random_array}')
random_array_reshape = random_array.reshape(4,5)
print(f'random_matrix\n {random_array_reshape}')

print(random_array.dtype)
