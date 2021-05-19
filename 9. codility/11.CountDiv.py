'''
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
'''
A = 11
B = 14
K = 2

# 실행 불가. - 시간복잡도!!
def solution2(A, B, K):
  set_cnt = {0}
  for i in range(A, B+1):
    if i % K == 0:
      set_cnt.add(i)
  if set_cnt:
    return len(set_cnt)-1

# O(1)
# B까지 K로 나누어 떨어지는 수 - A까지 K로 나누어 떨어지는 수
def solution(A, B, K):
  if (A % K == 0):
    return (B // K ) - (A // K) + 1
  else:
    return (B // K ) - (A // K)



print(solution(A, B, K))