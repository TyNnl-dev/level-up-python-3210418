"""
# Python Code Challenge #4: Find All List Items

Your goal is to implement a function, `index_all()`, that takes a list of objects and the item to search for as input arguments and returns a list of indices for where that item exists within the list.

NOTE: Since the input argument could be a list of lists, your function should be able to traverse multidimensional lists to find all instances of the item, and the elements of the returned list should also be lists to indicate multidimensional indices.

## Example Test Output
```console
>>> example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
>>> index_all(example, 2)
[[0, 0, 1], [0, 1], [1, 1]]
>>> print(index_all(example, [1, 2, 3]))
[[0, 0], [1]]
```

"""

def index_all(search_list, number):
  index_list = []
  for index, value in enumerate(search_list):
    if value == number:
      index_list.append([index])
    elif isinstance(search_list[index], list):
      for i in index_all(search_list[index], number):
        index_list.append([index] +i)
  return index_list

example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(index_all(example, 3))