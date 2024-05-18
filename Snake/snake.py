from searching_framework import *


def move_up(x, y, red_apples):
    if y < 9 and (x, y + 1) not in red_apples:
        y += 1
    return y


def move_down(x, y, red_apples):
    if y > 0 and (x, y - 1) not in red_apples:
        y -= 1
    return y


def move_left(x, y, red_apples):
    if x > 0 and (x - 1, y) not in red_apples:
        x -= 1
    return x


def move_right(x, y, red_apples):
    if x < 9 and (x + 1, y) not in red_apples:
        x += 1
    return x


class Snake(Problem):
    def __init__(self, red_apples, initial, goal=None):
        super(Snake, self).__init__(initial, goal)
        self.red_apples = red_apples

    def successor(self, state):
        successors = dict()
        # (head, body, direction, green_apples)
        head = state[0]
        body = state[1]
        direction = state[2]
        head_x, head_y = head[0], head[1]

        green_apples = state[3]

        if direction == "down":
            new_y = move_down(head_x, head_y, self.red_apples)
            if new_y != head_y:
                if new_y not in body:
                    new_body = list(body)

                    if any((head_x, new_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (head_x, new_y + 1))
                        successors['ProdolzhiPravo'] = ((head_x, new_y), tuple(new_body), "down",
                                                        tuple([a for a in green_apples if
                                                               [head_x, new_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (head_x, new_y+1))
                        # new_body.pop()
                        successors['ProdolzhiPravo'] = ((head_x, new_y), tuple(new_body), "down", tuple(green_apples))

            new_x = move_left(head_x, head_y, self.red_apples)
            if new_x != head_x:
                if new_x not in body:
                    new_body = list(body)

                    if any((new_x, head_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (new_x + 1, head_y))
                        successors['SvrtiDesno'] = ((new_x, head_y), tuple(new_body), "left",
                                                    tuple([a for a in green_apples if
                                                           [new_x, head_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (new_x+1, head_y))
                        # new_body.pop()
                        successors['SvrtiDesno'] = ((new_x, head_y), tuple(new_body), "left", tuple(green_apples))

            new_x = move_right(head_x, head_y, self.red_apples)
            if new_x != head_x:
                if new_x not in body:
                    new_body = list(body)

                    if any((new_x, head_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (new_x + 1, head_y))
                        successors['SvrtiLevo'] = ((new_x, head_y), tuple(new_body), "right",
                                                   tuple([a for a in green_apples if
                                                          [new_x, head_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (new_x+1, head_y))
                        # new_body.pop()
                        successors['SvrtiLevo'] = ((new_x, head_y), tuple(new_body), "right", tuple(green_apples))

        if direction == "left":
            new_x = move_left(head_x, head_y, self.red_apples)
            if new_x != head_x:
                if new_x not in body:
                    new_body = list(body)

                    if any((new_x, head_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (new_x + 1, head_y))
                        successors['ProdolzhiPravo'] = ((new_x, head_y), tuple(new_body), "left",
                                                        tuple([a for a in green_apples if
                                                               [new_x, head_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (new_x+1, head_y))
                        # new_body.pop()
                        successors['ProdolzhiPravo'] = ((new_x, head_y), tuple(new_body), "left", tuple(green_apples))

            new_y = move_down(head_x, head_y, self.red_apples)
            if new_y != head_y:
                if new_y not in body:
                    new_body = list(body)

                    if any((head_x, new_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (head_x, new_y + 1))
                        successors['SvrtiLevo'] = ((head_x, new_y), tuple(new_body), "down",
                                                   tuple([a for a in green_apples if
                                                          [head_x, new_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (head_x, new_y+1))
                        # new_body.pop()
                        successors['SvrtiLevo'] = ((head_x, new_y), tuple(new_body), "down", tuple(green_apples))

            new_y = move_up(head_x, head_y, self.red_apples)
            if new_y != head_y:
                if new_y not in body:
                    new_body = list(body)

                    if any((head_x, new_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (head_x, new_y + 1))
                        successors['SvrtiDesno'] = ((head_x, new_y), tuple(new_body), "up",
                                                    tuple([a for a in green_apples if
                                                           [head_x, new_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (head_x, new_y+1))
                        # new_body.pop()
                        successors['SvrtiDesno'] = ((head_x, new_y), tuple(new_body), "up", tuple(green_apples))

        if direction == "right":
            new_x = move_right(head_x, head_y, self.red_apples)
            if new_x != head_x:
                if new_x not in body:
                    new_body = list(body)

                    if any((new_x, head_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (new_x + 1, head_y))
                        successors['ProdolzhiPravo'] = ((new_x, head_y), tuple(new_body), "right",
                                                        tuple([a for a in green_apples if
                                                               [new_x, head_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (new_x+1, head_y))
                        # new_body.pop()
                        successors['ProdolzhiPravo'] = ((new_x, head_y), tuple(new_body), "right", tuple(green_apples))

            new_y = move_up(head_x, head_y, self.red_apples)
            if new_y != head_y:
                if new_y not in body:
                    new_body = list(body)

                    if any((head_x, new_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (head_x, new_y + 1))
                        successors['SvrtiLevo'] = ((head_x, new_y), tuple(new_body), "up",
                                                   tuple([a for a in green_apples if
                                                          [head_x, new_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (head_x, new_y+1))
                        # new_body.pop()
                        successors['SvrtiLevo'] = ((head_x, new_y), tuple(new_body), "up", tuple(green_apples))

            new_y = move_down(head_x, head_y, self.red_apples)
            if new_y != head_y:
                if new_y not in body:
                    new_body = list(body)

                    if any((head_x, new_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (head_x, new_y + 1))
                        successors['SvrtiDesno'] = ((head_x, new_y), tuple(new_body), "down",
                                                    tuple([a for a in green_apples if
                                                           [head_x, new_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (head_x, new_y+1))
                        # new_body.pop()
                        successors['SvrtiDesno'] = ((head_x, new_y), tuple(new_body), "down", tuple(green_apples))

        if direction == "up":
            new_y = move_up(head_x, head_y, self.red_apples)
            if new_y != head_y:
                if new_y not in body:
                    new_body = list(body)

                    if any((head_x, new_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (head_x, new_y + 1))
                        successors['ProdolzhiPravo'] = ((head_x, new_y), tuple(new_body), "up",
                                                        tuple([a for a in green_apples if
                                                               [head_x, new_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (head_x, new_y+1))
                        # new_body.pop()
                        successors['ProdolzhiPravo'] = ((head_x, new_y), tuple(new_body), "up", tuple(green_apples))

            new_x = move_left(head_x, head_y, self.red_apples)
            if new_x != head_x:
                if new_x not in body:
                    new_body = list(body)

                    if any((new_x, head_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (new_x + 1, head_y))
                        successors['SvrtiLevo'] = ((new_x, head_y), tuple(new_body), "left",
                                                   tuple([a for a in green_apples if
                                                          [new_x, head_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (new_x+1, head_y))
                        # new_body.pop()
                        successors['SvrtiLevo'] = ((new_x, head_y), tuple(new_body), "left", tuple(green_apples))

            new_x = move_right(head_x, head_y, self.red_apples)
            if new_x != head_x:
                if new_x not in body:
                    new_body = list(body)

                    if any((new_x, head_y) == (a[0], a[1]) for a in green_apples):
                        new_body.insert(0, (new_x + 1, head_y))
                        successors['SvrtiDesno'] = ((new_x, head_y), tuple(new_body), "right",
                                                    tuple([a for a in green_apples if
                                                           [new_x, head_y] != [a[0], a[1]]]), self.red_apples)
                    else:
                        # new_body.insert(0, (new_x+1, head_y))
                        # new_body.pop()
                        successors['SvrtiDesno'] = ((new_x, head_y), tuple(new_body), "right", tuple(green_apples))

        return successors

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[3]) == 0

    def actions(self, state):
        return self.successor(state).keys()


if __name__ == '__main__':
    zeleni_jabolki = list()
    crveni_jabolki = list()

    broj_zeleni = int(input())

    snake_body = [(0, 8), (0, 9)]
    snake_head = [0, 7]
    nasoka = "down"

    for i in range(broj_zeleni):
        par = [int(i) for i in input().split(",")]
        zeleni_jabolki.append(par)

    for i in range(broj_zeleni):
        zeleni_jabolki[i] = tuple(zeleni_jabolki[i])

    broj_crveni = int(input())
    for i in range(broj_crveni):
        par = [int(i) for i in input().split(",")]
        crveni_jabolki.append(par)

    for i in range(broj_crveni):
        crveni_jabolki[i] = tuple(crveni_jabolki[i])

    snake = Snake(tuple(crveni_jabolki), (tuple(snake_head), tuple(snake_body), nasoka, tuple(zeleni_jabolki)))

    result = breadth_first_graph_search(snake)

    if result is not None:
        print(result.solution())
