from searching_framework import Problem, astar_search


def dont_move(man_pos, home_pos, allowed_pos, direction):
    new_home = home_pos

    if direction == "desno" and home_pos[0] < 4:
        new_home = home[0] + 1, home[1]
        if new_home[0] == 4:
            direction = "levo"
    elif direction == "levo" and home_pos[0] > 0:
        new_home = home[0] - 1, home[1]
        if new_home[0] == 0:
            direction = "desno"
    return man_pos, new_home, direction


def move_up(man_pos, home_pos, allowed_pos, direction, is_double):
    new_man = man_pos
    new_home = home_pos

    if 0 < man_pos[0] < 4 and 0 < man_pos[1] < 8:
        if (man_pos[0], man_pos[1] + 2) in allowed_pos:
            new_man = man_pos[0], man_pos[1] + 2
            is_double = True
        else:
            new_man = man_pos[0], man_pos[1] + 1
            is_double = False

    if direction == "desno" and home_pos[0] < 4:
        new_home = home[0] + 1, home[1]
        if new_home[0] == 4:
            direction = "levo"
    elif direction == "levo" and home_pos[0] > 0:
        new_home = home[0] - 1, home[1]
        if new_home[0] == 0:
            direction = "desno"

    return new_man, new_home, direction, is_double


def move_up_right(man_pos, home_pos, allowed_pos, direction, is_double):
    new_man = man_pos
    new_home = home_pos

    if 0 < man_pos[0] < 4 and 0 < man_pos[1] < 8:
        if (man_pos[0] + 2, man_pos[1] + 2) in allowed_pos:
            new_man = man_pos[0] + 2, man_pos[1] + 2
            is_double = True
        else:
            new_man = man_pos[0] + 1, man_pos[1] + 1
            is_double = False

    if direction == "desno" and home_pos[0] < 4:
        new_home = home[0] + 1, home[1]
        if new_home[0] == 4:
            direction = "levo"
    elif direction == "levo" and home_pos[0] > 0:
        new_home = home[0] - 1, home[1]
        if new_home[0] == 0:
            direction = "desno"

    return new_man, new_home, direction, is_double


def move_up_left(man_pos, home_pos, allowed_pos, direction, is_double):
    new_man = man_pos
    new_home = home_pos

    if 0 < man_pos[0] < 4 and 0 < man_pos[1] < 8:
        if (man_pos[0] - 2, man_pos[1] + 2) in allowed_pos:
            new_man = man_pos[0] - 2, man_pos[1] + 2
            is_double = True
        else:
            new_man = man_pos[0] - 1, man_pos[1] + 1
            is_double = False

    if direction == "desno" and home_pos[0] < 4:
        new_home = home[0] + 1, home[1]
        if new_home[0] == 4:
            direction = "levo"
    elif direction == "levo" and home_pos[0] > 0:
        new_home = home[0] - 1, home[1]
        if new_home[0] == 0:
            direction = "desno"

    return new_man, new_home, direction, is_double


class HomeMan(Problem):
    def __init__(self, allowed_pos, init, goal=None):
        super().__init__(init, goal)
        self.allowed_pos = allowed_pos

    def successor(self, state):
        succ = dict()

        # (man, home,direction)

        man_pos = state[0]
        home_pos = state[1]
        direction = state[2]
        is_double = False

        # Up
        new_man, new_home, dir, double = move_up(man_pos, home_pos, self.allowed_pos, direction, is_double)
        if man_pos[1] != new_man[1]:
            if double:
                succ["Gore 2"] = (new_man, new_home, dir)
            else:
                succ["Gore 1"] = (new_man, new_home, dir)

        # Up left
        new_man, new_home, dir, double = move_up_left(man_pos, home_pos, self.allowed_pos, direction, is_double)
        if man_pos[1] != new_man[1]:
            if double:
                succ["Gore-levo 2"] = (new_man, new_home, dir)
            else:
                succ["Gore-levo 1"] = (new_man, new_home, dir)

        # Up right
        new_man, new_home, dir, double = move_up_right(man_pos, home_pos, self.allowed_pos, direction, is_double)
        if man_pos[1] != new_man[1]:
            if double:
                succ["Gore-desno 2"] = (new_man, new_home, dir)
            else:
                succ["Gore-desno 1"] = (new_man, new_home, dir)

        # Do not move
        new_man, newhome, dir = dont_move(man_pos, home_pos, self.allowed_pos, direction)
        if man_pos[1] == new_man[1]:
            succ["Stoj"] = (new_man, newhome, dir)

        print(state, succ)
        return succ

    def goal_test(self, state):
        return state[0] == state[1]

    def h(self, node):
        man_pos = node.state[0]
        home_pos = node.state[1]
        x_man, y_man = man_pos
        x_house, y_house = home_pos
        return abs(y_man - y_house)/2

    def result(self, state, action):
        return self.successor(state)[action]

    def actions(self, state):
        return self.successor(state).keys()


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    # your code here
    # (man, home,direction)
    m = input().split(",")
    h = input().split(",")
    d = input('')

    man = (int(m[0]), int(m[1]))
    home = (int(h[0]), int(h[1]))

    homeMan = HomeMan(allowed, (man, home, d))

    result = astar_search(homeMan)

    if result is not None:
        print(result)
    else:
        print("No Solution!")
