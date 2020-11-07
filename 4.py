"""Word frequency counter."""

input_list = [
    "python",
    "python3",
    "user1",
    "assignment",
    "user",
    "user1",
    "python",
    "User1"
    ]

ans_dict = {}

for each in input_list:
    ans_dict[each] = ans_dict.get(each, 0) + 1

print(ans_dict)
