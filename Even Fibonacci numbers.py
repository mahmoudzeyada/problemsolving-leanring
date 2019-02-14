prev=1
now=2
next=0
sum=0
while(now <= 4*10**6):
    if now %2 ==0 :
        sum+=now
    next=now+prev
    prev = now
    now=next
    
print (sum)
