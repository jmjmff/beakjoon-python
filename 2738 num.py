#입력받은 N,M이 크기가 주어질때, 두 행렬을 더하는 프로그램을 작성
A,B =[],[]
N,M = map(int,input().split())

# 첫 번째 행렬 입력 받기
for i in range(N):
    A.append(list(map(int, input().split())))
# 두 번째 행렬 입력 받기
for j in range(N):
    B.append(list(map(int, input().split())))

# 두 행렬을 더해서 결과 출력
for n in range(N):
    for m in range(M):
#더한 결과를 출력할 때 각 행의 원소를 공백으로 구분하여 출력하고, 한 행이 끝날 때마다 줄바꿈을 출력하여 결과를 더 보기 좋게 출력하도록
        print(A[n][m]+B[n][m], end=" ")
    print()  # 다음 행으로 넘어가기 위해 줄바꿈 출력



