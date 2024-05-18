from searching_framework import *


class Goal(Problem):
    def __init__(self, opponents, goal_cor, initial, goal=None):
        super().__init__(initial, goal)
        self.opponents = opponents
        self.goal_cor = goal_cor

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):

        return self.successor(state)[action]

    def goal_test(self, state):

        return state[1] in self.goal_cor

    def successor(self, state):
        successors = dict()
        man = state[0]
        ball = state[1]

        # Gore covek
        new_man_x, new_man_y = dviziGoreCovek(man, ball, self.opponents)
        if new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            successors['Pomesti coveche gore'] = (new_man, ball)

        # Dolu covek
        new_man_x, new_man_y = dviziDoluCovek(man, ball, self.opponents)
        if new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            successors['Pomesti coveche dolu'] = (new_man, ball)

        # Desno covek
        new_man_x, new_man_y = dviziDesnoCovek(man, ball, self.opponents)
        if new_man_x != man[0]:
            new_man = (new_man_x, new_man_y)
            successors['Pomesti coveche desno'] = (new_man, ball)

        # Gore Desno Covek
        new_man_x, new_man_y = dviziGoreDesnoCovek(man, ball, self.opponents)
        if new_man_x != man[0] and new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            successors['Pomesti coveche gore-desno'] = (new_man, ball)

        # Dolu Desno Covek
        new_man_x, new_man_y = dviziDoluDesnoCovek(man, ball, self.opponents)
        if new_man_x != man[0] and new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            successors['Pomesti coveche dolu-desno'] = (new_man, ball)

        # Gore topka
        new_man_x, new_man_y, new_ball_x, new_ball_y = dviziGoreTopka(man, ball, self.opponents)
        if new_ball_y != ball[1] and new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka gore'] = (new_man, new_ball)

        # Dolu topka
        new_man_x, new_man_y, new_ball_x, new_ball_y = dviziDoluTopka(man, ball, self.opponents)
        if new_ball_y != ball[1] and new_man_y != man[1]:
            new_man = (new_man_x, new_man_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka dolu'] = (new_man, new_ball)

        # Desno topka
        new_man_x, new_man_y, new_ball_x, new_ball_y = dviziDesnoTopka(man, ball, self.opponents)
        if new_ball_x != ball[0] and new_man_x != man[0]:
            new_man = (new_man_x, new_man_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka desno'] = (new_man, new_ball)

        # Gore Desno Topka
        new_man_x, new_man_y, new_ball_x, new_ball_y = dviziGoreDesnoTopka(man, ball, self.opponents)
        if new_ball_y != ball[1] and new_man_y != man[1] and new_ball_x != ball[0] and new_man_x != man[0]:
            new_man = (new_man_x, new_man_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka gore-desno'] = (new_man, new_ball)

        # Dolu Desno Topka
        new_man_x, new_man_y, new_ball_x, new_ball_y = dviziDoluDesnoTopka(man, ball, self.opponents)
        if new_ball_y != ball[1] and new_man_y != man[1] and new_ball_x != ball[0] and new_man_x != man[0]:
            new_man = (new_man_x, new_man_y)
            new_ball = (new_ball_x, new_ball_y)
            successors['Turni topka dolu-desno'] = (new_man, new_ball)

        return successors


def dviziGoreCovek(man, ball, opponents):
    new_man = (man[0], man[1] + 1)

    if check_valid(new_man, ball, opponents):
        return new_man[0], new_man[1]
    return man[0], man[1]


def dviziGoreTopka(man, ball, opponents):
    new_man = (man[0], man[1] + 1)
    new_ball = (ball[0], ball[1] + 1)

    if check_valid(new_man, new_ball, opponents) and new_man == ball:
        return new_man[0], new_man[1], new_ball[0], new_ball[1]
    return man[0], man[1], ball[0], ball[1]


def dviziDoluCovek(man, ball, opponents):
    new_man = (man[0], man[1] - 1)

    if check_valid(man, ball, opponents):
        return new_man[0], new_man[1]
    return man[0], man[1]


def dviziDoluTopka(man, ball, opponents):
    new_man = (man[0], man[1] - 1)
    new_ball = (ball[0], ball[1] - 1)

    if check_valid(new_man, new_ball, opponents) and new_man == ball:
        return new_man[0], new_man[1], new_ball[0], new_ball[1]
    return man[0], man[1], ball[0], ball[1]


def dviziDesnoCovek(man, ball, opponents):
    new_man = (man[0] + 1, man[1])

    if check_valid(man, ball, opponents):
        return new_man[0], new_man[1]
    return man[0], man[1]


def dviziDesnoTopka(man, ball, opponents):
    new_man = (man[0] + 1, man[1])
    new_ball = (ball[0] + 1, ball[1])

    if check_valid(new_man, new_ball, opponents) and new_man == ball:
        return new_man[0], new_man[1], new_ball[0], new_ball[1]
    return man[0], man[1], ball[0], ball[1]


def dviziGoreDesnoCovek(man, ball, opponents):
    new_man = (man[0] + 1, man[1] + 1)

    if check_valid(man, ball, opponents):
        return new_man[0], new_man[1]
    return man[0], man[1]


def dviziGoreDesnoTopka(man, ball, opponents):
    new_man = (man[0] + 1, man[1] + 1)
    new_ball = (ball[0] + 1, ball[1] + 1)

    if check_valid(new_man, new_ball, opponents) and new_man == ball:
        return new_man[0], new_man[1], new_ball[0], new_ball[1]
    return man[0], man[1], ball[0], ball[1]


def dviziDoluDesnoCovek(man, ball, opponents):
    new_man = (man[0] + 1, man[1] - 1)

    if check_valid(man, ball, opponents):
        return new_man[0], new_man[1]
    return man[0], man[1]


def dviziDoluDesnoTopka(man, ball, opponents):
    new_man = (man[0] + 1, man[1] - 1)
    new_ball = (ball[0] + 1, ball[1] - 1)

    if check_valid(new_man, new_ball, opponents) and new_man == ball:
        return new_man[0], new_man[1], new_ball[0], new_ball[1]
    return man[0], man[1], ball[0], ball[1]


def check_valid(man, ball, opponents):
    man_pos = man
    ball_pos = ball

    return 0 <= man_pos[0] < 8 and \
        0 <= man_pos[1] < 6 and \
        0 <= ball_pos[0] < 8 and \
        0 <= ball_pos[1] < 6 and \
        man_pos != opponents[4] and man_pos != opponents[11] and \
        ball_pos not in opponents and \
        man_pos != ball_pos


if __name__ == '__main__':
    tmp = input().split(",")
    player = (int(tmp[0]), int(tmp[1]))

    tmp = input().split(",")
    ball_input = (int(tmp[0]), int(tmp[1]))

    opponents_radius = ((2, 2), (3, 2), (4, 2),
                        (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
                        (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),
                        (4, 5), (5, 5), (6, 5))

    goal_place = ((7, 2), (7, 3))

    g = Goal(opponents_radius, goal_place, (player, ball_input))
    result = breadth_first_graph_search(g)
    print(result.solution())
