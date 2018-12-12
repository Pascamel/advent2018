def fill_grid(serial_number, size):
  grid = [[0 for col in range(size)] for row in range(size)]

  for y, row in enumerate(grid):
    for x, cell in enumerate(row):
      v = x + 11
      v *= y + 1
      v += serial_number
      v *= (x + 11)

      row[x] = int(str(v)[-3]) - 5

  return grid


def biggest_value(grid, size, size_min, size_max):
  total, sz, coords = None, None, None

  for i in range(size_min, size_max+1):
    for y, row in enumerate(grid[:size-i+1]):
      for x, cell in enumerate(row[:size-i+1]):
        s = 0
        for n in range(0, i):
          s += sum(grid[x+n][y:y+i])

        if total is None or s > total:
          total = s
          sz = i
          coords = (y+1, x+1)

  return (coords[0], coords[1], sz, total)


serial_number = 2866
size = 300
grid = fill_grid(serial_number, size)

step1 = biggest_value(grid, size, 3, 3)
print('step1', '{0[0]},{0[1]} (total is {0[3]})'.format(step1))

step2 = biggest_value(grid, size, 1, 300)
print('step2', '{0[0]},{0[1]},{0[2]} (total is {0[3]})'.format(step2))
