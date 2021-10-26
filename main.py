import a_star


color_c = ("R", "Y", "G", "B")
dir_c = ("R", "L", "D", "U")


def out_of_range(n, x):
    return (x < 0 or x >= n)


def solve(n):
    grid = [[0] * n] * n
    robots = []

    for i in range(n):
        grid[0][i] |= 0b1000
        grid[-1][i] |= 0b0100
        grid[i][0] |= 0b0010
        grid[i][-1] |= 0b0001

    with open('grid.txt', 'rt', encoding='utf-8') as f:
        for line in f:
            pos = line.split(' ')
            if len(pos) >= 3:
                y = int(pos[0]) - 1
                x = int(pos[1]) - 1
                z = int(pos[2], 2)
                grid[y][x] |= z

                if y > 0 and z & 0b1000:
                    grid[y-1][x] |= 0b0100
                if y < n-1 and z & 0b0100:
                    grid[y+1][x] |= 0b1000
                if x < 0 and z & 0b0010:
                    grid[y][x-1] |= 0b0001
                if x < n-1 and z & 0b0001:
                    grid[y][x+1] |= 0b0010

    with open('robots.txt', 'rt', encoding='utf-8') as f:
        for line in f:
            pos = line.split(' ')
            x = int(pos[0]) - 1
            y = int(pos[1]) - 1
            robots.append([x, y])

    print("Refresh the position of robots after solving problem : Y or N")

    refresh = None
    while refresh is None:
        answer = input().upper()
        if answer == 'Y':
            refresh = True
        elif answer == 'N':
            refresh = False
        else:
            print('Y or N : ', end='')

    while True:
        print('Input the goal. (x y color = RYGB)')
        goal = input().split(' ')

        if len(goal) < 3:
            break

        x = int(goal[0]) - 1
        y = int(goal[1]) - 1
        c = goal[2].upper()

        if out_of_range(n, x) or out_of_range(n, y) or c not in 'RYGB':
            break

        answer = a_star.a_star(grid, robots, x, y, a_star.color[c])
        if answer:
            print(len(answer))
            for i in answer:
                print(color_c[i[0]], dir_c[i[1]])
            if refresh:
                for i in answer:
                    robots = a_star.move(grid, robots, i[0], 1 << i[1])
        else:
            print("Failed to find answer...")


if __name__ == '__main__':
    # size = input('Input the size of grid : ')
    size = 16
    solve(int(size))
