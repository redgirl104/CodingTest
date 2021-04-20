
import math
import sys
import time

from collections import Counter
from itertools import permutations, combinations, product, combinations_with_replacement

# ----------------------------------------------------------------------------------------
# 난이도 : 중하 | 풀이시간 : 30분 | 시간제한 : 1초 | 메모리제한 : 128MB
# 문제 : N X M 크기의 얼음틀, 구멍 뚤린부분 0, 칸막이 부분 1 -> 0 으로 이어진 덩어리 개수 세기
# 예시 : 다음과 같은 4 X 5 배열에서는 총 3개의 덩어리가 생성됨
# 00110 [
# 00011
# 11111
# 00000
# 입력조건 :첫번째 줄에 얼음틀의 세로 길이 N, 가로길이 M (1 <= N, M <= 1,000)
#          둘째 줄부터 N+1번째 줄 까지 얼음틀 형태가 주어짐
# 출력조건 : 한번에 만들 수 있는 아이스크림 개수 출력
# 풀이 :
#   1. 데이터 입력
#   2. 모든 노드를 방문하면서
#   3. DFS 알고리즘
# ----------------------------------------------------------------------------------------

# 데이터 입력
n, m = map(int, input().split())
# 얼음틀 입력 (2차원 리스트)
ice_frame = []
for i in range(n):
    ice_frame.append(list(map(int, input())))
print(ice_frame)
# 시작시간
start_time = time.time()

# [알고리즘 시작] ----------------------------------------------------------------
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았으면
    if ice_frame[x][y] == 0:
        # 해당 노드를 방문 처리하고
        ice_frame[x][y] = 1
        # 상, 하, 좌, 우의 위치를 재귀적으로 호출
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False

# 모든 노드(위치)에 대해 음료수 채우기
ice_count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            ice_count += 1

print(ice_count)
# [알고리즘 종료] ----------------------------------------------------------------

# 종료시간
end_time = time.time()
print("duration_time = ", end_time - start_time)