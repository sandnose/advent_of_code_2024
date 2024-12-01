from collections import Counter

list1 = []
list2 = []

with open("data/day1.txt", "r") as loc_id:
    for row in loc_id:
        parts = row.strip().split()

        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

# part 1

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)
distances = []

for x, y in zip(sorted_list1, sorted_list2):
    distances.append(abs(x - y))

part1_answer = sum(distances)
print("Answer to part1 is: ", part1_answer)

# part 2

# count1 = Counter(list1)
count2 = Counter(list2)

list2_occurance = {nr: count2[nr] for nr in list1}
similarity_score = [k * v for k, v in list2_occurance.items()]

part2_answer = sum(similarity_score)
print("Answer to part2 is: ", part2_answer)
