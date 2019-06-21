# 백준알고리즘 1822
# https://www.acmicpc.net/problem/1822

# 문제
# 몇 개의 자연수로 이루어진 두 집합 A와 B가 있다. 집합 A에는 속하면서 집합 B에는 속하지 않는 모든 원소를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 집합 A의 원소의 개수 n(A)와 집합 B의 원소의 개수 n(B)가 빈 칸을 사이에 두고 주어진다. (1≤n(A), n(B)≤500,000)이 주어진다. 둘째 줄에는 집합 A의 원소가, 셋째 줄에는 집합 B의 원소가 빈 칸을 사이에 두고 주어진다. 하나의 집합의 원소는 2,147,483,647 이하의 자연수이며, 하나의 집합에 속하는 모든 원소의 값은 다르다.

# 출력
# 첫째 줄에 집합 A에는 속하면서 집합 B에는 속하지 않는 원소의 개수를 출력한다. 다음 줄에는 구체적인 원소를 빈 칸을 사이에 두고 증가하는 순서로 출력한다. 집합 A에는 속하면서 집합 B에는 속하지 않는 원소가 없다면 첫째 줄에 0만을 출력하면 된다.

import sys
read = sys.stdin.readline

read()

a = set(read().rstrip('\n').split(" "))
b = set(read().rstrip('\n').split(" "))
res = list(a - b)
res.sort(key=int)

if len(res) == 0:
    print(0)
else:
    print(len(res))
    print(" ".join(res))
