var prev=1
var now=2
var next
var sum=0
while (now < 4*Math.pow(10,6) ) {
    if (now %2 ==0) {
        sum =sum+now
    } 
    next=now+prev   
    prev=now
    now=next
}
console.log(now)