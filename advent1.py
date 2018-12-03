import pathlib 
list_ints = [int (x) for x in pathlib.Path('./advent1.input').read_text().splitlines()]

# step 1
sum = 0
for i in list_ints:
  sum += i

print('step 1')
print(sum)

# star 2
f, c, found = 0, dict([]), False

def loop(frequency, counters):
  for i in list_ints:
    frequency += i
    if frequency not in counters:
      counters[frequency] = 1
    else:
      return frequency, True

  return frequency, False

while not found:
  f, found = loop(f, c)

print('step 2')
print(f)