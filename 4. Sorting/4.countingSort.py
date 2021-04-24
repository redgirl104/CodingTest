"""
For simplicity, consider the data in the range 0 to 9. 
Input data: 1, 4, 1, 2, 7, 5, 2
  1) Take a count array to store the count of each unique object.
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  2  0   1  1  0  1  0  0

  2) Modify the count array such that each element at each index 
  stores the sum of previous counts. 
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  4  4  5  6  6  7  7  7

The modified count array indicates the position of each object in 
the output sequence.
 
  3) Output each object from the input sequence followed by 
  decreasing its count by 1.
  Process the input data: 1, 4, 1, 2, 7, 5, 2. Position of 1 is 2.
  Put data 1 at index 2 in output. Decrease count by 1 to place 
  next data 1 at an index 1 smaller than this index.

시간복잡도, 공간복잡도 = O(N + K)
-> 데이터가 0과 999,999로 단 2개만 존재하는 경우 : 심각한 비효율성
-> 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적
-> ex) 성적 100점 맞은 학생이 여러명일 경우
"""
# <Pseudo code>
# input array
# define count array : range 0 ~ 9
# iteration input_array from first to last atom 
#   append atom at right index
# iteration count array
#   if not 0 then print index * count
"""
array = [1, 4, 1, 2, 7, 5, 2]
output = []
count_array = [0] * 10

for i in range(0, len(array)):
  for j in range(0, len(count_array)):
    if array[i] == j:
      count_array[j] += 1

for i in range(0, len(count_array)):
  if count_array[i] > 0:
    for _ in range(count_array[i]):
      output.append(i)

print(output)
"""

array = list(map(int, input().split()))

count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')