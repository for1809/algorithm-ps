'''
문제
 
$n \choose m$의 끝자리
$0$의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수
$n$,
$m$ (
$0 \le m \le n \le 2,000,000,000$,
$n \ne 0$)이 들어온다.

출력
첫째 줄에
$n \choose m$의 끝자리
$0$의 개수를 출력한다.
'''
def count(n):
    count_two = 0
    count_five = 0
    exp_two = 1
    exp_five = 1
    while 2 ** exp_two <= n:
        count_two += n // 2 ** exp_two
        exp_two += 1
    while 5 ** exp_five <= n:
        count_five += n // 5 ** exp_five
        exp_five += 1
    return count_two, count_five
n, m = map(int, input().split())
n2, n5 = count(n)
m2, m5 = count(m)
dif2, dif5 = count(n - m)
two = n2 - m2 - dif2
five = n5 - m5 - dif5
print(min(two, five))