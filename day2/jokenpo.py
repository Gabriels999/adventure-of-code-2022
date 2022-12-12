def game(path):
    with open(path) as f:
        l = f.readlines()
    l = ''.join(l).splitlines()
    i = 0
    points = 0
    while i < len(l):
        round_points = rounds(l[i])
        points += round_points
        i += 1
    print(points)
    return points


def shape_check(string):
    if string == 'X':
        return 1
    elif string == 'Y':
        return 2
    else:
        return 3


def rounds(r):
    r1 = Round(r[0], r[-1])
    if r1.game() == 'w':
        shape_points = shape_check(r1.defense)
        return 6 + shape_points
    elif r1.game() == 't':
        shape_points = shape_check(r1.defense)
        return 3 + shape_points
    else:
        shape_points = shape_check(r1.defense)
        return 0 + shape_points


class Round:
    def __init__(self, enemy, defense):
        self.enemy = enemy
        self.defense = defense

    def game(self):
        if (self.enemy == 'A' and self.defense == 'Y') or (self.enemy == 'B' and self.defense == 'Z') or (self.enemy == 'C' and self.defense == 'X'):
            return 'w'
        elif (self.enemy == 'A' and self.defense == 'X') or (self.enemy == 'B' and self.defense == 'Y') or (self.enemy == 'C' and self.defense == 'Z'):
            return 't'
        else:
            return 'l'


game('./day2/sample.txt')
