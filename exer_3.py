def bomberMan(n, grid):
    if n in [0, 1]:
        return grid
    elif n % 2 == 0:
        return ['O' * len(x) for x in grid]
    else:
        grid = [x.replace('O', '2') for x in grid]
        grid = [x.replace('.', '0') for x in grid]
        grid = [list(map(int, list(x))) for x in grid]
        R = len(grid)
        C = len(grid[0])
        t = 1
        while t < 4 + n % 4:
            t += 1
            destroyed = []
            for r in range(R):
                for c in range(C):
                    if grid[r][c] > 0:
                        grid[r][c] -= 1
                    if t % 2 == 0 and grid[r][c] == 0:
                        grid[r][c] = 3
                    elif grid[r][c] == 0:
                        destroyed.append([r, c])
                        if r < R - 1:
                            destroyed.append([r + 1, c])
                        if r > 0:
                            destroyed.append([r - 1, c])
                        if c < C - 1:
                            destroyed.append([r, c + 1])
                        if c > 0:
                            destroyed.append([r, c - 1])
            if destroyed:
                grid = [[2] * len(x) for x in grid]
                for r, c in destroyed:
                    grid[r][c] = 0
        grid = [''.join(list(map(str, x))) for x in grid]
        grid = [x.replace('2', 'O') for x in grid]
        grid = [x.replace('0', '.') for x in grid]
        return grid
