
Algorithms Project 1
===

The purpose of this project was to test the efficiency of two different algorithms which determine if two input strings are anagrams of each other. One algorithm is a brute force algorithm, and the other is a better algorithm designed and developed by Arthur. This document describes how to run the project code and use it to validate itself using the built-in tests and test user-input strings.

*This document is written assuming this code is being run on the WPI CCC machines. It may vary on other computers with different Python installations, but the procedure should be largely the same.* 

## Project Setup

This project does not require any non-standard libraries to run. It can be run on CCC by typing

```
-bash-4.1$ python3.4 ./project1.py
```

Sometimes this command will fail, and drop into a python prompt instead of running the program (this is due to a configuration error on the CCC servers). To bypass this and run the program, follow these steps:

```
-bash-4.1$ python3.4
Python 3.4.1 (default, Aug 28 2014, 13:51:39)
[GCC 4.7.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import project1
>>> project1.main()
```

By importing and running the project in the python interpreter, the configuration issue can be bypassed and the program can be run.

## Project Usage

Once the project is running, the code will present a menu which will allow the user to perform its main functions.

```
Welcome to the anagram algorithm tester!
Please choose an option:
1: Run both algorithms with input strings
2: Generate sample data, and save it to a file
3: Run both algorithms with sample data file, and output the time results
---
9: Exit the program
 >>
```

The first option will allow the user to run an arbitrary pair of strings against both the brute force and better algorithm to determine if they are anagrams of each other. It will prompt the user to type in these strings, and then give the results. 

```
Welcome to the anagram algorithm tester!
Please choose an option:
1: Run both algorithms with input strings
2: Generate sample data, and save it to a file
3: Run both algorithms with sample data file, and output the time results
---
9: Exit the program
 >>  1
Input one string, and then another. This function will determine if the second string is an anagram of the first.
Input the first string
 >>  johnsmith
Input the second string
 >>  htismhonj
The better algorithm determined that the string htismhonj is an anagram of johnsmith in 0.00010800361633300781 seconds  (44 computation loops).
The brute force algorithm determined that the string htismhonj is an anagram of johnsmith in 0.06892275810241699 seconds  (114934 computation loops).
Press the ANY key to return to the main menu
```

The second option will allow the user to generate a data file that can be used to test both algorithms against large sets of testing data. A sample of using this is shown below.

```
Welcome to the anagram algorithm tester!
Please choose an option:
1: Run both algorithms with input strings
2: Generate sample data, and save it to a file
3: Run both algorithms with sample data file, and output the time results
---
9: Exit the program
 >>  2
This selection will generate and save testing data to a file.
Enter the filename you wish to save testing data to
 >>  test.txt
Enter the maximum length of string to generate in the testing data
 >>  5
Enter the number of entries to generate with each length
 >>  1
Enter 1 if you would like to generate tests that are anagrams, 2 if you would like tests that are not anagrams, or 3 if you would like both
 >>  3
Success! File test.txt written with testing data.
Press the ANY key to return to the main menu
```

The above example will generate a set of strings that are both anagrams and not anagrams with lengths from 1 to 5, and will generate 1 string at each increment.

The third menu option allows the user to run the algorithms with the generated data, as shown below.

```
Welcome to the anagram algorithm tester!
Please choose an option:
1: Run both algorithms with input strings
2: Generate sample data, and save it to a file
3: Run both algorithms with sample data file, and output the time results
---
9: Exit the program
 >>  3
This selection will read a testing data file, and run both algorithms on it.
Enter the filename of the testing file
 >>  test.txt
File loaded.
Enter the name of the test results file (CSV)
 >>  test.csv
Enter 1 to run the brute force algorithm, 2 to run the better algorithm, and 3 to run both
 >>  3
The brute force algorithm determined that the string a is an anagram of a in 3.790855407714844e-05 seconds  (1 computation loops).
The better algorithm determined that the string a is an anagram of a in 6.437301635742188e-05 seconds  (28 computation loops).
The brute force algorithm determined that the string ra is an anagram of ar in 5.245208740234375e-06 seconds  (2 computation loops).
The better algorithm determined that the string ra is an anagram of ar in 1.2636184692382812e-05 seconds  (30 computation loops).
The brute force algorithm determined that the string ldt is an anagram of tld in 5.245208740234375e-06 seconds  (4 computation loops).
The better algorithm determined that the string ldt is an anagram of tld in 1.3113021850585938e-05 seconds  (32 computation loops).
The brute force algorithm determined that the string ufpp is an anagram of pupf in 8.821487426757812e-06 seconds  (11 computation loops).
The better algorithm determined that the string ufpp is an anagram of pupf in 1.33514404296875e-05 seconds  (34 computation loops).
The brute force algorithm determined that the string uajhs is an anagram of aushj in 1.7404556274414062e-05 seconds  (30 computation loops).
The better algorithm determined that the string uajhs is an anagram of aushj in 1.3113021850585938e-05 seconds  (36 computation loops).
The brute force algorithm determined that the string v is an anagram of v in 3.5762786865234375e-06 seconds  (1 computation loops).
The better algorithm determined that the string v is an anagram of v in 1.1682510375976562e-05 seconds  (28 computation loops).
The brute force algorithm determined that the string td is not an anagram of dk in 4.0531158447265625e-06 seconds  (2 computation loops).
The better algorithm determined that the string td is not an anagram of dk in 9.5367431640625e-06 seconds  (15 computation loops).
The brute force algorithm determined that the string xts is not an anagram of mxf in 5.9604644775390625e-06 seconds  (6 computation loops).
The better algorithm determined that the string xts is not an anagram of mxf in 9.5367431640625e-06 seconds  (12 computation loops).
The brute force algorithm determined that the string ydqr is not an anagram of uang in 1.3589859008789062e-05 seconds  (24 computation loops).
The better algorithm determined that the string ydqr is not an anagram of uang in 8.344650268554688e-06 seconds  (9 computation loops).
The brute force algorithm determined that the string xiypd is not an anagram of dqzne in 5.984306335449219e-05 seconds  (120 computation loops).
The better algorithm determined that the string xiypd is not an anagram of dqzne in 9.298324584960938e-06 seconds  (15 computation loops).
Press the ANY key to return to the main menu
```

This example loaded the testing data and ran it against both algorithms, then ouput the resulting data into the file *test.csv*. This data is graphable in Excel, and contains the runtime of each algorithm for the strings, the strings themselves, the string length, the result of the computation, and the number of computations performed for the strings.

The final menu option (9) will exit the program.