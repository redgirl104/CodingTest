'''
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
'''

# A = [4, 1, 3, 2]
# A = [4, 1, 3]
A = [1, 1] # 연속된 숫자가 나와도 Fail

# O(N) or O(N * log(N))
def solution(A):
  set_int = {0}
  max_int = 0
  dup_cnt = 0
  for a in A:
    if a in set_int:
      dup_cnt += 1
    else:
      set_int.add(a)

    if a > max_int:
      max_int = a
  # set의 사이즈가 max_int보다 작으면 연속된 수가 아님 (set의 초기값 0 제외)
  if (len(set_int)-1 < max_int) or dup_cnt > 0:
    return 0
  else:
    return 1


print(solution(A))