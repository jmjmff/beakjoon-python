import sys
n = int(sys.stdin.readline())
queue = []

for i in range(n):
    word = sys.stdin.readline().split()

    if word[0]=='push':
        value = word[1]
        queue.append(value)
    elif word[0] == 'pop':
        #큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0]) #앞에 있는 수를 출력
            del(queue[0]) # 그 수를 뺸다

    elif word[0] == 'size':
        print(len(queue))
    elif word[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif word[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
