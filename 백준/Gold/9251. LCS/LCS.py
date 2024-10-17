import sys
sys.setrecursionlimit(10**7)
A = input()
B = input()

def LCS(X, Y):
  m, n = len(A), len(B)
  dp = [[-1] * n for _ in range(m)]

  def S(i, j):
    if i<0 or j<0: 
      return 0
    if dp[i][j] != -1: return dp[i][j]

    if X[i] == Y[j]:
      dp[i][j] = S(i-1, j-1)+1
    else:
      dp[i][j] = max(S(i, j-1), S(i-1, j))

    return dp[i][j]

  return S(m-1, n-1)
print(LCS(A, B))

