#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 28, 2022
# This program find the max value in an array
# of random integers


import random


def calculate_max_value(rand_array):
    # This function calculates the max
    max_value = 1
    # Loop that calculates the max value
    for counter in range(9):
        if max_value < rand_array[counter]:
            max_value = rand_array[counter]
    # Return the max value
    return max_value


def main():
    # This function creates the array and
    # fills the array
    array = []
    for counter in range(10):
        num = random.randint(0, 100)

        array.append(num)
        print("{} added in position {}.".format(num, counter))
    max_v = calculate_max_value(array)
    print(array)
    print(max_v)


if __name__ == "__main__":
    main()
