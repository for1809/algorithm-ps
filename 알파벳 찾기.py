from sys import stdin
string = stdin.readline().strip()
result = [string.find(chr(i)) if chr(i) in string else -1 for i in range(97, 123)]
print(' '.join(map(str, result)))

