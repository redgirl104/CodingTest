"""
병사 배치하기
- n명의 병사 무작위 나열
- 값이 큰 (전투력이 높은) 병사가 앞쪽에 오도록 내림차순 배치
- 배치 과정에는 특정한 위치에 있는 병사를 열외시키는 방법 이용
- 남아 있는 병사의 수가 최대가 되도록


난이도 : 중하 | 풀이시간 : 40분 | 시간제한 : 1초 | 메모리제한 : 256MB
문제 : 남아 있는 최대 병사의 수

입력조건 : n (병사수) (1 <= N <= 2000)
          각 병사의 전투력 배열  (1 <= M <= 10,000,000)
          
          
출력조건 : 남아 있는 병사가 최대가 되게 하는 열외시킨 병사의 수

예시 :7 
      15 11 4 8 5 2 4
출력 : 2

풀이 : 

LIS (Longest Incresing Subsequence)
가장 긴 증가하는 부분 수열
D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이

모든 0 <= j < i 에 대하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]
"""

n = int(input())
array = list(map(int, input().split()))

array.reverse()

# DP 테이블 초기화
d = [1] * n

# LIS 알고리즘 수행
for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]:
      d[i] = max(d[i], d[j] +1)


print(n - max(d))
