'''
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

# A = [1, 3, 6, 4, 1, 2]
A = [1, 2, 3]
# A = [-1, -3]

# O(N) or O(N * log(N))
def solution(A):
  set_int = {i for i in range(1,max(A)+2)}
  # print(set_int)
  for i, a in enumerate(A):
    if a in set_int:
      set_int.remove(a)

  if set_int:
    return set_int.pop()
  else:
    return 1

print(solution(A))