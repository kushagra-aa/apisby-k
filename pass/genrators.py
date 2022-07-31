from operator import le
import random
from sre_parse import SPECIAL_CHARS
import string

from .utils import randomize, shuffle_string, list_to_string

# Constants
LOWER_CASE_CHARACTERS = string.ascii_lowercase
UPPER_CASE_CHARACTERS = string.ascii_uppercase
DIGITS = string.digits
SEPCIAL_CHARACTERS = string.punctuation
# All characters Constant
ALL_CHARACTERS = LOWER_CASE_CHARACTERS + \
    UPPER_CASE_CHARACTERS+DIGITS+SEPCIAL_CHARACTERS

# ! GENRATOR FUNCTIONS


def generateRandom():
    """
    Returns:
        password: randomly generated password using all characters of random length
    """
    length = random.randint(8, 20)
    return list_to_string(randomize(ALL_CHARACTERS, length))


def generateRandomWithLength(length):
    """
    Arguments:
        length (int): length of the password
    Returns:
        password: randomly generated password using all characters of length
    """
    return list_to_string(randomize(ALL_CHARACTERS, length))


def generateRandomWithArguments(length, isUpper, isLower, isDigit, isSymbol):
    """
    This Function generates a random password using the specified character types of length
    Arguments:
        length (int): length of the password
        isUpper,isLower,isDigit,isSymbol: booleans that determine the characters in the password
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
    return list_to_string(randomize(selectedCharacters, length))


def generateRandomWithCustom(length, Upper, Lower, Digit, Symbol):
    """
    This Genrates a random password with custom number of characters
    Arguments:
        length (int): length of the password
    Returns:
        password: randomly generated password using all characters of length
        Upper,Lower,Digit,Symbol: integers that determine the number of their sepecific characters types in the password
    """
    selectedCharacters = []
    if Upper > 0:
        selectedCharacters.append(
            list_to_string(randomize(UPPER_CASE_CHARACTERS, Upper)))
    if Lower > 0:
        selectedCharacters.append(
            list_to_string(randomize(LOWER_CASE_CHARACTERS, Lower)))
    if Symbol > 0:
        selectedCharacters.append(
            list_to_string(randomize(SPECIAL_CHARS, Symbol)))
    if Digit > 0:
        selectedCharacters.append(list_to_string(randomize(DIGITS, Digit)))
    selectedCharacters = list_to_string(selectedCharacters)
    shuffle_string(selectedCharacters)
    return selectedCharacters


def generateRandomPerfect():
    """
    It Genrates a password of 10 random characters where ther is always atleast,
    2 random digits,lower,upper,symbols
    Arguments:
        length (int): length of the password
    Returns:
        password: randomly generated password using all characters of 10 character
    """
    selectedCharacters = []
    length = 2
    selectedCharacters.append(list_to_string(
        randomize(UPPER_CASE_CHARACTERS, 2)))
    selectedCharacters.append(list_to_string(
        randomize(LOWER_CASE_CHARACTERS, 2)))
    selectedCharacters.append(list_to_string(randomize(SPECIAL_CHARS, 2)))
    selectedCharacters.append(list_to_string(randomize(DIGITS, 2)))
    selectedCharacters.append(list_to_string(
        randomize(ALL_CHARACTERS, length)))
    selectedCharacters = list_to_string(selectedCharacters)
    shuffle_string(selectedCharacters)
    return selectedCharacters


def generateRandomWithMinimum(length, Upper, Lower, Digit, Symbol):
    """
    This Genrates password that will have atleast one character from the given character types
    Arguments:
        length (int): length of the password
    Returns:
        password: randomly generated password using all characters of length
        isUpper,isLower,isDigit,isSymbol: booleans that determine the characters in the password
    """
    selectedCharacters = []
    if Upper:
        selectedCharacters.append(
            list_to_string(randomize(UPPER_CASE_CHARACTERS, 1)))
        length -= 1
    if Lower:
        selectedCharacters.append(
            list_to_string(randomize(LOWER_CASE_CHARACTERS, 1)))
        length -= 1
    if Symbol:
        selectedCharacters.append(
            list_to_string(randomize(SPECIAL_CHARS, 1)))
        length -= 1
    if Digit:
        selectedCharacters.append(list_to_string(randomize(DIGITS, 1)))
        length -= 1
    selectedCharacters.append(list_to_string(
        randomize(ALL_CHARACTERS, length)))
    selectedCharacters = list_to_string(selectedCharacters)
    shuffle_string(selectedCharacters)
    return selectedCharacters
