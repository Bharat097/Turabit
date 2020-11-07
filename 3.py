"""
We have a count 35 heads and 94 legs among the chickens and rabbits in a farm.

How many rabbits and how many chickens do we have?
Write a program to get the answer.
"""

heads = int(input("Enter total heads: "))
legs = int(input("Enter total legs: "))

if legs < 2*heads:
    print("Invalid combination provided")

chickens = (4*heads - legs)/2

is_float = chickens % 1
if not is_float:
    rabbits = heads - chickens
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")
else:
    print("Invalid combination provided.")
