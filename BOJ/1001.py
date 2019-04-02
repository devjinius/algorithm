# 백준알고리즘 1001번
# https://www.acmicpc.net/problem/1001

# 문제
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 첫째 줄에 A-B를 출력한다.

a, b = input('A와 B를 띄어쓰기로 구분하여 입력해주세요. (0 < A, B < 10) : ').split(" ")

print(int(a) - int(b))
