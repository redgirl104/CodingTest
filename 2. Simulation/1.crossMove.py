import math
import sys
import time

from collections import Counter
from itertools import permutations, combinations, product, combinations_with_replacement


# ----------------------------------------------------------------------------------------
# 난이도 : 하 | 풀이시간 : 15분 | 시간제한 : 2초 | 메모리제한 : 128MB
# 문제 : N X N 크기의 정사각형 공간 내, 가장 왼쪽 위 좌표 (1,1), 가장 오른쪽 아래 (N, N)
#       상, 하, 좌, 우 방향으로 이동. 시작 좌표는 항상 (1,1)
# 예시 : L, R, U, D (공간 밖은 무시)
# 입력조건 : 첫째 줄에 이차원 공간 N  ( 1 <= N <= 100)
#           둘째 줄에 각 모험가의 이동 계획서 ( 1 <= 이동횟수 <= 100)
# 출력조건 : 첫째 줄에 여행가가 최종적으로 도착할 지점 좌표 (X, Y)를 공백 기준으로 구분 출력
# 풀이 :
#   1. 초기 좌표 설정
#   2. L, R, U, D 방향 이동 설정
#   3. 입력받은 방향에 따라 좌표 이동
# ----------------------------------------------------------------------------------------

# 데이터 입력
n = int(input())
plans = list(map(str, input().split()))

# 시작시간
start_time = time.time()

# [알고리즘 시작] ----------------------------------------------------------------
x, y = 1, 1

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 실제 이동 수행
    x, y = nx, ny

print(x, y)


# [알고리즘 종료] ----------------------------------------------------------------

# 종료시간
end_time = time.time()
print("duration_time = ", end_time - start_time)