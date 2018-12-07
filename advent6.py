import pathlib  
import re


# step 1


def prepare_data():
  line_pattern = re.compile(r"^(\d+), (\d+)$")
  input = pathlib.Path('./advent6.input').read_text().splitlines()

  result = []

  for s in input:
    data = line_pattern.match(s)
    result.append((int(data.group(1)), int(data.group(2))))

  return result


def prepare_grid(points):
  size = max(max(list(map(lambda a: a[0], points))) + 1, max(list(map(lambda a: a[1], points))) + 1)
  result = [['.' for y in range(size)] for x in range(size)]

  for i, point in enumerate(points):
    result[point[1]][point[0]] = 'P%02d' % i

  return result


def fill_grid(grid):
  for row, line_data in enumerate(grid):
    for line, case in enumerate(line_data):
      if case == '.':
        found, distance = [], 0
        while len(found) == 0:
          distance += 1
          for p in list_points(row, line, distance, len(grid) - 1):
            if grid[p[0]][p[1]][0] == 'P':
              t = grid[p[0]][p[1]]
              found.append(t)
        
        if len(found) > 1:
          grid[row][line] = '-'
        else:
          grid[row][line] = found[0][1:]
      
  return grid


def list_points(x, y, length, size_max):
  points = []
  for i in range(0, length + 1):
    points.append((x - i, y - length + i))
    points.append((x + i, y - length + i))
    points.append((x - i, y + length - i))
    points.append((x + i, y + length - i))

  points = [s for s in list(set(points)) if s[0] >= 0 and s[1] >= 0 and s[0] <= size_max and s[1] <= size_max]
  return points


def biggest_surface(grid):
  counters = {}
  for row, line_data in enumerate(grid):
    for line, case in enumerate(line_data):
      if case[0] == 'P':
        counters[case[1:]] = 1;
  
  for row, line_data in enumerate(grid):
    for line, case in enumerate(line_data):
      if case[0] != 'P' and case[0] != '-':
        counters[case] += 1;

  for row, line_data in enumerate(grid):
    if line_data[0][0] != 'P' and line_data[0][0] != '-':
      counters.pop(line_data[0], None)
    if line_data[len(line_data) - 1][0] != 'P' and line_data[len(line_data) - 1][0] != '-':
      counters.pop(line_data[len(line_data) - 1], None)

  for col, case in enumerate(grid[0]):
    if case[0] != 'P' and case[0] != '-':
      counters.pop(case, None)

  for col, case in enumerate(grid[len(grid) - 1]):
    if case[0] != 'P' and case[0] != '-':
      counters.pop(case, None)

  return max(counters.items(), key=(lambda key: key[1]))[1]


def display_data(s):
  if s == '.':
     return '....'
  if s[0] == 'P':
    return '[%02d]' % (int(s[1:]))
  if s == '-':
    return '----'
    
  return ' %02d ' % int(s)


def display_grid(grid):
  for s in grid:
    print(' '.join(list(map(lambda i: display_data(i), (s)))))


file = prepare_data()
grid = fill_grid(prepare_grid(file))
surface = biggest_surface(grid)
# display_grid(grid)
print('biggest surface', surface)

def region_sum(max):
  count, result = 0, [['.' for y in range(len(grid))] for x in range(len(grid))]

  for row, line_result in enumerate(result):
    for line, case in enumerate(line_result):
      sum = 0
      for p in file:
        sum += (abs(row-p[1]) + abs(line-p[0]))

      if sum < max:
        result[row][line] = '00'
        count += 1

  return count

print('region size step 2', region_sum(10000))