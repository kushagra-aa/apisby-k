from operator import le
import random
from sre_parse import SPECIAL_CHARS
import string

from .utils import randomize, shuffle_list, shuffle_string, list_to_string

# Constants
LOWER_CASE_CHARACTERS = string.ascii_lowercase
UPPER_CASE_CHARACTERS = string.ascii_uppercase
DIGITS = string.digits
SEPCIAL_CHARACTERS = string.punctuation
# All characters Constant
ALL_CHARACTERS = LOWER_CASE_CHARACTERS + \
    UPPER_CASE_CHARACTERS+DIGITS+SEPCIAL_CHARACTERS

# Mappings for letter encodings
LETTER_MAPS = {
    "A": ['A', 'a', '1', '2', '@', '!'],
    "B": ['B', 'b', '2', '?'],
    "C": ['C', 'c', '3', '2', '(', ')'],
    "D": ['D', 'd', '4', '3', '|)'],
    "E": ['E', 'e', '5', '3', '[', '|-'],
    "F": ['F', 'f', '6', '3', '=', '|='],
    "G": ['G', 'g', '7', '4', '+'],
    "H": ['H', 'h', '8', '4', '#', '|-|'],
    "I": ['I', 'i', '9', '4', '!', '|.'],
    "J": ['J', 'j', '10', '5', '%'],
    "K": ['K', 'k', '11', '5', '<', '>'],
    "L": ['L', 'l', '12', '5', '|_'],
    "M": ['M', 'm', '13', '6', '|^|', '|\\/|'],
    "N": ['N', 'n', '14', '6', '|\\|', '|/|'],
    "O": ['O', 'o', '15', '6', '0'],
    "P": ['P', 'p', '16', '7', ':', '"'],
    "Q": ['Q', 'q', '17', '7', ',0'],
    "R": ['R', 'r', '18', '7', '|\\'],
    "S": ['S', 's', '19', '7', '&', '$'],
    "T": ['T', 't', '20', '8', '_|_', '+'],
    "U": ['U', 'u', '21', '8', '|_|'],
    "V": ['V', 'v', '22', '8', '\\/'],
    "W": ['W', 'w', '23', '9', '\\^/'],
    "X": ['X', 'x', '24', '9', '/\\'],
    "Y": ['Y', 'y', '25', '9', ';', ':'],
    "Z": ['Z', 'z', '26', '9', '-/_'],
}


# ! GENRATOR FUNCTIONS


def generateRandom():
    """
    Returns:
        password: randomly generated password using all characters of random length
    """
    length = random.randint(8, 40)
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


def generateFromString(string, isPerfect):
    """
    This Genrates password from the given string
    uses LETTER_MAPS
    Arguments:
        string (str): string to convert to password
        isPerfect (bool): determines if the password should have all types of characters
    Returns:
        password: randomly generated password using string
    """
    password = []
    perfect = []
    for letter in string:
        password.append(list_to_string(
            randomize(LETTER_MAPS[letter.upper()], 1)))
    if isPerfect:
        perfect.append(list_to_string(
            randomize(UPPER_CASE_CHARACTERS, 1)))
        perfect.append(list_to_string(
            randomize(LOWER_CASE_CHARACTERS, 1)))
        perfect.append(list_to_string(
            randomize(SPECIAL_CHARS, 1)))
        perfect.append(list_to_string(
            randomize(DIGITS, 1)))
        perfect = shuffle_list(perfect)
        password.append(list_to_string(perfect))
    password = list_to_string(password)
    return password
