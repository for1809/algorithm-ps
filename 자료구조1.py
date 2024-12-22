'''
문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''
lst = []
for i in range(int(input())):
    prompt = input().split()
    if 'push' in prompt:
        lst.append(prompt[1])
    elif 'pop' in prompt:
        try:
            print(lst.pop())
        except IndexError:
            print(-1)
    elif 'size' in prompt:
        print(len(lst))
    elif 'empty' in prompt:
        print(1) if lst == [] else print(0)
    else:
        print(-1) if lst == [] else print(lst[-1])
# 결과: 시간초과
'''
개선점
1. if ' ' in prompt로 작성하여 push1 같은 잘못된 입력도 True로 처리될 수 있음.
속도가 index로 접근하는 게 더 빠름
2. 예외처리보다 조건문으로 하는 것이 더 명확
3. top 명령을 명시적으로 처리하는 것이 좋을 것 같음 
'''
#개선코드
lst = []
import sys
for i in range(input()):
    prompt = sys.stdin.readline().split()
    cmd = prompt[0]

    if cmd == 'push':
        lst.append(prompt[1])
    elif cmd == 'pop':
        print(lst.pop() if lst else -1)
    elif cmd == 'size':
        print(len(lst))
    elif cmd == 'empty':
        print(1 if not lst else 0)
    elif cmd == 'top':
        print(lst[-1] if lst else -1)
