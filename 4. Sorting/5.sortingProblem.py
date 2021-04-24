"""
두 배열의 원소 교체 문제
난이도 : 하 | 풀이시간 : 15분 | 시간제한 : 2초 | 메모리제한 : 128MB
문제 : N 길이의 두 배열의 원소를 K번 바꿔치기 연산을 통해 배열 A의 모든 원소의 합의 최댓값을 출력

입력조건 :N, K 공백 기준으로 구분 입력  (1<= N <= 100,000, 0<=K<=N)
        배열A의 원소들이 공백을 기준으로 구분 입력 : 모든 원소는 10,000,000 보다 작은 자연수
        배열B의 원소들이 공백을 기준으로 구분 입력 : 모든 원소는 10,000,000 보다 작은 자연수
      
출력조건 : 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값 출력

예시 : 5 3
      1 2 5 4 3
      5 5 6 6 5
풀이 :
   1. N, K 입력
   2. 배열 A, 배열 B 입력
   3. 배열 A 오름차순 정렬
   4. 배열 B 내림차순 정렬
   5. 두 배열을 차례로 비교 (K번 반복)
      5-1. A원소가 B원소보다 작으면 : 두 원소 교체

"""

n, k = map(int, input().split())

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()
array_b.sort(reverse=True)

for i in range(k):
  if array_a[i] < array_b[i]:
    array_a[i], array_b[i] = array_b[i], array_a[i]

print(sum(array_a))
