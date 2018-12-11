import pathlib  
import re


# step 1


def prepare_data():
  line_pattern = re.compile(r"^Step (\w+) must be finished before step (\w+) can begin.")
  input = pathlib.Path('./advent7.input').read_text().splitlines()

  result = {}

  for s in input:
    data = line_pattern.match(s)
    if data.group(1) not in result:
      result[data.group(1)] = []
    if data.group(2) not in result:
      result[data.group(2)] = []
    result[data.group(1)].append(data.group(2))

  return result


def available_tasks(tasks):
  result = list(tasks.keys())
  for value in tasks.values():
    for v in value:
      if v in result:
        result.remove(v)

  result.sort()
  return result


def list_execution(tasks):
  result = ''
  while len(tasks.keys()):
    available = available_tasks(tasks)

    v = available[0]
    result += v

    tasks.pop(v)
    for value in tasks.values():
      if v in value:
        value.pop(v)
  
  return result


tasks = prepare_data()
tasks_execution = list_execution(tasks)    

print('execution order', tasks_execution)


# step 2


def time_needed(task, base):
  result = ord(task) - 64 + base  #base=0 for sample, 60 for real input
  return result


def complete_tasks(tasks, max_workers, base):
  time, workers = -1, []

  while len(tasks.keys()):
    time += 1
    new_workers = []
    for worker in workers:
      if worker[1] > 1:
        new_workers.append((worker[0], worker[1] - 1))
      else:
        v = worker[0]
        tasks.pop(v)
        for value in tasks.values():
          if v in value:
            value.pop(v)
    
    workers = new_workers 
    available = available_tasks(tasks)
    
    for a in available:
      found = False

      for worker in workers:
        if worker[0] == a:
          found = True

      if not found and len(workers) < max_workers:
        workers.append((a, time_needed(a, base)))
  
  return time


tasks = prepare_data()
time = complete_tasks(tasks, 5, 60)

print('time needed', time)