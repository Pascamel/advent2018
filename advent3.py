import pathlib 
input = [x for x in pathlib.Path('./advent3.input').read_text().splitlines()]

# formatting

def format_input(s):
  s = s.replace(': ', 'x').replace(' @ ', 'x').replace('#', '').replace(' @ ', 'x').replace(',', 'x')
  r = {}
  (r['id'], r['start_x'], r['start_y'], r['size_x'], r['size_y']) = [int(i) for i in s.split('x')]

  return r

# step 1

area = [[0 for col in range(1000)] for row in range(1000)]

for s in [format_input(s) for s in input]:
  for x in range(s['start_x'], s['start_x'] + s['size_x']):
    for y in range(s['start_y'], s['start_y'] + s['size_y']):
      if area[x][y] == 0:
        area[x][y] = s['id']
      else:
        area[x][y] = -1

count = 0
for x in area:
  for y in x:
    if y == -1:
      count += 1

print('overlays', count)

# step 2

for s in [format_input(s) for s in input]:
  intact = True

  for x in range(s['start_x'], s['start_x'] + s['size_x']):
    for y in range(s['start_y'], s['start_y'] + s['size_y']):
      intact = intact and area[x][y] == s['id']

  if intact:
    print('intact', s['id'])
