# 정렬

배열은 제일 많이 사용되는 자료구조다. 이 배열에서도 정말 자주 사용되는 것이 배열이다.

정렬하는 방법은 여러가지가 있으며 각각 복잡도가 다르다.
몇가지를 알아보자.

###셔플

```js
const arr = [];
const { random, floor } = Math;

for (let i = 0; i < 100; i++) {
  arr.push(i);
}

for (let i = 0; i < 10000; i++) {
  let j = floor(random() * 100);
  let tmp = arr[0];
  arr[0] = arr[j];
  arr[j] = tmp;
}

console.log(arr);
```

별거 없다. 잘 섞으면 된다.

### 객체의 정렬

```js
const students = [
  { name: 'Jin', weight: 70, score: 100 },
  { name: 'Chulsu', weight: 65, score: 80 },
  { name: 'Minseong', weight: 60, score: 70 },
  { name: 'Minsu', weight: 55, score: 60 },
  { name: 'Kihoon', weight: 75, score: 65 },
  { name: 'Jin', weight: 75, score: 90 },
  { name: 'Jin', weight: 70, score: 90 },
  { name: 'Mike', weight: 80, score: 90 },
  { name: 'Psy', weight: 76, score: 95 },
  { name: 'Andy', weight: 75, score: 75 },
  { name: 'Anthony', weight: 80, score: 85 }
];

students.sort((a, b) => {
  if (a.name > b.name) {
    return 1;
  } else if (a.name < b.name) {
    return -1;
  } else {
    if (a.weight > b.weight) {
      return -1;
    } else if (a.weight < b.weight) {
      return 1;
    } else {
      if (a.score > b.score) {
        return -1;
      } else if (a.score < b.score) {
        return 1;
      } else {
        return 0;
      }
    }
  }
});

console.log(students);
```

js에서는 callback function을 받아 처리한다. 1이면 오름차순, -1은 반대 0은 같을때이다.

### 사용알고리즘

크롬과 node(즉 V8) 에서는 길이가 10이하면 `insertion sort`, 10 이상인 경우 quick sort를 사용한다.

### 안정정렬과 불안정정렬

`[3, 2, 2, 1]` 이 배열의 오름차순 정렬 결과는 `[1, 2, 2, 3]`이다.

기존의 배열을 뜯어봤을 때 `3, 2-1, 2-2, 1` 이라고 하자.

배열 후 결과는 두가지가 가능하다. `1, 2-1, 2-2, 3`과 `1, 2-2, 2-1, 3` 이렇게 말이다.

2-1의 위치가 보장되면 안정, 보장되지 않으면 불안정 정렬이다.
