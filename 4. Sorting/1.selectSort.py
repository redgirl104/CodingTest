
"""
선택정렬 : 처리되지 않은 데이터 중에서 가장 작은 원소를 가장 왼쪽의 데이터와 교환
"""

input_list = list(map(int, input().split()))

for i in range(len(input_list)):
  pointer = i
  for j in range(i+1, len(input_list)):
    if input_list[j] < input_list[pointer]:
      pointer = j
  input_list[i], input_list[pointer] = input_list[pointer], input_list[i]


print(input_list)

print('hello')