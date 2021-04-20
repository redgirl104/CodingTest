
import math
import sys
import time

from collections import Counter
from itertools import permutations, combinations, product, combinations_with_replacement

# ----------------------------------------------------------------------------------------
# 난이도 : 하 | 풀이시간 : 15분 | 시간제한 : 2초 | 메모리제한 : 128MB
# 문제 : 알파벳 대문자와 숫자(0~9)로만 구성된 문자열 입력, 모든 알파벳 오름차순 정렬, 그 뒤에 모든 숫자 합
# 예시 : K1KA5CB7 >> ABCKK13
# 입력조건 : 알파벳 대문자와 숫자(0~9)로만 구성된 문자열 (1 <= S의 길이 <= 10,000)
# 출력조건 : 모든 알파벳 오름차순 정렬, 그 뒤에 모든 숫자 합
# 풀이 :
#   1. 입력 문자열 iteration, 문자/숫자 체크
#   2. 문자면 문자열 리스트에 저장, 정렬
#   3. 숫자면 sum
#   4. 문자열 + str(숫자sum)
# ----------------------------------------------------------------------------------------

# 데이터 입력
data = input()

# 시작시간
start_time = time.time()

# [알고리즘 시작] ----------------------------------------------------------------

characters = []
sum = 0

for c in data:
    if c.isalpha(): # int(ord(c)) > 64
        # print(int(ord(c)))
        characters.append(c)
    else:
    # elif 49 <= int(ord(c)) <= 65:
        sum += int(c)

# 알파벳을 오름차순으로 정렬
characters.sort()

# 숫자가 하나라도 존재하는 경우
if sum != 0:
    characters.append(str(sum))

# 최종결과 출력 (리스트를 문자열로)
print(''.join(characters))

# [알고리즘 종료] ----------------------------------------------------------------

# 종료시간
end_time = time.time()
print("duration_time = ", end_time - start_time)