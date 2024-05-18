from searching_framework import *


def check_valid(player, ball, opponents):
    player_pos = player
    ball_pos = ball

    return 0 <= player_pos[0] < 8 and \
        0 <= player_pos[1] < 6 and \
        0 <= ball_pos[0] < 8 and \
        0 <= ball_pos[1] < 6 and \
        player_pos != opponents[0] and player_pos != opponents[1] and \
        ball_pos not in opponents and \
        player_pos != ball_pos


def move_player_up(player, ball, opponents):
    new_player = (player[0], player[1] + 1)

    if check_valid(new_player, ball, opponents):
        return new_player[0], new_player[1]
    return player[0], player[1]


def move_ball_up(player, ball, opponents):
    new_player = (player[0], player[1] + 1)
    new_ball = (ball[0], ball[1] + 1)

    if check_valid(new_player, new_ball, opponents) and new_player == ball:
        return new_player[0], new_player[1], new_ball[0], new_ball[1]
    return player[0], player[1], ball[0], ball[1]


def move_player_down(player, ball, opponents):
    new_player = (player[0], player[1] - 1)

    if check_valid(player, ball, opponents):
        return new_player[0], new_player[1]
    return player[0], player[1]


def move_ball_down(player, ball, opponents):
    new_player = (player[0], player[1] - 1)
    new_ball = (ball[0], ball[1] - 1)

    if check_valid(new_player, new_ball, opponents) and new_player == ball:
        return new_player[0], new_player[1], new_ball[0], new_ball[1]
    return player[0], player[1], ball[0], ball[1]


def move_player_right(player, ball, opponents):
    new_player = (player[0] + 1, player[1])

    if check_valid(player, ball, opponents):
        return new_player[0], new_player[1]
    return player[0], player[1]


def move_ball_right(player, ball, opponents):
    new_player = (player[0] + 1, player[1])
    new_ball = (ball[0] + 1, ball[1])

    if check_valid(new_player, new_ball, opponents) and new_player == ball:
        return new_player[0], new_player[1], new_ball[0], new_ball[1]
    return player[0], player[1], ball[0], ball[1]


def move_player_up_right(player, ball, opponents):
    new_player = (player[0] + 1, player[1] + 1)

    if check_valid(player, ball, opponents):
        return new_player[0], new_player[1]
    return player[0], player[1]


def move_ball_up_right(player, ball, opponents):
    new_player = (player[0] + 1, player[1] + 1)
    new_ball = (ball[0] + 1, ball[1] + 1)

    if check_valid(new_player, new_ball, opponents) and new_player == ball:
        return new_player[0], new_player[1], new_ball[0], new_ball[1]
    return player[0], player[1], ball[0], ball[1]


def move_player_down_right(player, ball, opponents):
    new_player = (player[0] + 1, player[1] - 1)

    if check_valid(player, ball, opponents):
        return new_player[0], new_player[1]
    return player[0], player[1]


def move_ball_down_right(player, ball, opponents):
    new_player = (player[0] + 1, player[1] - 1)
    new_ball = (ball[0] + 1, ball[1] - 1)

    if check_valid(new_player, new_ball, opponents) and new_player == ball:
        return new_player[0], new_player[1], new_ball[0], new_ball[1]
    return player[0], player[1], ball[0], ball[1]


class Football(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        # (player, ball, opponent, score)

        successors = dict()

        player = state[0]
        ball = state[1]
        opponents = state[2]
        score = state[3]

        # Pomesti coveche gore
        new_player = move_player_up(player, ball, opponents)
        if new_player[1] != player[1]:
            successors['Pomesti coveche gore'] = (new_player, ball, opponents, score)

        # Pomesti coveche dolu
        new_player = move_player_down(player, ball, opponents)
        if new_player[1] != player[1]:
            successors['Pomesti coveche dolu'] = (new_player, ball, opponents, score)

        # Pomesti coveche desno
        new_player = move_player_right(player, ball, opponents)
        if new_player[0] != player[0]:
            successors['Pomesti coveche desno'] = (new_player, ball, opponents, score)

        # Pomesti coveche gore desno
        new_player = move_player_up_right(player, ball, opponents)
        if new_player[0] != player[0] and new_player[1] != player[1]:
            successors['Pomesti coveche gore-desno'] = (new_player, ball, opponents, score)

        # Pomesti choveche dolu desno
        new_player = move_player_down_right(player, ball, opponents)
        if new_player[0] != player[0] and new_player[1] != player[1]:
            successors['Pomesti coveche dolu-desno'] = (new_player, ball, opponents, score)

        # Turni topka gore
        new_player_x, new_player_y, new_ball_x, new_ball_y = move_ball_up(player, ball, opponents)
        if new_ball_y != ball[1] and new_player_y != player[1]:
            new_player = (new_player_x, new_player_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka gore'] = (new_player, new_ball, opponents, score)

        # Turni topka dole
        new_player_x, new_player_y, new_ball_x, new_ball_y = move_ball_down(player, ball, opponents)
        if new_ball_y != ball[1] and new_player_y != player[1]:
            new_player = (new_player_x, new_player_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka dolu'] = (new_player, new_ball, opponents, score)

        # Turni topka desno
        new_player_x, new_player_y, new_ball_x, new_ball_y = move_ball_right(player, ball, opponents)
        if new_ball_x != ball[0] and new_player_x != player[0]:
            new_player = (new_player_x, new_player_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka desno'] = (new_player, new_ball, opponents, score)

        # Turni topka gore-desno
        new_player_x, new_player_y, new_ball_x, new_ball_y = move_ball_up_right(player, ball, opponents)
        if new_ball_x != ball[0] and new_player_x != player[0] and new_ball_y != ball[1] and new_player_y != player[1]:
            new_player = (new_player_x, new_player_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka gore-desno'] = (new_player, new_ball, opponents, score)

        # Turni topka dolu-desno
        new_player_x, new_player_y, new_ball_x, new_ball_y = move_ball_down_right(player, ball, opponents)
        if new_ball_x != ball[0] and new_player_x != player[0] and new_ball_y != ball[1] and new_player_y != player[1]:
            new_player = (new_player_x, new_player_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka dolu-desno'] = (new_player, new_ball, opponents, score)

        return successors

    def goal_test(self, state):
        return state[1] in state[3]

    def result(self, state, action):
        return self.successor(state)[action]

    def actions(self, state):
        return self.successor(state).keys()


if __name__ == '__main__':
    p = input().split(",")
    b = input().split(",")

    opponents = ((3, 3), (5, 4))
    score = ((7, 2), (7, 3))

    player = (int(p[0]), int(p[1]))
    ball = (int(b[0]), int(b[1]))

    football = Football((player, ball, opponents, score))
    result = breadth_first_graph_search(football)
    if result is not None:
        print(result.solution())
