"""
Final exam, problem 3.

Authors: Vibha Alangar, Aaron Wilkin, David Mutchler, Dave Fisher, 
         Matt Boutell, Amanda Stouder, their colleagues and 
         PUT_YOUR_NAME_HERE.  May 2019.

"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import math
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


###############################################################################
# TODO: 2.  READ the doc-strings for the   is_prime   and    sum_of_digits
# functions defined below.  They are the same as you have seen before.
# After you UNDERSTAND the doc-strings(JUST the doc-strings, NOT the code),
# ASKING QUESTIONS AS NEEDED, change the above _TODO_ to DONE.
###############################################################################
def is_prime(n):
    """
    What comes in:   An integer.
    What goes out:  Returns True if the given integer is prime.
                    Returns False if the given integer is NOT prime.
    Side effects: None.
    Examples:
      This function returns True or False, depending on whether
      the given integer is prime or not.  Since the smallest prime is 2,
      this function returns False on all integers < 2.
      It returns True on 2, 3, 5, 7, and other primes.
    Note: The algorithm used here is simple and clear but slow.
    Type hints:
      :type n: int
    """
    if n < 2:
        return False

    for k in range(2, int(math.sqrt(n) + 0.1) + 1):
        if n % k == 0:
            return False

    return True
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no TO DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  The sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TO DO in it.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the other problems.
    #
    # Ask for help if you are unsure what it means to CALL a function.
    # The ONLY part of this function that you need to understand is
    # the doc-string above.  Treat this function as a black box.
    # -------------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def run_test_problem3():
    """ Tests the  problem3   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3   function:')
    print('--------------------------------------------------')

    format_string = '    problem3( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    x = 95
    expected = 101
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem3(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    x = 101
    expected = 101
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem3(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    x = 102
    expected = 113
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem3(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    x = 14
    expected = 23
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem3(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    x = 9000
    expected = 9011
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem3(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    x = 10000
    expected = 10037
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem3(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    x = 50051
    expected = 50051
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem3(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    x = 51353
    expected = 51407
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem3(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem3(n):
    """
    What comes in:
      -- A positive integer n
    What goes out:  Returns the smallest number bigger than or equal to n
       that is prime and whose sum of digits is prime.
    Side effects: None.

    Examples:
     problem3(95) would return 101, since:
           95 is NOT prime
           96 is NOT prime
           97 IS prime but its sum of digits is 16, which is NOT prime
           98 is NOT prime
           99 is NOT prime
           100 is NOT prime
           101 IS prime and also its sum of digits is 2, which IS prime
    Type hints:
      :type n: int
      :rtype: int
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results,
                                                 format_string)


def print_actual_result_of_test(expected, actual, test_results):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
