def lemonadeChange(self, bills):
    # keep track of how many fives and tens we are holding
    f, t = 0, 0
    for b in bills:
        # if they are paying with five accept it
        if b == 5:
            f += 1
        elif b == 10:
            # if they are paying with ten and have fives give change, otherwise false
            if f > 0:
                f, t = f - 1, t + 1
            else:
                return False
        elif b == 20:
            # if they are paying with twenty, we can give a ten and five or three fives
            # if we can't give one of those two combos return false
            if f > 0 and t > 0:
                f, t = f - 1, t - 1
            elif f >= 3:
                f -= 3
            else:
                return False
    return True
