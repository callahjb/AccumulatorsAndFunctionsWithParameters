"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Joseph Callahan.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_powers()
    run_test_sum_powers_in_range()


def run_test_sum_powers():
    """ Tests the   sum_powers   function. """
    # ------------------------------------------------------------------
    # done: 2. Implement this function.
    #   It TESTS the  sum_powers  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 3.80826
    answer = sum_powers(5,-0.3)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = 144.45655
    answer = sum_powers(100,0.1)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    # Test 3:
    expected = 28
    answer = sum_powers(7,1)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)


def sum_powers(n, p):
    """
    What comes in:  A non-negative integer n
                    and a number p.
    What goes out:  The sum   1**p + 2**p + 3**p + ... + n**p
       for the given numbers n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:   None.
    Examples:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655
    """
    # ------------------------------------------------------------------
    # done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    answer = 0
    for k in range(n+1):
        if k > 0:
            answer = answer + k**p

    answer = answer
    return answer


def run_test_sum_powers_in_range():
    """ Tests the   sum_powers_in_range   function. """
    # ------------------------------------------------------------------
    # TODO: 4. Implement this function.
    #   It TESTS the  sum_powers_in_range  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers_in_range   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 142.384776
    answer = sum_powers_in_range(3, 100, 0.1)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = 208.08186
    answer = sum_powers_in_range(3,100,0.2)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    # Test 3:
    expected = 27
    answer = sum_powers_in_range(2,7,1)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)


def sum_powers_in_range(m, n, p):
    """
    What comes in:  Non-negative integers m and n, with n >= m,
                    and a number p.
    What goes out:  the sum
           m**p + (m+1)**p + (m+2)**p + ... + n**p
       for the given numbers m, n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:  None.
    Example:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776
    """
    # ------------------------------------------------------------------
    # done: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers_in_range  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    answer = 0
    sum = 0
    for k in range(n+1):
        if k > 0 and n >= (m+sum):
            answer = answer + ((m+sum)**p)
            sum = sum + 1

    answer = answer
    return answer


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
