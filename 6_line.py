import itertools

list1 = (1)
count = 0
for i in itertools.permutations([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
    if 1 + i[1] + i[4] + i[6] == 26 and 1 + i[2] + i[5] + i[9] == 26 and i[6] + i[7] + i[8] + i[9] == 26 and i[0] + i[
        4] + i[7] + i[10] == 26 and \
            i[0] + i[1] + i[2] + i[3] == 26 and i[3] + i[5] + i[8] + i[10] == 26:
        print(i)
        count += 1
print(count)
