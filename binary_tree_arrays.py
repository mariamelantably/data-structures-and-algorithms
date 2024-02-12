array = [[]*3]*20
next_free = 0
def insert(data, current_pointer = 0):
  global array, next_free
  if [data, None, None] not in array:
    array[next_free] = [data, None, None]
    next_free += 1
  if array[current_pointer][0] is None:
    array[current_pointer][0] = data
  else:
    if data < array[current_pointer][0]:
      if array[current_pointer][1] is not None:
        insert(data, array[current_pointer][1])
      else:
        array[current_pointer][1] = next_free - 1
    elif data > array[current_pointer][0]:
      if array[current_pointer][2] is not None:
        insert(data, array[current_pointer][2])
      else: 
        array[current_pointer][2] = next_free - 1
    else:
      return

def print_inorder_traversal(current_pointer = 0):
  global array
  if array[current_pointer][1] is not None:
    print_inorder_traversal(array[current_pointer][1])
  print(array[current_pointer][0])
  if array[current_pointer][2] is not None:
    print_inorder_traversal(array[current_pointer][2])

def print_preorder_traversal(current_pointer = 0):
  global array
  print(array[current_pointer][0])
  if array[current_pointer][1] is not None:
    print_preorder_traversal(array[current_pointer][1])
  if array[current_pointer][2] is not None:
    print_preorder_traversal(array[current_pointer][2])

def print_postorder_traversal(current_pointer = 0):
  global array
  if array[current_pointer][1] is not None:
    print_postorder_traversal(array[current_pointer][1])
  if array[current_pointer][2] is not None:
    print_postorder_traversal(array[current_pointer][2])
  print(array[current_pointer][0])


def search(target, current_pointer = 0):
  global array

  if array[current_pointer][0] == target:
    return True
  elif target < array[current_pointer][0] and array[current_pointer][1] is not None:
    return search(target, array[current_pointer][1])
  elif target > array[current_pointer][0] and array[current_pointer][2] is not None:
    return search(target, array[current_pointer][2])
  else:
    return False

def find_leaf_nodes():
  global array
  return_array = []
  for element in array:
    if element != [] and element[0] is not None and element[1] is None and element[2] is None:
        return_array.append(element[0])
  return return_array
  
insert(6)
insert(2)
insert(7)
insert(4)
insert(3)
insert(9)
insert(1)
insert(10)
insert(11)
insert(5)
print_inorder_traversal()
print(search(3))
print(search(8))