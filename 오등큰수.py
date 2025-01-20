'''
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오등큰수 NGF(i)를 구하려고 한다.

Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오등큰수는 -1이다.

예를 들어, A = [1, 1, 2, 3, 4, 2, 1]인 경우 F(1) = 3, F(2) = 2, F(3) = 1, F(4) = 1이다. A1의 오른쪽에 있으면서 등장한 횟수가 3보다 큰 수는 없기 때문에, NGF(1) = -1이다. A3의 경우에는 A7이 오른쪽에 있으면서 F(A3=2) < F(A7=1) 이기 때문에, NGF(3) = 1이다. NGF(4) = 2, NGF(5) = 2, NGF(6) = 1 이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

출력
총 N개의 수 NGF(1), NGF(2), ..., NGF(N)을 공백으로 구분해 출력한다.
'''
# 첫번째 시도: 빈도수 딕셔너리에 기록하기
n = int(input())
seq = list(map(int, input().split()))
count = {}
result = [-1] * n
stack = []
for _ in seq:
    if _ in count:
        count[_] += 1
    else:
        count[_] = 1
# 시간복잡도 O(n)
for i in range(n - 1, -1, -1):
    a = seq[i]
    b = count[a]
    if stack:
        while stack and b >= count[stack[-1]]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
    stack.append(a)
print(' '.join(map(int, result)))

# 찾아봤는데 collections에 counter라는 함수를 사용하면 빈도 딕셔너리가 생성된다구 함
# 그리고 반복문에 쓸데없는 변수 선언 하지 말고 연산에 바로 넣는 게 나을듯 함. 헷갈리기도 하고 적지만 연산이 늘어나긴 하니까...