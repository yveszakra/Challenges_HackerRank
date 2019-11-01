import sys
'''
def solution(A):
  """Your solution goes here."""
  A.sort()
  Sum = sum(A)
  mid = Sum // 2
  server1 = max(A)
  server2 = 0
  
  if max(A) >= mid:
    server2 = Sum - max(A)
  else:
    for x in range(len(A)-1):
      if server1 <= mid:
        server1 += A[x]
      else:
        server2 += A[x]
        
  diff = server1 - server2
  
  return abs(diff)
  


def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
'''

T = "2?:?8"
print(T.index('?'))
Print(is('?' < 3))