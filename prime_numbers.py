def prime_numbers(n) -> bool:
    """
    This function check if a number is whether or not prime.

    Args:
        int: An integer number.

    Returns:
        bool: True if is only divisible by itself and 1.
    """
    for i in range(n+1):

        if i == 0 or i == 1:
            continue

        elif i < n and n % i == 0:
            print('{} is not a prime number. It is multiple of {}.'.format(n, i))
            return False

        elif n % i == 0:
            print('{} is a prime number.'.format(i))
            return True

prime_numbers(991)