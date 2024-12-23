'''
문제
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.

입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.

출력
출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.
'''
# 코드
# 스택을 사용해 (는 넣고 )가 (랑 만나면 pop 하는 식으로 구현
'''
from sys import stdin as s
n = int(input())
for i in range(n):
    ps = s.readline()
    lst = []
    for c in ps:
        if c == '(':
            lst.append(c)
        else:
            try:
                lst.pop()
            except IndexError:
                result = 'NO'
    if not lst:
        result = 'YES'
    else:
        result = 'NO'
    print(result)
    '''
'''스택이 비어있는데 pop하는 경우를 대비하여 예외처리를 했지만 오류가 발생해서 result가 NO여야 하는 경우에도
최종적으로 스택이 비어있으면 괄호가 모두 짝지어진 것으로 판단해서 결과가 YES가 되어버리는 문제가 발생함'''
# 수정본
from sys import stdin as s
n = int(s.readline())
for i in range(n):
    ps = s.readline().strip()
    lst = []
    for c in ps:
        if c == '(':
            lst.append(c)
        else:
            try:
                lst.pop()
            except IndexError:
                result = 'NO'
                lst.append(0)
                break
    if not lst:
        result = 'YES'
    else:
        result = 'NO'
    print(result)
'''YES가 나와야 하는 문자열이 NO가 출력되는 이상현상이 있었는데 stdin으로 입력을 받아서
끝의 공백이 문자열 취급을 받아 pop을 1회 더 반복해서 생기는 문제였음. strip()메서드로 해결
허나 pop 오류가 발생할 때 0을 append하는 게 좀 짜치는 감이 있음...'''
#개선안
from sys import stdin as s
n = int(s.readline())
for i in range(n):
    ps = s.readline().strip()
    result = 'YES'
    lst = []
    for c in ps:
        if c == '(':
            lst.append(c)
        else:
            if lst:
                lst.pop()
            else:
                result = 'NO'
                break
    if lst:
        result = 'NO'
    print(result)
# 예외처리 대신 조건문으로 처리하고 result 의 default 값을 YES로 설정하니 더 깔끔해짐