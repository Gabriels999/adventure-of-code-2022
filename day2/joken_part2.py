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


def rounds(r):
    r1 = Round(r[0], r[-1])
    if r[-1] == 'Z':
        shape_points = r1.game()
        return 6 + shape_points
    elif r[-1] == 'Y':
        shape_points = r1.game()
        return 3 + shape_points
    else:
        shape_points = r1.game()
        return 0 + shape_points


class Round:
    def __init__(self, enemy, defense):
        self.enemy = enemy
        self.defense = defense

    def game(self):
        if (self.enemy == 'A' and self.defense == 'Y') or (self.enemy == 'B' and self.defense == 'X') or (self.enemy == 'C' and self.defense == 'Z'):
            return 1
        elif (self.enemy == 'B' and self.defense == 'Y') or (self.enemy == 'C' and self.defense == 'X') or (self.enemy == 'A' and self.defense == 'Z'):
            return 2
        else:
            return 3


game('./day2/sample.txt')
