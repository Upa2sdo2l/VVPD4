import sys


def count_knight_moves(start, end):

    end_x, end_y = end

    moves = 1
    current_position = start

    while current_position != end:
        possible_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        next_moves = [(current_position[0] + move[0], current_position[1] + move[1]) for move in possible_moves]

        valid_moves = [(x, y) for x, y in next_moves if 1 <= x <= 8 and 1 <= y <= 8]

        if end in valid_moves:
            break

        min_distance = float('inf')
        next_position = None

        for move in valid_moves:
            distance = abs(move[0] - end_x) + abs(move[1] - end_y)
            if distance < min_distance:
                min_distance = distance
                next_position = move

        current_position = next_position
        moves += 1

    return moves


def min_moves_between_knights(knight1, knight2):
    return count_knight_moves(knight1, knight2)


def main():
    while True:
        print('[1]Найти минимальное количество ходов\n'
              '[2]Найти минимальное расстояние\n'
              '[3]Завершить работу программы')
        choice = input()
        try:
            choice = int(choice)
            if choice == 1:
                print('Введите начальное и конечное положение коня на доске')
                print('Введите начальное положение:')
                x1, y1 = input().split()
                print('Введите конечное положение:')
                x2, y2 = input().split()
                try:
                    x1 = int(x1)
                    y1 = int(y1)
                    x2 = int(x2)
                    y2 = int(y2)
                    print(f'минимальное количество ходов:{count_knight_moves((x1,y1), (x2,y2))}')
                except ValueError:
                    print('Неверный ввод')
            elif choice == 2:
                print('Введите положение коней на доске')
                print('Введите положение первого коня:')
                x1, y1 = input().split()
                print('Введите положение второго коня:')
                x2, y2 = input().split()
                try:
                    x1 = int(x1)
                    y1 = int(y1)
                    x2 = int(x2)
                    y2 = int(y2)
                    print(f'минимальное расстояние:{min_moves_between_knights((x1, y1), (x2, y2))}')
                except ValueError:
                    print('Неверный ввод')
            elif choice == 3:
                sys.exit(0)
            else:
                print('Неверный ввод')
        except ValueError:
            print('Неверный ввод')


if __name__ == '__main__':
    main()
