from searching_framework import *


def check_valid(player, ball, opponents):
    pos_x = player[0]
    pos_y = player[1]

    ball_x = ball[0]
    ball_y = ball[1]

    if pos_x < 8 and pos_y < 6 and \
            pos_x not in opponents and \
            pos_y not in opponents and \
            ball_x not in opponents and \
            ball_y not in opponents and \
            ball_x < 8 and ball_y < 6:
        return True

    else:
        return False


def move_player_right(player, ball, opponents):
    pos_x = player[0]
    pos_y = player[1]
    if check_valid(player, ball, opponents):
        return pos_x + 1, pos_y
    return pos_x, pos_y


def move_player_up(player, ball, opponents):
    pos_x = player[0]
    pos_y = player[1]
    if check_valid(player, ball, opponents):
        return pos_x, pos_y + 1
    return pos_x, pos_y


def move_player_down(player, ball, opponents):
    pos_x = player[0]
    pos_y = player[1]
    if check_valid(player, ball, opponents):
        return pos_x, pos_y - 1
    return pos_x, pos_y


def move_player_up_right(player, ball, opponents):
    pos_x = player[0]
    pos_y = player[1]
    if check_valid(player, ball, opponents):
        return pos_x + 1, pos_y + 1
    return pos_x, pos_y


def move_player_down_right(player, ball, opponents):
    pos_x = player[0]
    pos_y = player[1]
    if check_valid(player, ball, opponents):
        return pos_x + 1, pos_y - 1
    return pos_x, pos_y


def move_ball_right(player, ball, opponents):
    ball_x = ball[0]
    ball_y = ball[1]
    player_x = player[0]
    player_y = player[1]

    if check_valid(player, ball, opponents) and player == ball:
        return player_x + 1, player_y, ball_x + 1, ball_y
    return player_x, player_y, ball_x, ball_y


def move_ball_up(player, ball, opponents):
    ball_x = ball[0]
    ball_y = ball[1]
    player_x = player[0]
    player_y = player[1]

    if check_valid(player, ball, opponents) and player == ball:
        return player_x, player_y + 1, ball_x, ball_y + 1
    return player_x, player_y, ball_x, ball_y


def move_ball_down(player, ball, opponents):
    ball_x = ball[0]
    ball_y = ball[1]
    player_x = player[0]
    player_y = player[1]

    if check_valid(player, ball, opponents) and player == ball:
        return player_x, player_y - 1, ball_x, ball_y - 1
    return player_x, player_y, ball_x, ball_y


def move_ball_up_right(player, ball, opponents):
    ball_x = ball[0]
    ball_y = ball[1]
    player_x = player[0]
    player_y = player[1]

    if check_valid(player, ball, opponents) and player == ball:
        return player_x + 1, player_y + 1, ball_x + 1, ball_y + 1
    return player_x, player_y, ball_x, ball_y


def move_ball_down_right(player, ball, opponents):
    ball_x = ball[0]
    ball_y = ball[1]
    player_x = player[0]
    player_y = player[1]

    if check_valid(player, ball, opponents) and player == ball:
        return player_x + 1, player_y - 1, ball_x + 1, ball_y - 1
    return player_x, player_y, ball_x, ball_y


class Football(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial,goal)

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
            successors['Turni topka gore'] = (new_player, new_ball,opponents,score)

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
        if new_ball_y != ball[1] and new_player_y != player[1] and new_ball_x != ball[0] and new_player_x != player[0]:
            new_player = (new_player_x, new_player_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka gore-desno'] = (new_player, new_ball, opponents, score)

        # Turni topka dolu-desno
        new_player_x, new_player_y, new_ball_x, new_ball_y = move_ball_down_right(player, ball, opponents)
        if new_ball_y != ball[1] and new_player_y != player[1] and new_ball_x != ball[0] and new_player_x != player[0]:
            new_player = (new_player_x, new_player_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka dolu-desno'] = (new_player, new_ball, opponents, score)

        return successors

    def goal_test(self, state):
        # return state[1] == state[3]
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
