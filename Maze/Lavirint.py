from searching_framework import *


def is_valid(man, walls, size):
    x = man[0]
    y = man[1]
    if x < 0 or y < 0 or x >= size or y >= size or (x, y) in walls:
        return False
    return True


class Maze(Problem):
    def __init__(self, size, wall, init, goal=None):
        super().__init__(init, goal)
        self.size = size
        self.walls = wall

    def successor(self, state):
        successor = dict()
        # (man)
        man = state
        man_x = man[0]
        man_y = man[1]

        wall_pos = self.walls
        size = self.size

        if is_valid((man_x, man_y + 1), wall_pos, size):
            new_man = (man_x, man_y + 1)
            successor["Gore"] = new_man

        if is_valid((man_x, man_y - 1), wall_pos, size):
            new_man = (man_x, man_y - 1)
            successor["Dolu"] = new_man

        if is_valid((man_x - 1, man_y), wall_pos, size):
            new_man = (man_x - 1, man_y)
            successor["Levo"] = new_man

        if is_valid((man_x + 2, man_y), wall_pos, size) and (man_x + 1, man_y) not in wall_pos:
            new_man = (man_x + 2, man_y)
            successor["Desno 2"] = new_man

        if is_valid((man_x + 3, man_y), wall_pos, size) and (man_x + 1, man_y) not in wall_pos and (man_x + 2, man_y) not in wall_pos:
            new_man = (man_x + 3, man_y)
            successor["Desno 3"] = new_man

        # print(state, successor)
        return successor

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        man = node.state
        man_x = man[0]
        man_y = man[1]
        home_x = self.goal[0]
        home_y = self.goal[1]
        res = abs(home_x - man_x) + abs(home_y - man_y)
        return res / 3

    def result(self, state, action):
        return self.successor(state)[action]

    def actions(self, state):
        return self.successor(state).keys()


if __name__ == '__main__':
    # your code here

    table_size = int(input())

    wall_number = int(input())
    walls = list()
    for wall in range(wall_number):
        walls.append(tuple(map(int, input().split(','))))

    m = input().split(",")
    h = input().split(",")

    man = (int(m[0]), int(m[1]))
    home = (int(h[0]), int(h[1]))

    maze = Maze(table_size, walls, man, home)
    result = astar_search(maze)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")
