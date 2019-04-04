'''
codewars 주어진 숫자별 소수 더하기 문제
https://www.codewars.com/kata/sum-of-odd-numbers/train/python

문제
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8

입력
int n

반환값
int sum

출력
없음
'''


def row_sum_odd_numbers(n):
    startNum = 1
    for i in range(n):
        startNum += 2 * i

    sum = 0
    for i in range(n):
        sum += startNum + (2 * i)
    return sum


print(row_sum_odd_numbers(1))  # 1
print(row_sum_odd_numbers(2))  # 8
print(row_sum_odd_numbers(13))  # 2197
print(row_sum_odd_numbers(19))  # 6859
print(row_sum_odd_numbers(41))  # 68921

# 추가로 이 문제는 sum만 구하면 된다.
# 가로로 각 라인을 모두 더하면 n의 3제곱이라는 규칙이 나온다.
# 따라서 그냥 return n*3 이라는 답이 가장 좋긴하다.
