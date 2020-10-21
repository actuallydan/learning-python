import random

# create a test array
def createList(array, length):
  for i in range(length):
    array.append(random.randint(1, 1000))
  return array



def binarySearch(target, array):

  # if its stupid but works it ain't stupid
  if(array[0] == target):
    return 0

  # get the last index
  max = len(array)
  min = 0

  # set a cursor to midpoint
  # use // to use integer division (floor division?)
  cursor = (max - min) // 2

  retval = -1
  
  while (max != min):
    if (array[cursor] == target):
      retval = cursor
      break

    elif (array[cursor] < target):
      # increase min to cursor
      min = cursor 
      cursor += (max - min) // 2
        
    elif (array[cursor] > target):
      # decrease max to cursor
      max = cursor 
      cursor -= (max - min) // 2

  return retval


# example mergeSort replace with own later ?
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

# setup 

testArr = createList([], 10000)
# print(testArr)

tar = testArr[3887]
print(tar)
sortedArr = testArr.copy()

# sort array
mergeSort(sortedArr)
# print(sortedArr)

res = binarySearch(tar, sortedArr)  
print(res)


# res = binarySearch(1, [1, 2, 3, 4, 5, 9, 55, 210])
# print(res)