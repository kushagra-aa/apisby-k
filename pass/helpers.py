from operator import le
import random
import string

# Constants
LOWER_CASE_CHARACTERS = string.ascii_lowercase
UPPER_CASE_CHARACTERS = string.ascii_uppercase
DIGITS = string.digits
SEPCIAL_CHARACTERS = string.punctuation
# All characters Constant
ALL_CHARACTERS = LOWER_CASE_CHARACTERS + \
    UPPER_CASE_CHARACTERS+DIGITS+SEPCIAL_CHARACTERS


def generateRandom():
    """
    Returns:
        password: randomly generated password using all characters of random length
    """
    length = random.randint(8, 20)
    return "".join(random.sample(ALL_CHARACTERS, length))


def generateRandomWithLength(length):
    """
    Arguments:
        length (int): length of the password
    Returns:
        password: randomly generated password using all characters of length
    """
    return "".join(random.sample(ALL_CHARACTERS, length))


def generateRandomWithArguments(length, isUpper, isLower, isDigit, isSymbol):
    """
    Arguments:
        length (int): length of the password
    Returns:
        password: randomly generated password using all characters of length
    """
    selectedCharacters = ''
    if isUpper:
        selectedCharacters = selectedCharacters + UPPER_CASE_CHARACTERS
    if isLower:
        selectedCharacters = selectedCharacters + LOWER_CASE_CHARACTERS
    if isSymbol:
        selectedCharacters = selectedCharacters + SEPCIAL_CHARACTERS
    if isDigit:
        selectedCharacters = selectedCharacters + DIGITS
    return "".join(random.sample(selectedCharacters, length))
