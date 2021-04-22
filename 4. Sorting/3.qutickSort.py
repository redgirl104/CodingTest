
"""
퀵정렬 : 기준데이터를 설정, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
        기본적인 퀵 정렬 - 첫 번째 데이터를 기준(pivot)으로 설정

방법 : 기준 데이터(pivot)의 오른쪽 부터 탐색하면서 pivot 보다 큰 첫 번째 데이터
      리스트 끝에서 왼쪽으로 탐색하면서 pivot 보다 작은 첫 번째 데이터
      두 데이터를 스위치
      두 데이터의 위치가 역전되면 > pivot과 작은 데이터를 스위치
      pivot을 기준으로 왼쪽/오른쪽이 분할됨
      분할된 왼쪽/오른쪽 리스트에서 위 과정 반복

"""

list_input = [2, 1, 7, 3, 9, 5, 8]

def quick_sort(array, start, end):
  if(start >= end):
    return
  pivot = start
  left = start + 1
  right = end

  while left <= right:
    # pivot보다 큰 데이터를 찾을때 까지 반복
    while(left<=end and array[left] <= array[pivot]):
      left += 1
    # pivot보다 작은 데이터를 찾을때 까지 반복
    while (right > start and array[right] >= array[pivot]):
      right -= 1
  
    if left > right:
      array[pivot], array[right] = array[right], array[pivot]
    else:
      array[left], array[right] = array[right], array[left]

  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)
  return(array)
  

quick_sort(list_input, 0, len(list_input)-1)
print(list_input)