import math
import sys
import time

from collections import Counter
from itertools import permutations, combinations, product, combinations_with_replacement


# ----------------------------------------------------------------------------------------
# 난이도 : 하 | 풀이시간 : 15분 | 시간제한 : 2초 | 메모리제한 : 128MB
# 문제 : 어떠한 수 N이 1이 될 때 까지 다음 두 과정 중 하나를 반복 수행. 단, 두번째 연산은 N이 K로 나누어 떨어질때만 가능
#     1. N에서 1을 뺀다
#     2. N을 K로 나눈다
# 예시 : N = 17, K=4 라고 가정. 1번 (N=16) -> 2번 (N=4) -> 2번 (N=1) : 총 3번 수행
# 입력조건 : 첫째 줄에 N(1<= N <= 100,000) 과 K (2<= k <= 100,000)가 공백을 기준으로 각각 자연수
# 출력조건 : 첫째 줄에 N이 1이 될 때 까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값 출력
# 풀이 : 아래와 같이 풀면 N이 엄청 큰 수일 경우에도 시간 복잡도는 급격히 줄어듦 (log N)
# ----------------------------------------------------------------------------------------

# 데이터 입력 (n, k)
n, k = map(int, input().split())

# 시작시간
start_time = time.time()

# 수행 횟수
result = 0

while True:
    # target : 최대로 나눌 수 있는 몫 (1을 빼기까지 가장 가깝게 나누어 떨어지는 수를 찾자)
    target = (n // k) * k
    # N이 K로 나누어 떨어지는 수가 될 때 까지 빼기 (1을 빼는 연산 수를 한번에 result에 넣어둠)
    result += (n - target)
    n = target

    # N이 K보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # K로 나누기 (K로 나눈 연산 횟수 1을 result에 더해줌)
    result += 1
    n //= k

# 마지막으로 남은 수에 대해 1씩 빼기
result += (n-1)
print(f'연산 수행 횟수 : {result}')

# 종료시간
end_time = time.time()
print("duration_time = ", end_time - start_time)