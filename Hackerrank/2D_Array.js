/*
HackerRank 2D_Array 문제
https://www.hackerrank.com/challenges/2d-array/problem

문제
Given a 6*6 2D Array

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

we define hourglass like this,

a b c
  d
e f g

there are 16 hourglasses in array. It should return an integer, the maximum hourglass sum in the array.

입력
The first line contains an integer,  N(the number of integers in A). 
The second line contains N space-separated integers describing A.
*/

function hourglassSum(arr) {
  let maxSum = -64;

  for (let i = 1; i < 5; i++) {
    for (let j = 1; j < 5; j++) {
      let tempSum =
        arr[i - 1][j - 1] +
        arr[i - 1][j] +
        arr[i - 1][j + 1] +
        arr[i][j] +
        arr[i + 1][j - 1] +
        arr[i + 1][j] +
        arr[i + 1][j + 1];
      maxSum = maxSum > tempSum ? maxSum : tempSum;
    }
  }
  return maxSum;
}
