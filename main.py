from random import randint
from math import factorial

my_dict = {}


def create_dict():
    for i in range(randint(0, 100)):
        my_dict["key" + str(i)] = i


print(my_dict)

create_dict()


def dict_factorial():
    for j in my_dict:
        my_dict[j] = factorial(my_dict[j])
    return my_dict


print(dict_factorial())
