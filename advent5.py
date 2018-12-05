import pathlib  

input = pathlib.Path('./advent5.input').read_text().strip()

# step 1


def reaction(input):
  last_char = None
  for (i, c) in enumerate(input):
    if not last_char:
      last_char = last_char
    elif (last_char != c and last_char.lower() == c.lower()):
      test = input[:i-1] + input[i+1:]
      return test
    last_char = c 

  return input


def reaction_v2(input):
  c, remove = 2, []
  while c < len(input):
    if (input[c] != input[c-1] and input[c].lower() == input[c-1].lower()):
      remove.append(c)
      c += 2
    else:
      c += 1

  for i,c in reversed(list(enumerate(remove))):
    input = input[:c-1] + input[c+1:]

  return input


def length_reaction(input):
  result = reaction_v2(input)

  while result != input:
    input = result
    result = reaction_v2(input)

  return len(result)


print('result', length_reaction(input))

# step 2


def strip_chars(s, chars):
  for c in chars:
    s = s.replace(c, '')
  
  return s


counters = [(chr(c), length_reaction(strip_chars(input, [chr(c), chr(c+32)]))) for c in range(65, 91)]
min_length = sorted(counters, key = lambda kv:kv[1])[0]

print('min length is {0} by removing {1}'.format(min_length[1], min_length[0]))