"""
1. Compare x with the middle element.
2. If x matches with middle element, we return the mid index.
3. Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
4. Else (x is smaller) recur for the left half.

"""

def binarySearch(array, start, end, x):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == x:
    return mid
  elif x > array[mid]:
    start = mid + 1
    return  binarySearch(array, start, end, x)
  else:
    end = mid - 1
    return binarySearch(array, start, end, x)
  


# input
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result == None:
  print("Can not found")
else:
  print(result+1)
