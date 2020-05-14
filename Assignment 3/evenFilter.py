from typing import Any, Callable, Union

list1 = [1, 2, 3, 4, 5]

even = lambda num: num % 2 == 0

list2 = list(filter(even, list1))
print(list2)
odd = lambda num: num % 2 != 0
list3 = list(filter(odd, list1))
print(list3)
