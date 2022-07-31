
# ? UTIL FUNCTIONS


import random


def list_to_string(lis):
    """Converts a list of strings to a string without comma(,)"""
    return ''.join(lis)


def randomize(list, length):
    """ Returns a random list of length from the given list"""
    return random.sample(list, length)


def shuffle_list(list):
    """Returns a shuffled list of itmes in the given list"""
    random.shuffle(list)
    return list


def shuffle_string(string):
    """Returns a shuffled string of itmes in the given string"""
    string = list(string)
    shuffle_list(string)
    string = list_to_string(string)
    return string
