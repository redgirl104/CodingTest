
import math
import sys
import time

from collections import Counter
from itertools import permutations, combinations, product, combinations_with_replacement

# ----------------------------------------------------------------------------------------
# 난이도 : 하 | 풀이시간 : 15분 | 시간제한 : 2초 | 메모리제한 : 128MB
# 문제 : 입력받은 정수를 바이너리로 변환하였을 때 1과 1사이의 0 숫자를 카운트하여 큰 수 반환
# 예시 : 9 >> 1001 : 2 리턴, 529 > 1000010001  : 4 리턴
# 입력조건 : positive integer N (1 <= N <= 2,147,483,647)
# 출력조건 : longest binary gap
# 풀이 :
#   1. 입력 숫자를 바이너리 변환
#   2. 왼쪽부터 1, 0 체크 > 다음 1이 나올때 까지 0 카운트
#   3. logest_gap 비교, 갱신
# ----------------------------------------------------------------------------------------

# 데이터 입력
n = int(input())

# 시작시간
start_time = time.time()

# [알고리즘 시작] ----------------------------------------------------------------
# 바이너리 변환 : bin(n) 을 사용하면 앞에 접두어 '0b' 가 붙음 > format을 사용하자 (실제 바이너리 수가 아닌 보이는 형태만 바이너리임)
binary_n = format(n, 'b')
print(binary_n)
longest_gap = 0
zero_sum = 0


zeros = binary_n.split('1')

# 마지막 자리가 '0'면 zeros list에서 제일 마지막 zero_count를 제거한다
if binary_n[-1] == '0':
    del zeros[-1]

for zero in zeros:
    zero_sum = len(zero)
    print(zero)
    if zero_sum > longest_gap:
        longest_gap = zero_sum

print(longest_gap)
# [알고리즘 종료] ----------------------------------------------------------------

# 종료시간
end_time = time.time()
print("duration_time = ", end_time - start_time)