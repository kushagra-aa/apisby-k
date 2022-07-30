from operator import le
import random
import string

LOWER_CASE_CHARACTERS = string.ascii_lowercase
UPPER_CASE_CHARACTERS = string.ascii_uppercase
DIGITS = string.digits
SEPCIAL_CHARACTERS = string.punctuation

ALL_CHARACTERS = LOWER_CASE_CHARACTERS + \
    UPPER_CASE_CHARACTERS+DIGITS+SEPCIAL_CHARACTERS


def genrateRandom():
    """
    Returns:
        password: randomly generated password using all characters of random length
    """
    length = random.randint(8, 20)
    return "".join(random.sample(ALL_CHARACTERS, length))


def genrateRandomWithLength(length):
    """
    Arguments:
        length (int): length of the password
    Returns:
        password: randomly generated password using all characters of length
    """
    return "".join(random.sample(ALL_CHARACTERS, length))
