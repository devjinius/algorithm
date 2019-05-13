# 백준알고리즘 1978
# https://www.acmicpc.net/problem/1978

# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

testLen = int(input())

primes = set(range(2, 1000+1))
for i in range(2, 1000+1):
    if i in primes:
        primes -= set(range(2*i, 1000+1, i))


inputList = list(filter(lambda x: x in primes, map(int, input().split())))
print(len(inputList))
