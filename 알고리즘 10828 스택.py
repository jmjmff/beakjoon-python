import sys
n = int(sys.stdin.readline())
stack=[]
for i in range (n):
    word = sys.stdin.readline().split()

#. 명령을 식별하려면 입력된 문자열을 분할하고 첫 번째 부분, 즉 0번 인덱스의 값을 가져와야 합니다.
    if word[0] == 'push':
        newword = word[1]
        stack.append(newword)

    elif word[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif word[0] == 'size':
        print(len(stack))
        # count() 함수는 리스트 내 특정 요소의 개수를 세는 함수이지만, 스택의 크기를 얻고 싶은 것이므로 len(stack)을 사용해야 gka
    elif word[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else: print(0)
    elif word[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])