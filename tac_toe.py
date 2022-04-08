# Сброс игровой матрицы в начальное состояние
def init_game():
    game_board = [['-' for i in range(3)] for j in range(3)]
    return game_board

# Получение информации о ходе игрока
def ask_user_move(game_board, user):
    while True:
        coords = input('Введите координаты хода для игрока \'' + user + '\' в формате (X,Y): ')
        if coords == '':
            continue
        coords_num = list(map(int, coords.split(',')))

        if len(coords_num) != 2 and not coords_num[0] in range(1, 3) and not coords_num[1] in range(1, 3):
            print('Не верное значение. Укажите числа в диапазоне от 1 до 3')
            continue

        if game_board[coords_num[0]-1][coords_num[1]-1] == '-':
            return coords_num
        else:
            print('Данная ячейка уже занята')


# Внисение изминений в игровое поле
def mark_move(game_board, coords, user):
    game_board[coords[0]-1][coords[1]-1] = user

# Поиск информации о ходе ИИ
def ai_move(game_board):
    # В данной версии вместе ИИ играет второй игрок
    coords = ask_user_move(game_board, 'o')
    return coords

# Проверка на окончание игры
def check_game_end(game_board):
    # Проверка на окончание игры по строкам
    for i in range(3):
        line_x = 0
        line_o = 0
        for j in range(3):
            if game_board[i][j] == 'x':
                line_x = line_x + 1
            if game_board[i][j] == 'o':
                line_o = line_o + 1
        if line_x == 3:
            return 'x'
        elif line_o == 3:
            return 'o'

    # Проверка на окончание игры по столбцам
    for j in range(3):
        line_x = 0
        line_o = 0
        for i in range(3):
            if game_board[i][j] == 'x':
                line_x = line_x + 1
            if game_board[i][j] == 'o':
                line_o = line_o + 1
        if line_x == 3:
            return 'x'
        elif line_o == 3:
            return 'o'

    # Проверка на окончание игры по диагонали
    line_x = 0
    line_o = 0
    for i in range(3):
        if game_board[i][i] == 'x':
            line_x = line_x + 1
        if game_board[i][i] == 'o':
            line_o = line_o + 1
    if line_x == 3:
        return 'x'
    elif line_o == 3:
        return 'o'

    # Проверка на окончание игры по диагонали 2
    line_x = 0
    line_o = 0
    for i in range(3):
        if game_board[2-i][i] == 'x':
            line_x = line_x + 1
        if game_board[2-i][i] == 'o':
            line_o = line_o + 1
    if line_x == 3:
        return 'x'
    elif line_o == 3:
        return 'o'

    # Проверка на наличие хотя бы одной пустой ячейки
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == '-':
                return '-'

    return 'n'


# Отображение игровой доски
def show_game_board(game_board):
    print('   |  1  |  2  |  3  |')

    for i in range(3):
        print(str(i+1)  + '  |', end='')
        for j in range(3):
            print('  ' + game_board[i][j], end='  |')
        print()



# Отображение результатов игры
def show_game_result(game_board):
    res = check_game_end(game_board)
    if res == 'x':
        print('Победил игрок X')
    elif res == 'o':
        print('Победил игрок O')
    elif res == 'n':
        print('Ничья')

# Начало выполнения программы
game_board = init_game()

while check_game_end(game_board) in ['-']:
    show_game_board(game_board)

    # Игрок 1
    coords = ask_user_move(game_board, 'x')
    mark_move(game_board, coords, 'x')
    show_game_board(game_board)

    # Проверка на завершение игры
    if check_game_end(game_board) in ['x', 'o', 'n']:
        break

    # Игрок 2
    coords = ai_move(game_board)
    mark_move(game_board, coords, 'o')

show_game_result(game_board)
