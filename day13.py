import enum
from collections import Counter


class CartDirections(enum.IntEnum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


class CartCurve(enum.IntEnum):
    LEFT = 0
    STRAIGHT = 1
    RIGHT = 2


class Cart:
    def __init__(self, row, column, motion):
        self.row = row
        self.column = column
        if motion == '>':
            self.motion = CartDirections.RIGHT
        if motion == '<':
            self.motion = CartDirections.LEFT
        if motion == 'v':
            self.motion = CartDirections.DOWN
        if motion == '^':
            self.motion = CartDirections.UP
        self.curve = CartCurve.LEFT
        self.crashed = False

    def turn_left(self):
        self.motion = CartDirections((int(self.motion) - 1) % 4)
        pass

    def turn_right(self):
        self.motion = CartDirections((int(self.motion) + 1) % 4)

    def new_curve(self):
        self.curve = CartCurve((int(self.curve) + 1) % 3)

    def move_forward(self):
        if self.motion == CartDirections.RIGHT:
            self.column += 1
        if self.motion == CartDirections.LEFT:
            self.column -= 1
        if self.motion == CartDirections.UP:
            self.row -= 1
        if self.motion == CartDirections.DOWN:
            self.row += 1

    def move(self, grid):
        case = grid[self.row][self.column]

        if case == '-':
            self.move_forward()

        if case == '|':
            self.move_forward()

        if case == '/':
            if self.motion == CartDirections.RIGHT or self.motion == CartDirections.LEFT:
                self.turn_left()
            elif self.motion == CartDirections.DOWN or self.motion == CartDirections.UP:
                self.turn_right()
            self.move_forward()

        if case == '\\':
            if self.motion == CartDirections.RIGHT or self.motion == CartDirections.LEFT:
                self.turn_right()
            elif self.motion == CartDirections.DOWN or self.motion == CartDirections.UP:
                self.turn_left()
            self.move_forward()

        if case == '+':
            if self.curve == CartCurve.LEFT:
                self.turn_left()
            if self.curve == CartCurve.STRAIGHT:
                pass
            if self.curve == CartCurve.RIGHT:
                self.turn_right()
            self.new_curve()
            self.move_forward()

    def __str__(self):
        return "(col={0}, row={1}), {2} {3}".format(self.column, self.row, self.motion, self.curve)


class Grid:
    def __init__(self, file):
        with open(file) as f:
            data = f.read().splitlines()

        self.grid, self.carts = [], []

        for row, s in enumerate(data):
            for c in ['>', '<', '^', 'v']:
                p = s.find(c)
                while p > -1:
                    self.carts.append(Cart(row, p, c))
                    s = s[:p] + ('-' if c in ['>', '<'] else '|') + s[p + 1:]
                    p = s.find(c)

            self.grid.append(s)

    def __str__(self):
        result = self.grid.copy()

        for i, cart in enumerate(self.carts):
            if not cart.crashed:
                result[cart.row] = result[cart.row][:cart.column] + str(i) + result[cart.row][cart.column + 1:] if cart.column < len(result[cart.row]) else ''

        return '\n'.join(result)

    def next_crash(self):
        self.carts = sorted(self.carts, key=lambda cart: (cart.row, cart.column))
        crash, current_cart = False, -1

        while not crash:
            current_cart += 1

            if current_cart >= len(self.carts):
                self.carts = sorted(self.carts, key=lambda cart: (cart.row, cart.column))
                current_cart = 0

            counter = Counter(list(map(lambda c: (c.column, c.row), self.carts)))
            dups = [c for c in counter if counter[c] > 1]
            if len(dups):
                crash = True
                print('step1', dups[0])

            self.carts[current_cart].move(self.grid)

    def highlander_cart(self):
        while len([i for i in self.carts if not i.crashed]) > 1:
            self.carts.sort(key=lambda c: (c.row, c.column))
            for i, cart in enumerate(self.carts):
                if cart.crashed:
                    continue

                cart.move(self.grid)

                for j, comp in enumerate(self.carts):
                    if i != j and cart.column == comp.column and cart.row == comp.row and not comp.crashed:
                        cart.crashed = True
                        comp.crashed = True
                        break

                if cart.crashed:
                    continue

        cart = self.carts[0]
        print('step2', cart.column, cart.row)


grid = Grid('day13.input')
grid.next_crash()
grid = Grid('day13.input')
grid.highlander_cart()
