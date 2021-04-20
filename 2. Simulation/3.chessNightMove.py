import math
import sys
import time

from collections import Counter
from itertools import permutations, combinations, product, combinations_with_replacement


# ----------------------------------------------------------------------------------------
# 난이도 : 하 | 풀이시간 : 15분 | 시간제한 : 2초 | 메모리제한 : 128MB
# 문제 : 8 X 8 좌표 평면상에서 나이트가 이동할 수 있는 경우의 수 출력 (행: 1~8, 열 : a~h)
#       나이트는 L자 형태로만 움직임 가능 (수평2 수직1 or 수직2 수평1)
# 예시 : c2 >> 경우의 수 6
# 입력조건 : 첫째 줄에 8 X 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두문자로 구성된 문자열 (a1, c2 ..)
# 출력조건 : 나이트가 이동할 수 있는 경우의 수 출력
# 풀이 :
#   1. 입력받은 좌표 변환 (a > 1, b > 2 ... )
#   2. 나이트 이동방향 정의 (8방향)
#   3. 현재 좌표에서 움직임 가능 확인, move_count 증가
# ----------------------------------------------------------------------------------------

# 데이터 입력
xy = input()
row = int(xy[1])
col = int(ord(xy[0])) - int(ord('a')) + 1 # ASCII 코드로 문자를 숫자로 변환하여 좌표값 세팅

print(row, col)
# 시작시간
start_time = time.time()

# [알고리즘 시작] ----------------------------------------------------------------

# 나이트 이동 방향
steps = [(-2,-1), (-1,-2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
# print(steps)

# 현재 좌표에서 이동 가능한지 확인
move_count = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    # 해당 위치로 이동이 가능하다면
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        move_count += 1


print(move_count)

# [알고리즘 종료] ----------------------------------------------------------------

# 종료시간
end_time = time.time()
print("duration_time = ", end_time - start_time)
