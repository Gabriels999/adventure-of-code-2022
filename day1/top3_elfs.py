from elfs_calories import calories


def top3(elfs_list):
    target = elfs_list[:3]
    print(sum(target))
    return


elfs = calories('./day1/sample.txt')
top3(elfs)
