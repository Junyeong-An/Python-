N,M=map(int,input().split())
count=0
array=[[0 for i in range(N)] for j in range(M)]
for i in range(0,N):
    for j in range(0,M):
        array[i][j]=input()
for i in range(1,N+1):
    for j in range(1,M+1):
          if(array[i-1][j-1]==array[i][j]):
            count+=1
print(count)