# 재귀란?

재귀는 함수가 자기 자신을 호출하는 것을 이야기 합니다.

## 특징

모든 재귀 함수는 일반 함수로 구현할 수 있습니다. 또한 일반 함수가 더 높은 성능을 보이는 경우가 많습니다.

재귀함수는 항상 종료조건이 필요합니다. 그렇지 않으면 무한 루프에 빠지게 됩니다.

이렇게 불편한 재귀 함수를 사용해서 얻는 이득은 프로그래머의 능력입니다 =)

## 예시

- a부터 b까지 정수를 더해서 리턴해 주는 함수

```js
const atob = (a, b) => {
  return a === b ? b : a + atob(a + 1, b);
};
```

- 팩토리얼

```js
const fact = n => {
  return n === 1 ? 1 : n * fact(n - 1);
};
```

- 피보나치

```js
const fibo = n => {
  return n < 2 ? n : fibo(n - 1) + fibo(n - 2);
};
```

### 다이나믹 프로그래밍

피보나치의 경우 중복값이 계속 사용된다. 예를들어 피보나치 `fibo(5)`와 `fibo(4)`를 호출하는 경우 어딘가 `fibo(5), (4) (3), (2), (1)`의 결과를 저장해놨다면 fibo(4)는 구할 필요가 없다. 이미 한번 연산해봤기 때문이다.

```js
const memo = [0, 1];
let count = 0;

const fiboMemo = n => {
  count++;
  console.log('called fiboMemo: ', count);
  if (typeof memo[n] !== 'number') {
    memo[n] = fiboMemo(n - 1) + fiboMemo(n - 2);
  }
  return memo[n];
};

fiboMemo(15); // fibo를 29번 호출
// f(1) ... f(15) 까지 값은 저장되어 있음

count = 0; // count 초기화
fiboMemo(14); // f(14) 1번 호출

count = 0; // count 초기화
fiboMemo(16); // f(16), f(15), f(14) 총 3번 호출

// f(16)의 결과 저장
```

### 참고자료

- [메모이제이션을 활용한 피보나치](https://github.com/Im-D/Dev-Docs/blob/master/Design_Pattern/Memoization.md#memoization%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%EC%BD%94%EB%93%9C-3)
- [Understanding Memoization In JavaScript](https://morioh.com/p/08ba8ca0fb47/understanding-memoization-in-javascript)
