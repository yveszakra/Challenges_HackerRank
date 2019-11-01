import sys

def solution(A):
  """Your solution goes here."""
  max = A[0]
  row_count = 1
  
  for x in range(1, len(A)):
    if A[x] > max:
      row_count += 1
      max = A[x]
    x += 1
    
  return row_count


def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()