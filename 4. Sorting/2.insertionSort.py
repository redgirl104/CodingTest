
"""
삽입정렬 : 처리되지 않은 데이터를 하나 골라 
처리된 데이터의 마지막 데이터부터 비교
선택한 (처리되지 않은 데이터) 데이터가 비교 대상보다 작으면 왼쪽에 삽입 : switch, 크면 오른쪽에 삽입 : stay

위 방법을 리스트 원소 끝까지 반복

"""

list_data = [2, 4, 1, 7, 3]

for i in range(1, len(list_data)):
  for j in range(i, 0, -1):
    if list_data[j] < list_data[j-1]:
      list_data[j], list_data[j-1] = list_data[j-1], list_data[j]
    else:
      break
print(list_data)
