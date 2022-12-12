def rucksack(path):
    with open(path) as f:
        items = f.readlines()
    items = ''.join(items).splitlines()
    groups_list = identify_groups(items)
    priorities_total = 0
    for g in groups_list:
        group = Group(g)
        priorities_total += group.common_to_all()
    print(priorities_total)
    total = 0
    for i in items:
        item = Rucksack(i)
        total += item.count_priorities()
    return total


def identify_groups(items_list):
    i = 1
    groups_list = []
    while i <= len(items_list):
        if i % 3 == 0:
            groups_list.append(
                (items_list[i-3], items_list[i-2], items_list[i-1]))
        i += 1
    return groups_list


class Rucksack:
    def __init__(self, code):
        self.full_code = code

    def split_items(self):
        half = int(len(self.full_code)/2)
        self.item1, self.item2 = self.full_code[:half], self.full_code[half:]
        return (self.item1, self.item2)

    def shared_items(self):
        share_items = []
        items = self.split_items()
        for i in range(len(items[0])):
            if self.item1[i] in self.item2:
                if self.item1[i] not in share_items:
                    share_items.append(self.item1[i])
        return share_items

    def count_priorities(self):
        priorities = self.shared_items()
        return self.priorities_math(priorities)

    def priorities_math(self, priorities):
        result = 0
        for i in priorities:
            if i.islower():
                result += ord(i)-96
            else:
                result += ord(i)-65+27
        return result


class Group(Rucksack):
    def __init__(self, rucks):
        self.first = rucks[0]
        self.second = rucks[1]
        self.third = rucks[2]

    def __str__(self):
        return self.first + self.second + self.third

    def common_to_all(self):
        target = [self.first, self.second, self.third]
        share_items = []
        size = [len(self.first), len(self.second), len(self.third)]
        t = size.index(max(size))
        i = 0
        while i < max(size):
            if (target[t][i] in self.first) and (target[t][i] in self.second) and (target[t][i] in self.third):
                if target[t][i] not in share_items:
                    share_items.append(target[t][i])
            i += 1

        return self.priorities_math(share_items)


print(rucksack('./day3/sample.txt'))
