#공백 4 3 2 1 0 
# 별 1 2 3 4 5
N=int(input())
for i in range(1,N+1):
  for j in range(N-i):
    print(" ",end="")
  for k in range(i): 
    print("*",end="")
    
  print()