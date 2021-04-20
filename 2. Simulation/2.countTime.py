import math
import sys
import time

from collections import Counter
from itertools import permutations, combinations, product, combinations_with_replacement


# ----------------------------------------------------------------------------------------
# 난이도 : 하 | 풀이시간 : 15분 | 시간제한 : 2초 | 메모리제한 : 128MB
# 문제 : 정수 N이 입력되면 00시 00분 00초 ~ N시 59분 59초 까지 모든 시각 숫자 중에서 3이 하나라도 포함되는 경우의 수
# 예시 : 00시 13분 30초 > 1건+
# 입력조건 : 첫째 줄에 정수 N  ( 1 <= N <= 23)
# 출력조건 : 00시 00분 00초 ~ N시 59분 59초 까지 모든 시각 숫자 중에서 3이 하나라도 포함되는 경우의 수 출력
# 풀이 :
#   1. 시, 분, 초 for
#   2. 3이 포함되어 있으면 count
# ----------------------------------------------------------------------------------------

# 데이터 입력
h = int(input())

# 시작시간
start_time = time.time()

# [알고리즘 시작] ----------------------------------------------------------------
count = 0

for i in range(0,h+1):
    for j in range(0,60):
        for k in range(0,60):
            if '3' in str(j) + str(j) + str(k):
                count +=1
print(count)

# [알고리즘 종료] ----------------------------------------------------------------

# 종료시간
end_time = time.time()
print("duration_time = ", end_time - start_time)