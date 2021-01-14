buses = ["19", "x", "x", "x", "x", "x", "x", "x", "x", "41", "x", "x", "x", "37", "x", "x", "x", "x", "x", "821", "x",
         "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "13", "x", "x", "x", "17", "x", "x", "x", "x", "x", "x",
         "x", "x", "x", "x", "x", "29", "x", "463", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
         "x", "x", "x", "x", "x", "x", "x", "x", "x", "23"]

# part 1

time = 1001612
bus_departures = {}

for bus in buses:
    if bus != "x":
        bus_dep = int(bus)
        times = int(time / bus_dep)

        while times * bus_dep < time:
            times = times + 1

        bus_departures[bus_dep] = (times * bus_dep) - time

bus_departures = dict(sorted(bus_departures.items(), key=lambda item: item[1]))

for item in bus_departures.items():
    print(item[0] * item[1])
    break

# part 2

example = ["7", "13", "x", "x", "59", "x", "31", "19"]

from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


bus_idxs_dic = {}
for i in range(0, len(buses)):
    if buses[i] != "x":
        bus_idxs_dic[int(i)] = int(buses[i])

remains = []
divs = []

for bus_idx in bus_idxs_dic.keys():
    remains.append(-(bus_idx) % bus_idxs_dic[bus_idx])
    divs.append(bus_idxs_dic[bus_idx])

print(chinese_remainder(divs, remains))
