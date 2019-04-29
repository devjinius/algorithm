# 백준알고리즘 11047번
# https://www.acmicpc.net/problem/11047

# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

# 출력
# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.


[coinLen, targetCost] = list(map(int, input().split(" ")))
coins = []
for _ in range(coinLen):
    coins.append(int(input()))

count = 0
while(len(coins) != 0):
    coin = coins.pop()
    tempCount = targetCost // coin

    if (tempCount == 0):
        continue

    targetCost -= (coin * tempCount)
    count += tempCount

print(count)
