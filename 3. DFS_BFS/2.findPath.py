
import math
import sys
import time

from collections import Counter
from itertools import permutations, combinations, product, combinations_with_replacement

# ----------------------------------------------------------------------------------------
# 난이도 : 중하 | 풀이시간 : 30분 | 시간제한 : 1초 | 메모리제한 : 128MB
# 문제 : N X M 크기의 미로, 괴물있는 부분 0, 없는 부분 1 -> 1로 이어지는 최단경로 찾기
# 예시 : 다음과 같은 5 X 6 배열
# 101010
# 111111
# 000001
# 111111
# 111111
# 입력조건 :첫번째 줄에 두 정수 N, M (4 <= N, M <= 200)
#          둘째 줄부터 N+1번째 줄 까지 미로의 형태가 주어짐
# 출력조건 : 최소 이동칸의 개수 출력
# 풀이 :
#   1. 데이터 입력
#   2. 모든 노드를 방문하면서
#   3. BFS 알고리즘을 수행, 1 : 연결된 노드를 찾으면서 move_count 1씩 증가
# ----------------------------------------------------------------------------------------

# 데이터 입력
n, m = map(int, input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 시작시간
start_time = time.time()

# [알고리즘 시작] ----------------------------------------------------------------
def bfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았으면
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리하고
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치를 재귀적으로 호출
        bfs(x, y-1)
        bfs(x, y+1)
        bfs(x-1, y)
        bfs(x+1, y)
        return True
    return False

# 모든 노드(위치)에 대해 방문
move_count = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            move_count += 1

print(move_count)
# [알고리즘 종료] ----------------------------------------------------------------

# 종료시간
end_time = time.time()
print("duration_time = ", end_time - start_time)