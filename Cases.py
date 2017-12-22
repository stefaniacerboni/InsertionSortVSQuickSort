import Algorithm
import random

def worstQCK(n):
    vector = range(n)
    Algorithm.quick_sort(vector, 0, len(vector) - 1)


def worstINSRT(n):
    vector = range(n)
    rotcev = list(reversed(vector))
    Algorithm.insertion_sort(rotcev)


def avgINSRT(n):
    vector = range(n)
    random.shuffle(vector)
    Algorithm.insertion_sort(vector)


def avgQCK(n):
    vector = range(n)
    random.shuffle(vector)
    Algorithm.quick_sort(vector, 0, len(vector) - 1)


def bestQCK(n):
    vector = range(n)
    Algorithm.best_quick_sort(vector, 0, len(vector) - 1)


def bestINSRT(n):
    vector = range(n)
    Algorithm.insertion_sort(vector)