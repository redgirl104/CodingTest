'''
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
'''

S = 'CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]

# O(N * M)
def solution(S, P, Q):
  geo = {'A': 1, 'C':2, 'G':3, 'T':4}
  # S를 배열로 변환
  list_s = list(S)
  result_geo = []
  # P[k] ~ Q[k] 사이의 문자열 구하기
  for i in range(len(P)):
    p, q = P[i], Q[i]
    sub_geo = list_s[p:q+1]
    sub_geo_num =[]
    min_geo = 4
    geo_num = 1
    # print(list(S[p:q+1]))
    # 문자열을 geo 코드(숫자)로 변환
    for j in sub_geo:
      # print(geo[j])
      geo_num = geo[j]
      sub_geo_num.append(geo_num)
      # 최솟값 찾기
      if geo_num < min_geo:
        min_geo = geo_num
    result_geo.append(min_geo)
  return result_geo
        
# O(N + M)
# 문자열은 list로 바꾸지 말자. 바꾸지 않아도 인덱싱이 됨...
def solution2(S, P, Q):
  result_geo = []
  # P[k] ~ Q[k] 사이의 문자열 구하기
  for i in range(len(P)):
    p, q = P[i], Q[i]
    sub_geo = S[p:q+1]
    # print(type(sub_geo))
    # geo 문자열이 있는지 여부만 차례로 체크하면 됨
    try:
      sub_geo.index('A')
      result_geo.append(1)
    except:
      try:
        sub_geo.index('C')
        result_geo.append(2)
      except:
        try:
          sub_geo.index('G')
          result_geo.append(3)
        except:
          result_geo.append(4)
  return result_geo
        


print(solution2(S, P, Q))
print(S[0:4])