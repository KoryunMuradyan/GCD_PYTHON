#!/usr/bin/python3
import sys
import os
import argparse 

"""
    this function gets argument from command line
"""
def arg_parse_foo():
    linear_parse=argparse.ArgumentParser(description="this script takes a file\
            as an argument from command line in which in ideal shold be an\
            linear equality and creates another file containing the solutionn\
            of the given equality and as a feedback compares the got solution\
            with right solution")
    linear_parse.add_argument('-f', "--file", required = True)
    arguments = linear_parse.parse_args()
    return arguments.file

"""
    this function checks if file is empty
"""
def is_file_empty(file_path):
    # Check if file exist and it is empty
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0

"""
    this function reads content from file and returns it as string
"""
def read_from_file():
    file_path = arg_parse_foo()
    try:
        is_empty = is_file_empty(file_path)
        if is_empty:
            print("File is empty")
            sys.exit()
        else:
            with open(arg_parse_foo()) as my_file:
                equat_str = my_file.read()
            return equat_str
    except IOError :
        print("File of this named exist")
        sys.exit()

"""
    this function compares the result with the one in golden.txt
"""
def test(arg_num_str):
    try:
        with open("golden.txt") as golden_num_f:
            golden_num_str = golden_num_f.read()
        if float(arg_num_str) == float(golden_num_str):
            print(f"{float(arg_num_str)} solution is right!\n")
        else:
            print(f"solution is wroong!!!  should be {golden_num_str} \n")
    except IOError:
        print("Golden file not exist")
        sys.exit()

"""
    this function generates output.txt containing the result wit feedback
"""
def create_output_file(gcd_):
    gcd_str = str(gcd_)
    with open('output.txt', 'w') as output_f:
        output_f.write(gcd_str)

"""
    this function gets a and b numbers as argument and returns gcd
"""
def gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)
    
def main() -> None:
    try:
        input_str = read_from_file()
        arr = input_str.split(" ");
        if len(arr) == 2:
            a = int(arr[0])
            b = int(arr[1])
            gcd_ = gcd(a, b)
            test(gcd_)
            create_output_file(gcd_)
        else:
            print("Quantity does not meet expectations")
    except TypeError:
        print("Problem with the entered arguments")

if __name__ == '__main__':
    main()
