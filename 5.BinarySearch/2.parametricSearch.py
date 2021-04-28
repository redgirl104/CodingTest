"""
파라메트릭 서치
  - 최적화 문제를 Yes/No 문제로 바꾸어 해결하는 기법

난이도 : 중 | 풀이시간 : 40분 | 시간제한 : 2초 | 메모리제한 : 128MB
문제 : 절단기로 길이가 각기 다른 떡을 자름. 적어도 M 만큼의 떡을 얻기 위해 잘라야 하는 높이의 최댓값

입력조건 :떡의 개수 N, 요청한 떡의 길이 M 공백 기준으로 구분 입력  
          (1<= N <= 1,000,000, 1<=M<=2,000,000,000)
        떡의 개별 높이 (1 <= H <= 1,000,000,000)
      
출력조건 : 적어도 M만큼의 떡을 가져가기 위해 설정할 수 있는 절단 높이의 최댓값

예시 : 4 6
      19 15 10 17
풀이 :
   1. N, M 입력
   2. 배열 H 입력
   3. 배열의 원소 중 최댓값을 기준으로 이진탐색
      3-1. 잘린 길이와 M을 비교
      3-2. 잘린 길이가 더 크면 오른쪽 구간에서 다시 이진탐색
      3-3. 잘린 길이가 더 작으면 왼쪽 구간에서 다시 이진탐색
      3-4. 위 과정을 반복

"""

n, m = map(int, input().split(' '))
h_list = list(map(int, input().split()))

# def findMaxHeight(input_list, start, end, req_len):
#   while(start <= end):
#     mid = (start + end) // 2
#     total = sum([i - mid for i in input_list])

#     if total > req_len:
#       start = mid + 1
#     elif total < req_len:
#       end = mid - 1
#     else:
#       return mid

#     if total >= m:
#       break
#   return total
    

# total = findMaxHeight(h_list, 0, len(h_list)-1, m)
# print(total)


# 문제 답안
start = 0
end = max(h_list)
result = 0
while (start <= end):
  total = 0
  mid = (start + end) // 2
  for x in h_list:
    if x > mid :
      total += x - mid  
  if total < m:
    end = mid -1
  else:
      result = mid
      start = mid + 1

print(result)