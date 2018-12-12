import pathlib


def prepare_data():
  state, rules = None, []

  for i,s in enumerate(pathlib.Path('./day12.input').read_text().splitlines()):
    if i == 0:
      state = s[15:]
    elif i > 1 and s[9] == '#':
      rules.append(s[:5])

  return {'input': state, 'rules': rules}


def evolution(initial_state, rules, time):
  result = ['...' + initial_state + '...']

  for t in range(time):
    current_state, new_state = result[-1], '..'

    for i in range(2, len(current_state)-2):
      s = current_state[i-2:i+3]
      new_state += '#' if (s in rules) else '.'

    result.append(new_state+ '...')

  return result


def sum_pot_number(days, time):
  index = []

  for i, c in enumerate(days[-1]):
    if c == '#':
      index.append(i - 3)
  return sum(index)


def step2(delay):
  # we search for a pattern in the evolution of the result
  step2start, diff, count, previous_solution = 20, 0, 1, 0
  while count < 100:
    days = evolution(data['input'], data['rules'], step2start)
    solution = sum_pot_number(days, step2start)
    if solution - previous_solution == diff:
      count+=1
    else:
      diff = solution - previous_solution
      count=1
    previous_solution = solution
    step2start += 1

  return solution + (delay - step2start + 1) * diff


data = prepare_data()
days = evolution(data['input'], data['rules'], 20)
print('step1', sum_pot_number(days, 20))
print('step2', step2(50000000000))