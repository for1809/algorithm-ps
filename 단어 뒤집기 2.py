'''
문제
문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.

먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.

알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
문자열의 시작과 끝은 공백이 아니다.
'<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고, '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다. 단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

입력
첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.

출력
첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.
'''
# 스택에 태그 넣고 단어 다른 스택에 넣고 뺴고 태그 닫을까 생각해보았으나 단어의 공백이 문제임
from sys import stdin as s
from collections import deque
'''
string = s.readline().rstrip()
word = deque(string)
tag_1 = []
tag_2 = deque()
while True:
    if word[0] == '>':
        tag_1.append(word.popleft())
        break
    tag_1.append(word.popleft())
while True:
    if word[-1] == '<':
        tag_2.appendleft(word.pop())
        break
    tag_2.appendleft(word.pop())
lst = [''.join(reversed(i)) for i in ''.join(word).split()]

print(''.join(tag_1), ' '.join(lst), ''.join(tag_2), sep = '')
'''
# 태그가 3개 이상일 때 문제 발생
# 1차 수정
'''
string = s.readline().rstrip()
tag = deque()
word = deque()
flag = 0
for s in string:
    if s == '<':
        tag.append(s)
        flag = 1
    elif s == '>':
        flag = 0
        tag.append(s)
    else:
        if flag:
            tag.append(s)
        else:
            word.append(s)
print(tag)
print(word)
'''
# 태그 분리는 성공했으나 재조합에 문제가 생김
# 수정본
string = s.readline().rstrip()
lst = []
result = []
for char in string:
    if char == '>':
        lst.append(char)
        result.append(''.join(lst))
        lst.clear()
    elif char == '<':
        result.append(''.join(reversed(lst)))
        lst.clear()
        lst.append(char)
    elif char == ' ' and lst[0] != '<':
        result.append(''.join(reversed(lst)))
        result.append(char)
        lst.clear()
    else:
        lst.append(char)
if lst:
    result.append(''.join(reversed(lst)))
print(''.join(result))
# 최적화 코드 (gpt)
string = input().rstrip()  # 문자열 입력 받기
result = []  # 최종 결과 저장
word = ''  # 현재 단어를 저장
in_tag = False  # 태그 내부 여부 확인

for char in string:
    if char == '<':  # 태그 시작
        result.append(word[::-1])  # 단어를 역순으로 추가
        word = ''
        in_tag = True
        result.append(char)
    elif char == '>':  # 태그 끝
        in_tag = False
        result.append(char)
    elif in_tag:  # 태그 내부 문자
        result.append(char)
    elif char == ' ':  # 공백 문자
        result.append(word[::-1])  # 공백 전 단어를 역순으로 추가
        result.append(char)  # 공백 그대로 추가
        word = ''
    else:  # 일반 문자 (단어 구성)
        word += char

# 마지막 남은 단어 처리
result.append(word[::-1])

# 결과 출력
print(''.join(result))
