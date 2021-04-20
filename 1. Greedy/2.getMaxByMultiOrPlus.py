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
# 입력조건 : 첫째 줄에 여러개의 숫자로 구성된 문자열 S (1<= S길이 <= 20)
# 출력조건 : 첫째 줄에 만들어질 수 있는 가장 큰 수
# 풀이 :
#   1. 첫 번째 문자를 숫자로 변경하여 대입
#   2. 두 번째 문자부터 가져와서, 두 수 중에 하나라도 '0' 혹은 '1'인 경우, 더하기 수행
#   3. 아닐 경우에는 곱하기 연산
# ----------------------------------------------------------------------------------------

data = input()

# 시작시간
start_time = time.time()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에 하나라도 '0' 혹은 '1'인 경우, 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)



# 종료시간
end_time = time.time()
print("duration_time = ", end_time - start_time)