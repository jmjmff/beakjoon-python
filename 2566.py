# 9x9격자판 배열 선얼과 입력 받기
import sys

A = []
#A의 행렬을 입력받는다
for i in range(9):
    A.append(list(map(int,sys.stdin.readline().split())))
#세로항 가로항 최댓값을 초기화하고 선언해줌
n=0
m=0
max=0
#이중 for문으로 최댓값을 찾고 돌린다
for a in range(9):
    for b in range(9):
        if A[a][b] >= max :#구하려는 값이 max보다 큰지 검사해줌
            max =A[a][b]
            n = a+1#0부터 시작하므로 +1을 해준다
            m = b+1#0부터 시작하므로 +1을 해준다
print(max)
print(n,m)

