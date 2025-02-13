'''
문제
여러 개의 쇠막대기를 레이저로 절단하려고 한다. 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다. 쇠막대기와 레이저의 배치는 다음 조건을 만족한다.

쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다. - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.
아래 그림은 위 조건을 만족하는 예를 보여준다. 수평으로 그려진 굵은 실선은 쇠막대기이고, 점은 레이저의 위치, 수직으로 그려진 점선 화살표는 레이저의 발사 방향이다.



이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있다.

레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반드시 레이저를 표현한다.
쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다.
위 예의 괄호 표현은 그림 위에 주어져 있다.

쇠막대기는 레이저에 의해 몇 개의 조각으로 잘려지는데, 위 예에서 가장 위에 있는 두 개의 쇠막대기는 각각 3개와 2개의 조각으로 잘려지고, 이와 같은 방식으로 주어진 쇠막대기들은 총 17개의 조각으로 잘려진다.

쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하시오.

입력
한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.

출력
잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.
'''
# 1차시: 루프 두 번 돌기, 시간 복잡도:O(n)
'''
loc = input()
lst = []
for _ in loc:
    if lst:
        if lst[-1] == '(' and _ == ')':
            lst.pop()
            lst.append('/')
        else:
            lst.append(_)
    else:
        lst.append(_)
slash = ''.join(lst)
slst = []
result = 0
for _ in slash:
    if _ == '(':
        slst.append(_)
    elif _ == ')':
        slst.pop()
        result += 1
    elif _ == '/':
        result += len(slst)
print(result)
'''
# 정답은 맞는데 더 좋은 방법을 찾아보자
loc = input()
lst = []
result = 0
for i, c in enumerate(loc):
    if c == '(':
        lst.append(c)
    elif c == ')':
        if loc[i - 1] == '(':
          lst.pop()
          result += len(lst)
        else:
            lst.pop()
            result += 1
print(result)
''' 예전에 풀었던 문제에서 리스트 인덱스 검색으로 풀었을 때 시간 초과 났던 희미한 기억 때문에
인덱싱의 시간 복잡도가 1차였던 것 같은데 사실 상수였다. 아마 insert랑  value찾기랑 헷갈린듯...
괜히 돌아갔네
엥 그런데 첫번째 코드보다 시간이 더 걸렸다... 뭐지?'''