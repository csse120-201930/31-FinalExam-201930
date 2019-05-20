"""
Final exam, problem 4.

Authors: Vibha Alangar, Aaron Wilkin, David Mutchler, Dave Fisher, 
         Matt Boutell, Amanda Stouder, their colleagues and 
         PUT_YOUR_NAME_HERE.  May 2019.

"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_shape()


def run_test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('There is no automatic testing for this one; just compare it'
          'to the expected output given in the comments:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: n=5')
    shape(5)

    print()
    print('Test 2 of shape: n=3')
    shape(3)

    print()
    print('Test 3 of shape: n=7')
    shape(7)


def shape(n):
    ####################################################################
    # IMPORTANT: In your final solution for this problem,
    #   you must NOT use string multiplication.
    ####################################################################
    """
    Prints a shape with numbers on the left side of the shape,
    other numbers on the right side of the shape,
    and stars in the middle, per the pattern in the examples below.

    You do NOT need to deal with any test cases where n > 9.

    It looks like this example for n=5:
*66666+++++54321
**5555++++4321
***444+++321
****33++21
*****2+1

    And this one for n=3:
*444+++321
**33++21
***2+1


    And this one for n=7:
*8888888+++++++7654321
**777777++++++654321
***66666+++++54321
****5555++++4321
*****444+++321
******33++21
*******2+1
    :type n: int
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    ####################################################################
    # IMPORTANT: In your final solution for this problem,
    #   you must NOT use string multiplication.
    ####################################################################


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
