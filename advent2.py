import pathlib 
input = [x for x in pathlib.Path('./advent2.input').read_text().splitlines()]

# star 1
c2, c3 = 0, 0

for s in input:
  f2, f3, counters = False, False, dict([])
  for c in s:
    if c not in counters:
      counters[c] = 0
    counters[c] += 1

  for count in counters:
    if counters[count] == 2: 
      f2 = True
    if counters[count] == 3: 
      f3 = True
    if f2 and f3:
      break;

  if f2:
    c2 += 1
  if f3:
    c3 += 1

print('checksum', c2 * c3)

# step 2
def pick_common(s1, s2):
  s = []
  for c1, c2 in zip(s1, s2):
    if c1 == c2:
      s += c1
  return ''.join(s)

def loop_boxes():
  for s1 in input:
    for s2 in [s for s in input if s1 != s]:
      c = pick_common(s1, s2)
      if len(s1) - len(c) == 1:
        return c;

  return 'Not found';

print('label', loop_boxes())