avg=0
sum=0

for i in range(5):
    a=0
    a= int(input())
    if a<40:
        a=40
    sum+=a
avg=sum/5
print(int(avg))

