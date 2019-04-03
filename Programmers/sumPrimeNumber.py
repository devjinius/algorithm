'''
프로그래머스 두 정수 사이의 합 문제
https://programmers.co.kr/learn/courses/30/lessons/14406

문제
2부터 N까지의 모든 소수의 합을 구하세요.
N이 7이라면 {2,3,5,7} = 17을 출력 하시면 됩니다.
N의 범위는 2이상 10,000,000이하 입니다.
효율성 테스트의 모든 시간 제한은 1초입니다.

입력
N

반환값
int

출력
없음
'''

# 풀이 1
# N 이하의 소수를 먼저 구해야한다.
# 가장 쉽게 접근할 수 있는 방법이 2부터 N-1까지 나눈다.
# 나누어 떨어지는 수가 없으면 소수다.
# 4의 경우 이미 2로 나누어 떨어졌으므로 3으로 나누지 않아도 된다. flag를 이용하여 구현


def solution1(N):
    primeNumbers = []
    for i in range(2, N+1):
        flag = True

        for j in range(2, i):
            if (i % j == 0):
                flag = False
                break
        if (flag):
            primeNumbers.append(i)
    return sum(primeNumbers)


# 풀이 2
# 에라토스테네스의 체 방법
# 쉽게 설명하자면 아래와 같다.
# 2 본인을 제외한 2의 배수를 모두 mark
# 3 본인을 제외한 3의 배수를 모두 mark
# 4는 이미 2의 배수이므로 pass
# 5를 제외한 5의 배수를 모두 mark
# 6도 4의 경우처럼 pass
# 7을 제외한 7의 배수를 모두 mark ...
# 위의 과정을 반복하면 배수가 아닌 경우만 남고 그게 소수다.
# 성능이 정말 훨씬 좋다.


def solution2(N):
    # 0부터 N까지 배열을 초기화한다. 1은 0으로 세팅
    primeNumbers = [0, 0]
    for i in range(2, N + 1):
        primeNumbers.append(i)

    # 이제 마킹한다.
    for i in range(2, N+1):
        # 4나 6처럼 이미 마킹되었다면 pass
        if(primeNumbers[i] == 0):
            continue
        # 자신을 제외하기에 i+i부터 tic이 시작된다.
        # step을 i만큼 증가시켜 j를 i의 배수로 만든다.
        for j in range(i+i, N+1, i):
            primeNumbers[j] = 0
    return sum(primeNumbers)


print(solution2(100))

# 프로그래머스에서는 C++만 사용 가능하다.
# 그래서 C++로도 짜봤다.

# include <iostream>
# include <vector>
# using namespace std;
# vector<int> primeNumbers;
# for(int i = 2; i < N+1; i = i + 1) {
#     bool flag = true;
#     for (int j = 0; j < primeNumbers.size(); j = j + 1) {
#         if (i % primeNumbers[j] == 0){
#             flag = false;
#             break;
#         }
#     }
#     if (flag) {
#         primeNumbers.push_back(i);
#     }
# }
# long long answer = 0;
# for (int i = 0; i < primeNumbers.size(); i = i + 1) {
#     answer = answer + primeNumbers[i];
# }
# return answer;
