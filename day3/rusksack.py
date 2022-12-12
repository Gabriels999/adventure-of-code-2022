def rucksack(path):
    with open(path) as f:
        items = f.readlines()
    items = ''.join(items).splitlines()
    total = 0
    for i in items:
        item = Rucksack(i)
        total += item.count_priorities()
    return total


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
        result = 0
        for i in priorities:
            if i.islower():
                result += ord(i)-96
            else:
                result += ord(i)-65+27
        return result


print(rucksack('./day3/sample.txt'))
