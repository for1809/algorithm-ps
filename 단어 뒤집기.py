'''문제
문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다. 단어의 길이는 최대 20, 문장의 길이는 최대 1000이다. 단어와 단어 사이에는 공백이 하나 있다.

출력
각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.
'''
# 코드
'''
from sys import stdin
n = int(input())
for _ in range(n):
    letter = stdin.readline().split()
    lst = list(map(reversed, letter))
    print(lst)
    result = ' '.join(lst)
    print(result)
# TypeError: sequence item 0: expected str instance, reversed found 발생
'''
'''
lst를 print 해보니[<reversed object at 0x00000201E27BCAF0>, <reversed object at 0x00000201E27BC310>, <reversed object at 0x00000201E27BCB80>, <reversed object at 0x00000201E27BCBB0>, <reversed object at 0x00000201E27BCC10>, <reversed object at 0x00000201E27BCC40>, <reversed object at 0x00000201E27BCC70>, <reversed object at 0x00000201E27BCCA0>, <reversed object at 0x00000201E27BCCD0>, <reversed object at 0x00000201E27BCD00>, <reversed object at 0x00000201E27BCD30>, <reversed object at 0x00000201E27BCD60>, <reversed object at 0x00000201E27BCD90>, <reversed object at 0x00000201E27BCDC0>, <reversed object at 0x00000201E27BCDF0>, <reversed object at 0x00000201E27BCE20>]
여전히 맵객체인 것을 확인
'''
# 해결
from sys import stdin
n = int(input())
for _ in range(n):
    letter = stdin.readline().split()
    lst = [''.join(list(reversed(l))) for l in letter]
    print(' '.join(lst))

# reversed가 iterator를 반환하기 때문에 발생한 문제. list comprehension 사용하여 해결함
# 개선안
from sys import stdin
n = int(input())
for i in range(n):
    letter = stdin.readline().split()
    lst = [''.join(reversed(word)) for word in letter]
    result = ' '.join(lst)
    print(result)
# map 객체도 iterable이므로 join가능. 그렇게 하면 중간에 reversed 객체를 list로 변환하는 과정을 거치지 않아도 됨
