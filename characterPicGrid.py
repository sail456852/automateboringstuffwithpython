grid = [
    ['.','.','.','.','.','.'],
    ['.','o','o','.','.','.'],
    ['o','o','o','o','.','.'],
    ['o','o','o','o','o','.'],
    ['.','o','o','o','o','o'],
    ['o','o','o','o','o','.'],
    ['o','o','o','o','.','.'],
    ['.','o','o','.','.','.'],
    ['.','.','.','.','.','.']
]


def transMatrix(grid):
    width = len(grid[0])  # 6
    height = 9 # 9
    for j in range(6):
        print()
        for i in range(9):
            print(grid[i][j], end='')

transMatrix(grid)

        