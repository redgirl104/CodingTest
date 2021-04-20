import math
import sys
import time

from collections import Counter
from itertools import permutations, combinations, product, combinations_with_replacement


# ----------------------------------------------------------------------------------------
# 난이도 : 하 | 풀이시간 : 30분 | 시간제한 : 1초 | 메모리제한 : 128MB
# 문제 : 각 자리가 숫자(0~9)로만 이루어진 문자열 S에서, 왼쪽부터 오른쪽까지 x or + 연산처리해서 가장 큰 수 구하려함
#       모든 연산은 왼쪽에서부터 순서대로 이루어짐
# 예시 : S = 02984 >> ((((0+2)X9)X8)X4) = 576
# 입력조건 : 첫째 줄에 모험가 수 N ( 1 <= N <= 100,000)
#           둘째 줄에 각 모험가의 공포토 값을 N 이하의 자연수, 각 자연수는 공백으로 구분
# 출력조건 : 여행을 떠날 수 있는 그룹 수의 최댓값 출력
# 풀이 :
#   1. 공포도 X 역순으로 N 리스트 정렬
#   2. 리스트 첫번째 원소의 값 만큼 리스트에서 원소 삭제 (그룹수 + 1 )
#   3. 리스트 원소가 남지 않을 때 까지 반복
# ----------------------------------------------------------------------------------------

# 데이터 입력
n = int(input())
data = list(map(int, input().split()))

# 시작시간
start_time = time.time()

# [알고리즘 시작 - 최대 그룹 수] ----------------------------------------------------------------
data.sort()
# 현재그룹 모험가 수
count_n = 0
# 그룹 수
max_group = 0

for i in data: # 공포도를 낮은 것부터 하나씩 확인해 가며
    count_n += 1 # 현재 그룹에 해당 모험가를 추가시키고
    if count_n >= i: # 현재 그룹에 포함된 모험가 수가, 현재 확인중인 공포도 이상이면
        max_group += 1 # 새로운 그룹 만들고
        count_n = 0 # 새로 만든 그룹에 포함된 모험가 수를 초기화

print(data)
print("max_group :", max_group)

# [알고리즘 시작 - 최소 그룹 수] ----------------------------------------------------------------
data.sort(reverse=True)
# 한 그룹에 포함되는 최대 모험가 수 초기화
max_count = data[0]
# 현재그룹 모험가 수
count_n = 0
# 그룹 수
min_group = 0

for i in data:
    if count_n == 0: # 모험가 수가 초기화 되었으면
        max_count = i # 현재 공포도를 세팅

    count_n += 1
    if count_n == max_count : # 현재 그룹에 포함된 모험가 수가, 처음 그룹핑 기준이된 공포도 숫자보다 크면
        min_group += 1 # 그룹을 추가하고
        count_n = 0 # 모험가 수를 초기화한다


print(data)
print("min_group :", min_group)


# [알고리즘 종료] ----------------------------------------------------------------

# 종료시간
end_time = time.time()
print("duration_time = ", end_time - start_time)