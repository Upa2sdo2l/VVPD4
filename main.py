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
