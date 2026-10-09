my_list = [1, "Python", 2, 3, 5, "Java", "C"]

# Find max number
max_num = max(x for x in my_list if isinstance(x, (int, float)))

# Split BEFORE max_num
i = my_list.index(max_num)

part1 = my_list[:i]
part2 = my_list[i:]

print(part1, part2)
# Output: [1, 'Python', 2, 3] [5, 'Java', 'C']