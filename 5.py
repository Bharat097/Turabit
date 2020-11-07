"""Remove duplicate integers."""

input_list = [1, 2, 55, 1, 3, 2, 34, 55]

ans_dict = {}

for each in input_list:
    if not ans_dict.get(each):
        ans_dict[each] = 1

print(list(ans_dict.keys()))
