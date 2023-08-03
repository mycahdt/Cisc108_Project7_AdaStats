#Project 7
"""
# Ada's Stats Module
A collection of functions for doing some basic statistics on your data.

# When You Are Done
When you pass all tests, remember to clean and document your code.
Be sure to unit test and document your functions.
"""

from cisc108 import assert_equal
import math

# 1) count
def count(numbers: [int]) -> int:
    '''
    Consumes a list of numbers and produces an integer
    that represents the length of the list.
    
    Args:
        numbers ([int]): The list of numbers which are integers
    Returns:
        int: The length of the 'numbers' list 
    '''
    count = 0
    for num in numbers:
        count = count + 1
    return count

assert_equal(count([1, 2]), 2)
assert_equal(count([2, 3, 9]), 3)
assert_equal(count([1, 2, 3, 3]), 4)

# 2) summate
def summate(nums: [int]) -> int:
    '''
    Consumes a list of numbers and produces an integer
    that represents the total sum of all of the numbers
    in the list.
    
    Args:
        nums ([int]): The list of numbers which are integers
    Returns:
        int: The total sum of all the numbers
    '''
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

assert_equal(summate([1, 2, 3, 4, 5]), 15)
assert_equal(summate([505, 100, 650, 140, 820]), 2215)
assert_equal(summate([100, 200, 300, 900]), 1500)

# 3) mean
def mean(nums: [int]) -> float:
    '''
    Consumes a list of numbers and produces a float
    value that represents the mean of the list.
    
    Args:
        nums ([int]): The list of numbers which are integers
    Returns:
        float: The mean value of the list
    '''
    if not nums:
        return None
    else:
        return summate(nums) / count(nums)
    
assert_equal(mean([1, 2, 3, 4, 5]), 3.0)
assert_equal(mean([22, 54, 81, 99, 1, 43, 6]), 43.71428571)
assert_equal(mean([31, 50]), 40.5)

# 4) square
def square(nums: [int]) -> [int]:
    '''
    Consumes a list of numbers and produces a new list
    where each number from the list is squared.
    
    Args:
        nums ([int]): The list of number which are integers
    Returns:
        [int]: The list of numbers where each element is squared
    '''
    squaredList = []
    for num in nums:
        squaredList.append(num**2)
    return squaredList

assert_equal(square([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])
assert_equal(square([21, 10, 88, 32]), [441, 100, 7744, 1024])
assert_equal(square([45, 999]), [2025, 998001])



# 5) diff
def diff(nums: [int], a_num: int) -> [int]:
    '''
    Consumes a list of numbers and a number, and produces
    a new list where each number from the list is subtracted
    by the given number.
    
    Args:
        nums ([int]): The list of numbers which are integers
        a_num (int): The given number used to subtract from
            each element in the list
    Returns:
        [int]: The list of integers where each element of the
            old list is subtracted by the given number
    '''
    diffList = []
    for num in nums:
        diffList.append(num - a_num)
    return diffList

assert_equal(diff([1, 2, 3, 4, 5], 1), [0, 1, 2, 3, 4])
assert_equal(diff([38, 74, 59, 11, 85, 67], 3), [35, 71, 56, 8, 82, 64])
assert_equal(diff([200, 1000, 300], 100), [100, 900, 200])

# 6) standard_deviation
def standard_deviation(nums: [int]) -> float:
    '''
    Consumes a list of numbers and produces a float
    that represents the standard deviation. This is done
    by subtracting the mean from each value in the list,
    squaring each value in the list, find the sum of the list,
    dividing by the number of elements minus 1, and then find
    the square root.
    
    Args:
        nums ([int]): The list of numbers which are integers
    Returns:
        float: The float value that represents the standard
            deviation of the list.
        None: is returned when list length is less than 2
    '''
    if count(nums) < 2:
        return None
    else:
        value = math.sqrt(summate(square(diff(nums,mean(nums))))/(count(nums)-1))
    return value
            
assert_equal(standard_deviation([1, 2, 3, 4, 5]), 1.58113883)
assert_equal(standard_deviation([94, 42, 26, 67, 71, 10, 3]), 33.959359464485)
assert_equal(standard_deviation([11, 8, 39]), 17.097758137643)
assert_equal(standard_deviation([]), None)

# 7) main function
# The following code can be used to try out your functions.
# Comment them out now.
# Uncomment each line as you implement the functions to try them out.
def main(question, results):
    '''
    Consumes a string which represents the question that was
    asked to the participants, and consumes a list of integers
    which represents the results or data collected from the question.
    Produces printed values that show the number of participants,
    the question, the sum of the data, the mean of the data, and
    the standard deviation of the data.
    
    Args:
        question (str): The question that was asked to the participants
        results ([int]): The list of numbers which data collected that
            respresents the answers given by the participants. 
    '''
    print("We asked", count(results), "people the following question.")
    print(' "'+question+'"')
    print("Here are the statistical results:")
    print("\tSum:", summate(results))
    print("\tMean:", mean(results))
    print("\tStandard Deviation:", standard_deviation(results))
    
# 8) Question and Results
# Comment these out until you are ready to define them
QUESTION = "How many reusable face masks do you own?"
ANSWERS = [3, 5, 3, 5, 8, 20, 7, 3, 7, 3, 2, 0, 10, 3, 4, 2, 10, 5, 7, 10, 3, 2, 6]
ANALYSIS = 'We asked 23 people the following question. "How many reusable face masks do you own?" Here are the statistical results: Sum: 128 Mean: 5.565217391304348 Standard Deviation: 4.219285667207423'



main(QUESTION, ANSWERS)