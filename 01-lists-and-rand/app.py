import random

def createList(array, length):
  for i in range(length):
    array.append(random.randint(1, 1000))
  return array

arr = createList([], 10)

print(arr)
