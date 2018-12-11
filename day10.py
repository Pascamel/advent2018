import pathlib, re  


def prepare_data():
  result = []

  for s in pathlib.Path('./day10.input').read_text().splitlines():
    data = re.findall(r'[0-9-]+', s)
    result.append({
      'position': [int(data[0]), int(data[1])],
      'velocity': [int(data[2]), int(data[3])]
    })
 
  return result


def dots_sizes(data):
  sizes = []
  for t in range(20000):
    min_x, max_x, min_y, max_y = None, None, None, None
    for d in data:
      p = (d['position'][0] + t * d['velocity'][0], d['position'][1] + t * d['velocity'][1])
  
      if (min_x is None) or (p[0] < min_x):
        min_x = p[0]
      if (max_x is None) or max_x < p[0]:
        max_x = p[0]

      if min_y is None or p[1] < min_y:
        min_y = p[1]
      if max_y is None or max_y < p[1]:
        max_y = p[1]
    
    sizes.append((max_x - min_x) * (max_y - min_y))

  return sizes


def print_at_timestamp(data, t):
  min_x, max_x, min_y, max_y = None, None, None, None
  for d in data:
    p = (d['position'][0] + t * d['velocity'][0], d['position'][1] + t * d['velocity'][1])

    if (min_x is None) or (p[0] < min_x):
      min_x = p[0]
    if (max_x is None) or max_x < p[0]:
      max_x = p[0]

    if min_y is None or p[1] < min_y:
      min_y = p[1]
    if max_y is None or max_y < p[1]:
      max_y = p[1]

  grid = [['.' for col in range(max_x - min_x + 1)] for row in range(max_y - min_y + 1)]

  for d in data:
    p = (
      d['position'][0] + t * d['velocity'][0] - min_x, 
      d['position'][1] + t * d['velocity'][1] - min_y
      )
    grid[p[1]][p[0]] = '#'

  for row in grid:
    print(''.join(row))


# both steps
data = prepare_data()
sizes = dots_sizes(data)
min_value = min(sizes)
timestamp = sizes.index(min(sizes))

print('smallest size', min_value)
print('index sm size', timestamp)

print_at_timestamp(data, timestamp)