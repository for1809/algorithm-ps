'''
문제
문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.

입력
첫째 줄부터 N번째 줄까지 문자열이 주어진다. (1 ≤ N ≤ 100) 문자열의 길이는 100을 넘지 않는다.

출력
첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.
'''
import sys
result = []
lines = sys.stdin.readlines()

for line in lines:
    line = line.rstrip('\n')
    low, up, dig, space = 0, 0, 0, 0
    for c in line:
        if c.islower():
            low += 1
        elif c.isupper():
            up += 1
        elif c.isdigit():
            dig += 1
        elif c.isspace():
            space += 1
    result.append(' '.join(map(str, [low, up, dig, space])))
print('\n'.join(result))
'''
EOF(End of File) 처리하는 방법
1. input 사용하고 예외처리 except EOFError
2. readlines로 전체 읽어버리기
'''