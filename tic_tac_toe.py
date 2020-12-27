grid = [[' '] * 3 for i in range(3)]
count = 0  # if even - X, odd - O


def change_rows(matrix):
    rows = [row for row in grid] + [[matrix[i][j] for i in range(3)] for j in range(3)] \
           + [[matrix[i][i] for i in range(3)]] + [[matrix[i][2 - i] for i in range(3)]]
    return rows


def print_grid():
    print('-' * 9)
    for i in range(3):
        print('|', *grid[i], '|')
    print('-' * 9)


def make_move():
    global count
    coordinates = input('Enter the coordinates: ').split()
    if not coordinates[0].isdigit() or not coordinates[1].isdigit():
        print('You should enter numbers!')
        make_move()
        return
    x = int(coordinates[0]) - 1
    y = int(coordinates[1]) - 1
    if x > 2 or y > 2:
        print('Coordinates should be from 1 to 3!')
        make_move()
        return
    elif grid[x][y] != ' ':
        print('This cell is occupied! Choose another one!')
        make_move()
        return
    grid[x][y] = 'X' if count % 2 == 0 else 'O'
    count += 1


print_grid()

while True:
    make_move()
    print_grid()
    rows_results = change_rows(grid)
    if ['X', 'X', 'X'] in rows_results:
        print('X wins')
        break
    if ['O', 'O', 'O'] in rows_results:
        print('O wins')
        break
    if not any(row.count(' ') for row in grid):
        print('Draw')
        break
