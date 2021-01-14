import numpy as np


input = [".##.####",
         ".#.....#",
         "#.###.##",
         "#####.##",
         "#...##.#",
         "#######.",
         "##.#####",
         ".##...#."]

hash = bytes("#", 'utf-8')
dot = bytes(".", 'utf-8')


def get_adj_cubes_layer(row, column, cubes):
    adj_cubes = []

    top_most = row == 0
    bottom_most = row == len(cubes) - 1
    left_most = column == 0
    right_most = column == len(cubes[0]) - 1

    # left
    if not left_most:
        adj_cubes.append(cubes[row, column - 1])

    # right
    if not right_most:
        adj_cubes.append(cubes[row, column + 1])

    # top
    if not top_most:
        adj_cubes.append(cubes[row - 1, column])

        if not left_most:
            adj_cubes.append(cubes[row - 1, column - 1])

        if not right_most:
            adj_cubes.append(cubes[row - 1, column + 1])

    # bottom
    if not bottom_most:
        adj_cubes.append(cubes[row + 1, column])

        if not left_most:
            adj_cubes.append(cubes[row + 1, column - 1])

        if not right_most:
            adj_cubes.append(cubes[row + 1, column + 1])

    return adj_cubes


def get_adj_cubes_cube(row, column, layer, cubes):
    adj_cubes = []

    top_most = layer == 0
    bottom_most = layer == cubes.shape[-1] - 1

    # top
    if not top_most:
        adj_cubes.extend(get_adj_cubes_layer(row, column, cubes[..., layer - 1]))
        adj_cubes.append(cubes[row, column, layer - 1])

    # middle
    adj_cubes.extend(get_adj_cubes_layer(row, column, cubes[..., layer]))

    # bottom
    if not bottom_most:
        adj_cubes.extend(get_adj_cubes_layer(row, column, cubes[..., layer + 1]))
        adj_cubes.append(cubes[row, column, layer + 1])

    return adj_cubes


def expand_cube(start, cycles):
    for i in range(len(start)):
        start[i] = list(start[i])

    start = np.asarray(start)
    start_dim = len(start)
    end_dim = start_dim + cycles * 2

    even_dims = end_dim % 2 == 0

    end_z = end_dim
    if even_dims:
        end_z = end_z + 1

    x = int(end_dim / 2) - int(start_dim / 2)
    y = int(end_dim / 2) - int(start_dim / 2)
    z = int(end_dim / 2)

    end = np.chararray((end_dim, end_dim, end_z))
    end[:] = "."
    end[x:x+start_dim, y:y+start_dim, z] = start

    return end


def cycle(cubes, cycles):
    cubes = expand_cube(cubes, cycles)

    shape = cubes.shape
    height = shape[0]
    width = shape[1]
    depth = shape[2]

    curr = cubes.copy()

    for i in range(cycles):
        row = 0
        column = 0
        layer = 0
        prev = curr.copy()

        while layer < depth:
            active_adj_cubes = get_adj_cubes_cube(row, column, layer, prev).count(hash)

            if prev[row, column, layer] == hash:
                if active_adj_cubes < 2 or active_adj_cubes > 3:
                    curr[row, column, layer] = dot

            if prev[row, column, layer] == dot:
                if active_adj_cubes == 3:
                    curr[row, column, layer] = hash

            # move
            column = column + 1

            if column >= width:
                row = row + 1
                column = 0

            if row >= height:
                layer = layer + 1
                row = 0
                column = 0

    print(np.sum(curr.count(hash)))


cycle(input, 6)


# part 2

def get_adj_cubes_hyper(row, column, layer, hyper, cubes):
    adj_cubes = []

    top_most = hyper == 0
    bottom_most = hyper == cubes.shape[-1] - 1

    # top
    if not top_most:
        adj_cubes.extend(get_adj_cubes_cube(row, column, layer, cubes[..., hyper - 1]))
        adj_cubes.append(cubes[row, column, layer, hyper - 1])

    # middle
    adj_cubes.extend(get_adj_cubes_cube(row, column, layer, cubes[..., hyper]))

    # bottom
    if not bottom_most:
        adj_cubes.extend(get_adj_cubes_cube(row, column, layer, cubes[..., hyper + 1]))
        adj_cubes.append(cubes[row, column, layer, hyper + 1])

    return adj_cubes


def expand_hyper_cube(start, cycles):
    for i in range(len(start)):
        start[i] = list(start[i])

    start = np.asarray(start)
    start_dim = len(start)
    end_dim = start_dim + cycles * 2

    even_dims = end_dim % 2 == 0

    end_z = end_dim
    if even_dims:
        end_z = end_z + 1

    x = int(end_dim / 2) - int(start_dim / 2)
    y = int(end_dim / 2) - int(start_dim / 2)
    z = int(end_dim / 2)
    w = int(end_dim / 2)

    end = np.chararray((end_dim, end_dim, end_z, end_z))
    end[:] = "."
    end[x:x+start_dim, y:y+start_dim, z, w] = start

    return end


def cycle(cubes, cycles):
    cubes = expand_hyper_cube(cubes, cycles)

    shape = cubes.shape
    height = shape[0]
    width = shape[1]
    depth = shape[2]
    hyper_depth = shape[3]

    curr = cubes.copy()

    for i in range(cycles):
        row = 0
        column = 0
        layer = 0
        hyper_layer = 0
        prev = curr.copy()

        while hyper_layer < hyper_depth:
            active_adj_cubes = get_adj_cubes_hyper(row, column, layer, hyper_layer, prev).count(hash)

            if prev[row, column, layer, hyper_layer] == hash:
                if active_adj_cubes < 2 or active_adj_cubes > 3:
                    curr[row, column, layer, hyper_layer] = dot

            if prev[row, column, layer, hyper_layer] == dot:
                if active_adj_cubes == 3:
                    curr[row, column, layer, hyper_layer] = hash

            # move
            column = column + 1

            if column >= width:
                row = row + 1
                column = 0

            if row >= height:
                layer = layer + 1
                row = 0
                column = 0

            if layer >= depth:
                hyper_layer = hyper_layer + 1
                row = 0
                column = 0
                layer = 0

    print(np.sum(curr.count(hash)))


# input = [".#.",
# "..#",
# "###"]

cycle(input, 6)
