import json
from unique import Unique
#from print_result import print_result
import sys

path = 'data_light.json'


with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return Unique(arg, ignore_case=True)
    #raise NotImplemented


@print_result
def f2(arg):
    return filter(lambda x: x == 'Программист', arg)
    #raise NotImplemented


@print_result
def f3(arg):
    raise NotImplemented


@print_result
def f4(arg):
    raise NotImplemented


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))