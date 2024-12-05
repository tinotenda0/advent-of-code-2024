with open("day1.txt", "r") as file:
    left_list = []
    right_list = []
    listdist = 0

    for line in file:
        temp = line.split()
        left_list.append(temp[0])
        right_list.append(temp[1])

    left_list.sort()
    right_list.sort()

    if len(left_list) == len(right_list):
        for i in range(len(left_list)):
            listdist += abs(int(left_list[i]) - int(right_list[i]))

print(listdist)