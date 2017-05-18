"""
This module handles various versions of fibonnaci
"""

def fib1(num):
    """
    naive way of doing fibonacci: update one state at a time
    :param num: input
    :return: fibonacci sequence
    """
    first = 0
    second = 1
    for _ in range(num):
        print first
        tmp = second
        second = first+second
        first = tmp


def fib2(num):
    """
    update multiple states together
    :param num: input
    :return: fibonacci sequence
    """
    first = 0
    second = 1
    for _ in range(num):
        print first
        first, second = second, first+second

if __name__ == '__main__':
    N = 5
    # fib1(N)
    fib2(N)
