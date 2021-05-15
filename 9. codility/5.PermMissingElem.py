'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''

A = [2, 3, 1, 5, 6, 7]
# A = [1]

def solution(A):
  # A 리스트를 오름차순으로 정렬
  A.sort()
  miss_n = 0
  # 각 원소값과 인덱스를 비교 (각 원소값은 인덱스+1의 값과 같아야 함)
  for i in range(len(A)):
    # 처음으로 안맞는 원소가 찾아지면 miss_n에 값을 넣고 스톱
    if A[i] != i+1:
      miss_n = i+1
      break
  # miss_n을 찾았으면
  if miss_n != 0:
    return miss_n
  # 안맞는 원소가 없는 것은 가장 마지막 숫자(N+1)가 빠졌다는 뜻
  else:
    return len(A)+1
    

print(solution(A))
# 시간복잡도 : O(N) or O(NlogN)