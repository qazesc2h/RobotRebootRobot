import heapq

color = {'R': 0, 'Y': 1, 'G': 2, 'B': 3}


def cell(grid, robots, c):
    return grid[robots[c][1]][robots[c][0]]


def move(grid, robots, c, d):
    ret = [item[:] for item in robots]

    if d == 0b1000:
        while not (cell(grid, ret, c) & d):
            if [ret[c][0], ret[c][1] - 1] in ret:
                break
            ret[c][1] -= 1
    elif d == 0b0100:
        while not (cell(grid, ret, c) & d):
            if [ret[c][0], ret[c][1] + 1] in ret:
                break
            ret[c][1] += 1
    elif d == 0b0010:
        while not (cell(grid, ret, c) & d):
            if [ret[c][0] - 1, ret[c][1]] in ret:
                break
            ret[c][0] -= 1
    elif d == 0b0001:
        while not (cell(grid, ret, c) & d):
            if [ret[c][0] + 1, ret[c][1]] in ret:
                break
            ret[c][0] += 1

    return ret


# 언제든 정지 가능하다 + 다른 로봇이 없다는 가정하에 이동할 수 있는 최단거리
def heuristic(grid, robots, x, y, c):
    ret = 0
    if robots[c][0] != x:
        ret += 1
    if robots[c][1] != y:
        ret += 1

    cell = grid[y][x]

    if robots[c][1] == y:
        if (cell & 0b0010) and robots[c][0] < x:
            ret = 3
        elif (cell & 0b0001) and robots[c][0] > x:
            ret = 3
    elif (cell & 0b1000) and robots[c][1] < y:
        if robots[c][0] == x:
            ret = 3
        elif (cell & 0b0010) and robots[c][0] < x:
            ret = 3
        elif (cell & 0b0001) and robots[c][0] > x:
            ret = 3
    elif (cell & 0b0100) and robots[c][1] > y:
        if robots[c][0] == x:
            ret = 3
        elif (cell & 0b0010) and robots[c][0] < x:
            ret = 3
        elif (cell & 0b0001) and robots[c][0] > x:
            ret = 3

    return ret


def a_star(grid, robots, x, y, c):
    search = 0
    heap = []

    for i in range(4):
        for j in range(4):
            new_robots = move(grid, robots, i, 1 << j)
            if robots != new_robots:
                element = (1 + heuristic(grid, new_robots, x, y, c),
                           new_robots, [(i, j)])
                heapq.heappush(heap, element)

    while search <= 5e6:
        search += 1
        element = heapq.heappop(heap)

        if element[1][c] == [x, y]:
            return element[2]

        for i in range(4):
            for j in range(4):
                if element[2][-1][0] == i:
                    if element[2][-1][1] + j == 1 or element[2][-1][1] + j == 5:
                        continue
                new_robots = move(grid, element[1], i, 1 << j)
                if element[1] != new_robots:
                    new_element = (1 + len(element[2]) +
                                   heuristic(grid, new_robots, x, y, c),
                                   new_robots, element[2] + [(i, j)])
                    heapq.heappush(heap, new_element)

    return []
