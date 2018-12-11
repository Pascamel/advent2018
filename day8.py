import pathlib  

def prepare_data():
  text = pathlib.Path('./day8.input').read_text().split()
  result = list(map(lambda a: int(a), text))
 
  return result


# step 1


def structure_data(list):
  data = extract_node(list[0], list[1], list[2:])
  return (data[0], data[1])


def extract_node(children, metadata, array_data):
  kids, data = [], []

  while children > 0:
    tmp = extract_node(array_data[0], array_data[1], array_data[2:])
    kids.append((tmp[0], tmp[1]))
    children -= 1
    array_data = tmp[2]
  
  if metadata > 0:
    data = array_data[:metadata]
    del array_data[:metadata] 
  
  return (kids, data, array_data)
  

def sum_metadata(data):
  return sum(data[1]) + sum(list(map(lambda v: sum_metadata(v), data[0])))


# step 2

def score_node(data):
  if len(data[0]) == 0:
    return sum(data[1])
  else:
    s = 0
    for v in data[1]:
      if len(data[0]) >= v:
        s += score_node(data[0][v-1])
    return s


prepared_data = prepare_data()
structured_data = structure_data(prepared_data)

print('step 1', sum_metadata(structured_data))
print('step 2', score_node(structured_data))
