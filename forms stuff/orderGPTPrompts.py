f = open("gpt prompts.txt", "r")

ordered = {}
for row in f:
    split = row.split(":")
    ordered[int(split[0][:-5])]  = split[1]

# ordered.sort(key= (lambda x: x[0]))

# print(ordered[46][2:-2])

csvString = ""

for row in ordered:
    csvString += str(row) + "," + ordered[row][2:-2] + "\n"

print(csvString)

"""
targetFile = open("forms question order.txt", "r")


targets = []
for row in targetFile:
    split = row.split(",")

    targets.append(int(split[1][9:]))

for target in targets:
    print(target, ",",ordered[target])
"""