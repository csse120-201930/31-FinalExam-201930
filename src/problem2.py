"""
Final exam, problem 2.

Authors: Vibha Alangar, Aaron Wilkin, David Mutchler, Dave Fisher, 
         Matt Boutell, Amanda Stouder, their colleagues and 
         PUT_YOUR_NAME_HERE.  May 2019.

"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem2()


###############################################################################
# TODO: 2.  READ the doc-string for the   Point   class defined below.
# It is a simple version of ones that you have seen before.
# After you UNDERSTAND it, ASKING QUESTIONS AS NEEDED,
# change the above _TODO_ to DONE.
###############################################################################


class Point(object):
    """ A Point in 2-d space, with x and y coordinates. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)


def run_test_problem2():
    """ Tests the    problem2    function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2   function:')
    print('--------------------------------------------------')

    format_string = '    problem2( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    seq = [(Point(3, 1), Point(5, 4), Point(15, 99)),
           [Point(0, 0)],
           [],
           (Point(6, -20), Point(-20, -10), Point(3.1, 0))
          ]
    z = 3
    expected = [4, 99, -20, 0]
    print_expected_result_of_test([seq, z], expected,
                                  test_results, format_string)
    actual = problem2(seq, z)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    seq = [(Point(3, 1), Point(5, 4), Point(15, 99)),
           [Point(0, 0)],
           [],
           (Point(6, -20), Point(-20, -10), Point(3.1, 0))
           ]
    z = 2
    expected = [1, 4, 99, -20, 0]
    print_expected_result_of_test([seq, z], expected,
                                  test_results, format_string)
    actual = problem2(seq, z)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    seq = [(Point(3, 1), Point(5, 4), Point(15, 99)),
           [Point(0, 0)],
           [],
           (Point(6, -20), Point(-20, -10), Point(3.1, 0))
           ]
    z = -1
    expected = [1, 4, 99, 0, -20, 0]
    print_expected_result_of_test([seq, z], expected,
                                  test_results, format_string)
    actual = problem2(seq, z)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    seq = [[Point(0, 0)],
           (Point(3, 1), Point(5, 4), Point(-15, 99)),
           [],
           (Point(6, -20), Point(-20, -10), Point(3.1, 0))
           ]
    z = -1
    expected = [0, 1, 4, -20, 0]
    print_expected_result_of_test([seq, z], expected,
                                  test_results, format_string)
    actual = problem2(seq, z)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    seq = [(Point(3, 1), Point(5, 4), Point(15, 99)),
           [Point(0, 0)],
           [],
           (Point(6, -20), Point(-20, -10), Point(3.1, 0))
           ]
    z = 30
    expected = []
    print_expected_result_of_test([seq, z], expected,
                                  test_results, format_string)
    actual = problem2(seq, z)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)

    # Test 6:
    seq = [(Point(3, 1), Point(5, 4), Point(15, 99)),
           [Point(0, 0)],
           [],
           (Point(6, -20), Point(31, -10), Point(3.1, 0))
           ]
    z = 30
    expected = [-10]
    print_expected_result_of_test([seq, z], expected,
                                  test_results, format_string)
    actual = problem2(seq, z)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem2(seq, z):
    """
    What comes in:
      -- A sequence of sub-sequences of Point objects.
      -- An integer z.
    What goes out:  Returns a list that contains the y-values of the
      Point objects in the sub-sequences that meet the following criteria:
        the x-value of that Point object is greater than the argument z.
    Side effects: PRINTS all of the Point objects in the sub-sequences
      whose x-value is greater than the argument z.

    Examples:
      If seq = [(Point(3, 1), Point(5, 4), Point(15, 99)),
                [Point(0, 0)],
                [],
                (Point(6, -20), Point(-20, -10), Point(3.1, 0))
               ]
      and z = 3,
      then    problem2(seq, z)    PRINTS the points:
         Point(5, 4)
         Point(15, 99)
         Point(6, -20)
         Point(3.1, 0)
      and RETURNS the list:
           [4, 99, -20, 0]
    Type hints:
      :type seq: [[Point]]
      :type z:   int
      :rtype: [int]
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
