import random
import time
from itertools import permutations
import os

global_dict = "abcdefghijklmnopqrstuvwxyz"


def main():
    """
    This is the main method for Project 1.
    """
    main_menu()
    for i in generate_true_test_data(50, 2).split('\n'):
        print(i, '\t', is_anagram_better_method(i.split(',')[0], i.split(',')[1]))
    for i in generate_true_test_data(50, 2).split('\n'):
        print(i, '\t', is_anagram_brute_force(i.split(',')[0], i.split(',')[1]))


def main_menu():
    os.system('clear')
    print('Welcome to the anagram algorithm tester!')
    print('Please choose an option: ')
    print('1: Run both algorithms with input strings')
    get_menu_choice(input(' >>  '))
    # TODO: finish menus


def get_menu_choice(choice):
    choice = choice.lower()
    if choice == '1':
        print('You chose 1')
    # TODO: finish menus


def is_anagram_brute_force(string1, string2):
    """
    Detect whether or not string2 is an anagram of string1 using
    a brute force algorithm.
    :param string1: The first string to test.
    :param string2: The second string to test.
    :return: A tuple, the first value is a boolean of whether or not the
    second string is an anagram of the first. The second value is a float
    of the runtime of the operation.
    """
    # TODO: DO COMPUTATION
    is_anagram = False
    start_time = time.time()
    string1_permutations = [''.join(p) for p in permutations(string1)]
    string1_permutations = set(string1_permutations)  # Removes duplicates
    if string2 in string1_permutations:
        is_anagram = True
    end_time = time.time()
    return is_anagram, (end_time - start_time)


def is_anagram_better_method(string1, string2):
    """
    Detect whether or not string2 is an anagram of string1 using
    my devised method.
    :param string1: The first string to test.
    :param string2: The second string to test.
    :return: A tuple, the first value is a boolean of whether or not the
    second string is an anagram of the first. The second value is a float
    of the runtime of the operation.
    """
    string1_letter_count = build_letter_count_dict(global_dict)
    string2_letter_count = build_letter_count_dict(global_dict)
    is_anagram = True
    start_time = time.time()
    for i in string1:
        string1_letter_count[i] += 1
    for i in string2:
        string2_letter_count[i] += 1
    for i in global_dict:
        if string1_letter_count[i] != string2_letter_count[i]:
            is_anagram = False
            break
    end_time = time.time()
    return is_anagram, (end_time - start_time)


def build_letter_count_dict(letters):
    """
    Build a dictionary to count letter occurrences.
    :param letters: The letters to build the dictionary on.
    :return: The filled dict.
    """
    letter_count = {}
    for i in letters:
        letter_count[i] = 0
    return letter_count


def generate_true_test_data(length, number):
    """
    Generate testing data for the anagram algorithm. This method
    generates a large number of test anagram strings for the algorithm
    to be tested against. It is different each time it is run, due
    to its use of the built-in pseudo random number generator.
    :param length: Generate strings in length from 1 to this length.
    :param number: Generate this number of strings at each length.
    :return: A string containing all of the test string data.
    """
    return_string = []
    for i in range(1, length+1):
        for j in range(1, number+1):
            initial_string = ""
            for k in range(1, i+1):
                initial_string += random.choice(global_dict)
            string_list = list(initial_string)
            random.shuffle(string_list)
            jumbled_string = ''.join(string_list)
            anagram_string = initial_string + ',' + jumbled_string
            return_string.append(anagram_string)
    return '\n'.join(return_string)


def generate_false_test_data(length, number):
    """
    Generate testing data for the anagram algorithm. This method
    generates a large number of test incorrect anagram strings for the algorithm
    to be tested against. It is different each time it is run, due
    to its use of the built-in pseudo random number generator.
    :param length: Generate strings in length from 1 to this length.
    :param number: Generate this number of strings at each length.
    :return: A string containing all of the test string data.
    """
    return_string = []
    for i in range(1, length+1):
        for j in range(1, number+1):
            initial_string = ''
            for k in range(1, i+1):
                initial_string += random.choice(global_dict)
            jumbled_string = ''
            for k in range(1, i+1):
                jumbled_string += random.choice(global_dict)
            anagram_string = initial_string + ',' + jumbled_string
            return_string.append(anagram_string)
    return '\n'.join(return_string)

if __name__ == "__main__":
    main()
