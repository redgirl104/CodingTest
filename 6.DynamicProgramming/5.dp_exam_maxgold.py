"""
채굴 가능한 최대 금의 크기
- n x m 크기 금광
- 첫 번째 열의 어느 행에서든 출발 가능
- 오른쪽 위, 오른쪽, 오른쪽 아래 만 이동가능


난이도 : 중하 | 풀이시간 : 30분 | 시간제한 : 1초 | 메모리제한 : 128MB
문제 : 채굴 가능한 최대 금의 크기

입력조건 : 테스트 케이스 T (1 <= T <= 1000)
          n, m 금광 크기 공백으로 입력(2차원)  (1<= N,   M <= 20)
          각 행열의 금의 개수를 공백으로 구분 입력 (1<= 각 위치에 매장된 금의 개수 <= 100)
          
출력조건 : 테스트 케이스마다의 금 최대 크기 (줄바꿈)

예시 :2 
      3 4
      1 3 3 2 2 1 4 1 0 6 4 7
      4 4 
      1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
출력 : 19
      16

풀이 : 

dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
"""


for tc in range(int(input())):
  n, m = map(int, input().split())
  array = list(map(int, input().split()))

  # DP 위한 2차원 DP테이블 초기화
  dp = []
  index = 0
  for i in range(n):
    dp.append(array[index:index + m])
    index += m

  # DP 진행
  for j in range(1, m):
    for i in range(n):
      #왼쪽 위에서 오는 경우
      if i == 0: left_up = 0 # out of index 방지
      else: left_up = dp[i-1][j-1]
      #왼쪽 아래서 오는 경우
      if i == n-1: left_down = 0
      else: left_down = dp[i+1][j-1]
      #왼쪽에서 오는 경우
      left = dp[i][j-1]
      dp[i][j] = dp[i][j] + max(left_up, left_down, left)
  result=0
  for i in range(n):
    result = max(result, dp[i][m-1])
  print(result)