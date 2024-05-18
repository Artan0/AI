from searching_framework import Problem, astar_search


def move_home(home_pos, direction):
    new_home = home_pos
    if direction == "desno" and home_pos[0] < 4:
        new_home = (home[0] + 1, home[1])
        if new_home[0] == 4:
            direction = "levo"
    else:
        new_home = (home[0] - 1, home[1])
        if new_home[0] == 0:
            direction = "desno"
    return new_home, direction


def dont_move(man_pos, home_pos, allowed_pos, direction):
    new_home, new_direction = move_home(home_pos, direction)
    return man_pos, new_home, new_direction


def move_up_1(man_pos, home_pos, allowed_pos, direction):
    new_man = man_pos
    new_home = home_pos

    if 0 < man_pos[0] < 4 and 0 < man_pos[1] < 8:
        if (man_pos[0], man_pos[1] + 1) in allowed_pos:
            new_man = (man_pos[0], man_pos[1] + 1)
            new_home, direction = move_home(home_pos, direction)
    return new_man, new_home, direction


def move_up_2(man_pos, home_pos, allowed_pos, direction):
    new_man = man_pos
    new_home = home_pos

    if 0 < man_pos[0] < 4 and 0 < man_pos[1] < 8:
        if (man_pos[0], man_pos[1] + 2) in allowed_pos:
            new_man = (man_pos[0], man_pos[1] + 2)
            new_home, direction = move_home(home_pos, direction)

    return new_man, new_home, direction


def move_up_right_1(man_pos, home_pos, allowed_pos, direction):
    new_man = man_pos
    new_home = home_pos

    if 0 < man_pos[0] < 4 and 0 < man_pos[1] < 8:
        if (man_pos[0] + 1, man_pos[1] + 1) in allowed_pos:
            new_man = (man_pos[0] + 1, man_pos[1] + 1)
            new_home, direction = move_home(home_pos, direction)

    return new_man, new_home, direction


def move_up_right_2(man_pos, home_pos, allowed_pos, direction):
    new_man = man_pos
    new_home = home_pos

    if 0 < man_pos[0] < 4 and 0 < man_pos[1] < 8:
        if (man_pos[0] + 2, man_pos[1] + 2) in allowed_pos:
            new_man = (man_pos[0] + 2, man_pos[1] + 2)
            new_home, direction = move_home(home_pos, direction)

    return new_man, new_home, direction


def move_up_left_1(man_pos, home_pos, allowed_pos, direction):
    new_man = man_pos
    new_home = home_pos

    if 0 < man_pos[0] < 4 and 0 < man_pos[1] < 8:
        if (man_pos[0] - 1, man_pos[1] + 1) in allowed_pos:
            new_man = (man_pos[0] - 1, man_pos[1] + 1)
            new_home, direction = move_home(home_pos, direction)

    return new_man, new_home, direction


def move_up_left_2(man_pos, home_pos, allowed_pos, direction):
    new_man = man_pos
    new_home = home_pos

    if 0 < man_pos[0] < 4 and 0 < man_pos[1] < 8:
        if (man_pos[0] - 2, man_pos[1] + 2) in allowed_pos:
            new_man = (man_pos[0] - 2, man_pos[1] + 2)
            new_home, direction = move_home(home_pos, direction)

    return new_man, new_home, direction


def is_valid(man_pos, allowed_pos):
    x = man_pos[0]
    y = man_pos[1]
    if 0 < x < 4 and 0 < y < 8 and (y, x) in allowed_pos:
        return True
    return False


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

        # Up
        new_man, new_home, dir = move_up_1(man_pos, home_pos, self.allowed_pos, direction)
        if is_valid(new_man, self.allowed_pos):
            succ["Gore 1"] = (new_man, new_home, dir)

        new_man, new_home, dir = move_up_2(man_pos, home_pos, self.allowed_pos, direction)
        if is_valid(new_man, self.allowed_pos):
            succ["Gore 2"] = (new_man, new_home, dir)

        # Up left
        new_man, new_home, dir = move_up_left_1(man_pos, home_pos, self.allowed_pos, direction)
        if is_valid(new_man, self.allowed_pos):
            succ["Gore-levo 1"] = (new_man, new_home, dir)

        new_man, new_home, dir = move_up_left_2(man_pos, home_pos, self.allowed_pos, direction)
        if is_valid(new_man, self.allowed_pos):
            succ["Gore-levo 2"] = (new_man, new_home, dir)

        # Up right
        new_man, new_home, dir = move_up_right_1(man_pos, home_pos, self.allowed_pos, direction)
        if is_valid(new_man, self.allowed_pos):
            succ["Gore-desno 1"] = (new_man, new_home, dir)

        new_man, new_home, dir = move_up_right_2(man_pos, home_pos, self.allowed_pos, direction)
        if is_valid(new_man, self.allowed_pos):
            succ["Gore-desno 2"] = (new_man, new_home, dir)

        # Do not move
        new_man, newhome, dir = dont_move(man_pos, home_pos, self.allowed_pos, direction)
        if is_valid(new_man, self.allowed_pos):
            succ["Stoj"] = (new_man, new_home, dir)

        # print(state, succ)
        return succ

    def goal_test(self, state):
        return state[0] == state[1]

    def h(self, node):
        man_pos = node.state[0]
        home_pos = node.state[1]
        x_man, y_man = man_pos
        x_house, y_house = home_pos
        return abs(y_man - y_house) / 2

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
        print(result.solution())
    else:
        print("No Solution!")
