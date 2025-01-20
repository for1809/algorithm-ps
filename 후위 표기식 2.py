'''
문제
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다. (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

출력
계산 결과를 소숫점 둘째 자리까지 출력한다.
'''
'''
import sys
read = sys.stdin.readline
n = int(read().strip())
notation = read().strip()
num_list = []
lst = []
stack = []
for i in range(n):
    num = float(read().strip())
    num_list.append(num)
for c in notation:
    if c.isalpha():
        lst.append(num_list[ord(c) - ord('A')])
    else:
        lst.append(c)

def Binaryop(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1/n2

for i in lst:
    if isinstance(i, float):
        stack.append(i)
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        stack.append(Binaryop(n1, n2, i))

print(f'{stack[0]:.2f}')
'''

# 개선안
import sys
read = sys.stdin.readline
n = int(read().strip())
notation = read().strip()
num_list = [float(read().strip()) for i in range(n)]
stack = []

def Binaryop(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1/n2

for c in notation:
    if c.isalpha():
        stack.append(num_list[ord(c) - ord('A')])
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        stack.append(Binaryop(n1, n2, c))
print(f'{stack[-1]:.2f}')