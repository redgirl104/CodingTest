"""
피보나치 수(영어: Fibonacci numbers)
첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열

1 1 2 3 5 8 13 21 34 55 89

1) 단순 재귀함수 사용
  - 시간복잡도 : 지수시간 O(2^N)

2) 메모이제이션(Memoization) 방식
  - 다이나믹 프로그래밍 구현 방법 
  - 한번 계산한 결과를 메모리 공간에 메모 => 캐싱
  - 시간복잡도 : O(N)
  2-1) 탑다운(하향식)
  2-2) 보텀업(상향식) - DP 전형적인 형태
    결과 저장용 리스트 : DP테이블

3) 분할정복
  - DP와의 차이 : 부분 문제의 중복
  - 분할정복에서는 동일한 부분 문제가 반복적으로 계산되지 않음.
  - 대표적 예 : 퀵정렬 
    -> 기준원소(pivot)가 자리를 변경해서 기준이 확정되면 그 기준원소의 위치는 바뀌지 않음.
    -> 분할 이후 해당 피벗을 다시 처리하는 부분 문제는 호출하지 않음.
"""
import time

n = int(input())

start_time = time.time()

# 1) 단순 재귀함수
def fibo(num):
  if num <= 2:
    return 1
  sum = fibo(num-1) + fibo(num-2)
  return sum



# 2-1) 메모이제이션 : 탑다운
# 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀적으로 표현 (탑다운 DP)
def fiboDP_T(num):
  if num <= 2:
    return 1
  if d[num] != 0:
    return d[num]
  d[num] = fiboDP_T(num-1) + fiboDP_T(num-2)
  return d[num]


# 2-2) 메모이제이션 : 바텀업
def fiboDP_B(num):
  d[1] = 1
  d[2] = 1

  for i in range(3, num+1):
    d[i] = d[i -1] + d[i-2]
  return d[num]

print('fibo: ',fibo(n))
# print('fiboDP_T: ', fiboDP_T(n))
# print('fiboDP_B: ', fiboDP_B(n))

end_time = time.time()

print('duration time:', round(end_time - start_time, 2))