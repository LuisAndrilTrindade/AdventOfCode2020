import numpy as np

input = [104, 83, 142, 123, 87, 48, 102, 159, 122, 69, 127, 151, 147, 64, 152, 90, 117, 132, 63, 109, 27, 47, 7, 52, 59,
         11, 161, 12, 148, 155, 129, 10, 135, 17, 153, 96, 3, 93, 82, 55, 34, 65, 89, 126, 19, 72, 20, 38, 103, 146, 14,
         105, 53, 77, 120, 39, 46, 24, 139, 95, 140, 33, 21, 84, 56, 1, 32, 31, 28, 4, 73, 128, 49, 18, 62, 81, 66, 121,
         54, 160, 158, 138, 94, 43, 2, 114, 111, 110, 78, 13, 99, 108, 141, 40, 25, 154, 26, 35, 88, 76, 145]


# part 1

max = np.max(input) + 3
input.append(max)
input.append(0)
input.sort()

dif_1 = 0
dif_3 = 0

for i in range(len(input) - 1):
    dif = input[i + 1] - input[i]
    if dif == 1:
        dif_1 = dif_1 + 1
    if dif == 3:
        dif_3 = dif_3 + 1

print(dif_1 * dif_3)


# part 2

input.remove(0)
poss = {0: 1, }

for adapt in input:
    poss[adapt] = 0
    if adapt - 1 in poss:
        poss[adapt] = poss[adapt] + poss[adapt - 1]
    if adapt - 2 in poss:
        poss[adapt] = poss[adapt] + poss[adapt - 2]
    if adapt - 3 in poss:
        poss[adapt] = poss[adapt] + poss[adapt - 3]

print(poss[max])
