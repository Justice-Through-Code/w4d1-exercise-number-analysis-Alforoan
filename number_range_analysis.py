# number_range_analysis.py

"""
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

"""
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION


def calculate_sum(start, end):
    # initialize a variable called sum to store the sum of the numbers within the range and set it to 0
    # start with a for loop boiler plate
    # for each number starting from the 'start', add it to sum
    # print sum

    sum = 0
    for i in range(start, end + 1):
        sum = sum + i
    return sum

    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.


def find_smallest_number(start, end):
    # initialize a variable called smallest_number and set it to 10000
    # start with a for loop boiler plate
    # for each number starting from the 'start', compare it to the smallest_number and if it's smaller set smallest_number to that value
    # print smallest_number
    smallest_number = 10000
    for i in range(start, end + 1):
        if i < smallest_number:
            smallest_number = i
    return smallest_number

    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.


def find_largest_number(start, end):
    # initialize a variable called largest_number and set it to -1000
    # start with a for loop boiler plate
    # for each number starting from the 'start', compare it to the larget_number and if it's smaller set largest_number to that value
    # print largest_number
    largest_number = -1000
    for i in range(start, end + 1):
        if i > largest_number:
            largest_number = i
    return largest_number
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.


def count_even_numbers(start, end):
    # initialize a variable called counter and set it to 0
    # start with a for loop boiler plate
    # for each number starting from the 'start', determine if it's evenly divisible by 2, and if it is, increase the counter
    # print counter

    counter = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            counter += 1

    return counter
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.


count_even_numbers(0, 5)


def count_odd_numbers(start, end):
    # initialize a variable called counter and set it to 0
    # start with a for loop boiler plate
    # for each number starting from the 'start', determine if it's not evenly divisible by 2, and if it is not, increase the counter
    # print counter

    counter = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            counter += 1
    return counter
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.
