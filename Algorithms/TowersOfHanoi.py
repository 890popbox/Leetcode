# n == number of towers, a,b,c are the tower names and locations
def hanoi(n=3, a='A', b='B', c='C'):
    # Eventually all cases will meet zero
    if n == 0:
        return
    else:
        hanoi(n - 1, a, c, b)
        print('{0} to {1}'.format(a, c))
        hanoi(n - 1, b, a, c)


# Solves the hanoi tower puzzle for given number of towers as input
# The first case A goes to C which is the end, then after that c and b swap so the next A goes to B
# A and B also have to swap because C must go back to B so the next A can go to C.
hanoi(3)
