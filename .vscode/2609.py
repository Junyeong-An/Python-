a,b=map(int,input().split())
c=min(a,b)
max_count=0 #최대공약수
min_count=0 #최소공배수
for i in range(1,c):
    if a%i==0 and b%i==0:
        max_count=max(max_count,i)    
min_count=(a* b)/max_count

print(max_count)
print(int(min_count))