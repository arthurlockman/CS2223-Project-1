import string
import random

def main():
    """
    This is the main method for Project 1.
    """
    print(generate_test_data(10, 5))


def generate_test_data(length, number):
    """
    Generate testing data for the anagram algorithm. This method
    generates a large number of test anagram strings for the algorithm
    to be tested against. It is different each time it is run, due
    to its use of the built-in pseudo random number generator.
    :param length: Generate strings in length from 1 to this length.
    :param number: Generate this number of strings at each length.
    :return: A string containing all of the test string data.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    return_string = []
    for i in range(1, length+1):
        for j in range(1, number+1):
            anagram_string = ""
            initial_string = ""
            for k in range(1, i+1):
                initial_string += random.choice(letters)
            string_list = list(initial_string)
            random.shuffle(string_list)
            jumbled_string = ''.join(string_list)
            anagram_string = initial_string + ',' + jumbled_string
            return_string.append(anagram_string)
    return '\n'.join(return_string)

if __name__ == "__main__":
    main()
