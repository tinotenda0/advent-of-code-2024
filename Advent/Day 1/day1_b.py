from collections import Counter

file = open("day1.txt", "r")
left_list = []
right_list = []

for line in file:
    temp = line.split()
    left_list.append(int(temp[0]))
    right_list.append(int(temp[1]))


right_counts = Counter(right_list)


similarity_score = sum(num * right_counts[num] for num in left_list)

print("Similarity Score:", similarity_score)
