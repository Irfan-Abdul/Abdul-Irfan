initial_price,percentage=input().split()
initial_price=int(initial_price)
percentage=int(percentage)
total_price=int(0)
c=round(int(percentage)/100,2)
while(initial_price>=1):
    total_price+=initial_price
    initial_price-=initial_price*c
print(int(total_price))    
