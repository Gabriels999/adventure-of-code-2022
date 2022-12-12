def calories(path):
    with open(path) as f:
        lines = f.readlines()
    tx = ''.join(lines)
    elfs_list = []
    elf = 0
    for item in tx.splitlines():
        if item != '':
            elf += int(item)
        else:
            elfs_list.append(elf)
            elf = 0
    # print(max(elfs_list)) printa o que leva mais calorias
    elfs_list = sorted(elfs_list, reverse=True)
    return elfs_list


calories('./day1/sample.txt')
