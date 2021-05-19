'''
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

개구리는 잎이 1에서 X까지 강 건너 모든 위치에 나타날 때만 건널 수 있습니다 (즉, 1에서 X까지의 모든 위치가 잎으로 덮여있는 가장 빠른 순간을 찾고 싶습니다)

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
'''

A = [1, 3, 1, 4, 2, 3, 5, 4]
# A = [3]
# A = [2, 2, 2, 2, 2]
X = 5

def solution(X, A): 
  arr_p = [0] * (X)
  arr_sum = 0
  for i in range(len(A)):
    if arr_p[A[i]-1] == 0:
      # print(A[i])
      arr_p[A[i]-1] = 1
      # print(arr_p)
      arr_sum += 1
      if arr_sum == X:
        return i
        print('idx', idx)
        break
  return -1

print(solution(X, A))