import pathlib 
from datetime import date, time, timedelta

input = [x for x in pathlib.Path('./advent4.input').read_text().splitlines()]
input.sort()

# preparing records

def prepare_records(input):
  current_date = None
  current_guard = None
  current_schedule = None
  sleep_start = None
  records = []

  for s in input:
    timestamp, action = s.replace('[', '').split('] ')
    # print('action', action)
    if action.endswith('begins shift'):

      if current_guard:
        records.append({
          'date': current_date.strftime('%m-%d'),
          'guard': current_guard, 
          'schedule': current_schedule
        })

      current_schedule = '.' * 60
      current_guard = int(action[action.index('#')+1:action.index(' ', action.index('#'))])

      dt, tm = timestamp.split(' ')
      y, m, d = [int(s) for s in dt.split('-')]
      
      current_date = date(y, m, d)
      if int(tm.split(':')[0]) == 23:
        current_date += timedelta(days=1)

    elif action == 'falls asleep':
      sleep_start = int(timestamp.split(':')[1])

    elif action == 'wakes up':
      sleep_ends = int(timestamp.split(':')[1])
      current_schedule = current_schedule[0:sleep_start] + '#' * ( sleep_ends - sleep_start) + current_schedule[sleep_ends:]

  records.append({
    'date': current_date.strftime('%m-%d'),
    'guard': current_guard, 
    'schedule': current_schedule
  })

  return records

# who is the guard that has the most minutes asleep?

def sleepiest_guard(records):
  total_minutes = {}
  for record in records:
    if record['guard'] not in total_minutes:
      total_minutes[record['guard']] = 0
    for sleepy in enumerate(record['schedule']):
      if sleepy == '#':
        total_minutes[s['guard']] += 1
    
  return sorted(total_minutes.items(), key = lambda kv:-kv[1])[0][0]

# which minute is a guard the most likely to be asleep?

def sleepiest_minute(records, guard):
  minute_counters = [0] * 60
  for record in [s for s in records if s['guard'] == guard]:
    for minute, sleepy in enumerate(record['schedule']):
      if sleepy == '#':
        minute_counters[minute] += 1

  sleepiest_minute = None
  sleepiest_count = 0
  for idx, sleepy in enumerate(minute_counters):
    if sleepiest_minute is None or sleepiest_count < sleepy:
      sleepiest_minute = idx
      sleepiest_count = sleepy

  return sleepiest_minute

# final result step 1

records = prepare_records(input)
guard = sleepiest_guard(records)
minute = sleepiest_minute(records, guard)

print('sleepier guard', guard)
print('sleepiest_minute', minute)
print('result', guard * minute)

# counters for all guards

def sleepiest_minute_guard(records):
  total_minutes = {}
  for record in records:
    if record['guard'] not in total_minutes:
      total_minutes[record['guard']] = [0] * 60
    for minute, state in enumerate(record['schedule']):
      if state == '#':
        total_minutes[record['guard']][minute] += 1
  
  result_guard = None
  result_count = None
  result_minute = None

  for guard in total_minutes:
    for minute, count in enumerate(total_minutes[guard]):
      if (result_guard is None or count > result_count):
        result_guard = guard
        result_count = count
        result_minute = minute

  return {'guard': result_guard, 'minute': result_minute}
  
# step 2

step2 = sleepiest_minute_guard(records)
print('sleepiest_minute_guard', step2)
print('sleepiest_minute_guard', step2['guard'] * step2['minute'])