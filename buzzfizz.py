def buzzfizz(n):
    """Start from 0 up to n.
    For each multiple of 2 print buzz. For each multiple of 3 print fizz."""

    for number in range(n+1):
        if number % 2 == 0:
            print('buzz to {}'.format(number))
        elif number % 3 == 0:
            print('fizz to {}'.format(number))
