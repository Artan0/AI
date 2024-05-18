from searching_framework import *


def is_valid_man(man_pos, allowed):
    man_x = man_pos[0]
    man_y = man_pos[1]
    if 0 <= man_x <= 4 and 0 <= man_y <= 8 and (man_x, man_y) in allowed:
        return True
    return False


def move_valid_home(home_pos, direction):
    home_x = home_pos[0]
    home_y = home_pos[1]
    new_home = (home_x, home_y)

    if direction == "desno":
        if home_x+1 <= 4:
            new_x = home_x + 1
            new_home = (new_x, home_y)
        else:
            direction = "levo"
            new_x = home_x - 1
            new_home = (new_x, home_y)
    else:
        if home_x-1 >= 0:
            new_x = home_x - 1
            new_home = (new_x, home_y)
        else:
            direction = "desno"
            new_x = home_x + 1
            new_home = (new_x, home_y)

    return new_home, direction


class Home(Problem):
    def __init__(self, allowed_pos, init, goal=None):
        super().__init__(init, goal)
        self.allowed_pos = allowed_pos

    def successor(self, state):
        successor = dict()

        # (man, home, direction)
        man = state[0]
        home = state[1]
        direction = state[2]

        man_x = man[0]
        man_y = man[1]

        if is_valid_man((man_x, man_y + 1), self.allowed_pos):
            new_man = (man_x, man_y + 1)
            new_home, direct = move_valid_home(home, direction)
            successor["Gore 1"] = (new_man, new_home, direct)

        if is_valid_man((man_x, man_y + 2), self.allowed_pos):
            new_man = (man_x, man_y + 2)
            new_home, direct = move_valid_home(home, direction)
            successor["Gore 2"] = (new_man, new_home, direct)

        if is_valid_man((man_x - 1, man_y + 1), self.allowed_pos) or (man_x - 1, man_y + 1) in move_valid_home(home,
                                                                                                               direction)[0]:
            new_man = (man_x - 1, man_y + 1)
            new_home, direct = move_valid_home(home, direction)
            successor["Gore-levo 1"] = (new_man, new_home, direct)

        if is_valid_man((man_x - 2, man_y + 2), self.allowed_pos) or (man_x - 2, man_y + 2) in move_valid_home(home,
                                                                                                               direction)[0]:
            new_man = (man_x - 2, man_y + 2)
            new_home, direct = move_valid_home(home, direction)
            successor["Gore-levo 2"] = (new_man, new_home, direct)

        if is_valid_man((man_x + 1, man_y + 1), self.allowed_pos) or (man_x + 1, man_y + 1) in move_valid_home(home,
                                                                                                               direction)[0]:
            new_man = (man_x + 1, man_y + 1)
            new_home, direct = move_valid_home(home, direction)
            successor["Gore-desno 1"] = (new_man, new_home, direct)

        if is_valid_man((man_x + 2, man_y + 2), self.allowed_pos) or (man_x + 2, man_y + 2) in move_valid_home(home,
                                                                                                               direction)[0]:
            new_man = (man_x + 2, man_y + 2)
            new_home, direct = move_valid_home(home, direction)
            successor["Gore-desno 2"] = (new_man, new_home, direct)

        if is_valid_man((man_x, man_y), self.allowed_pos):
            new_man = (man_x, man_y)
            new_home, direct = move_valid_home(home, direction)
            successor["Stoj"] = (new_man, new_home, direct)

        # print(successor)
        return successor

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[1]

    def actions(self, state):
        return self.successor(state).keys()

    def h(self, node):
        man_pos = node.state[0]
        home_pos = node.state[1]
        x_man = man_pos[0]
        y_man = man_pos[1]
        x_house = home_pos[0]
        y_house = home_pos[1]
        res = abs(y_house - y_man)
        return res / 2


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    # your code here
    m = input().split(",")
    h = input().split(",")
    d = input('')

    man = (int(m[0]), int(m[1]))
    home = (int(h[0]), int(h[1]))

    problem = Home(allowed, (man, home, d))

    result = astar_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No solution!")
