# n=int(input())
# rem=0
# sum=0
# while n!=0:
#     rem=n%10
#     sum+=rem
#     n=n//10
# print(sum)

# n=int(input())
# rem=0
# prod=1
# while n!=0:
#     rem=n%10
#     prod*=rem
#     n=n//10
# print(prod)

# n=int(input())
# rem=0
# while n!=0:
#     rem=n%10
#     if rem%2==0:
#         print(rem,end="")
#     n=n//10

n=int(input())
rem=0
while n!=0:
    rem=n%10
    if rem%2!=0:
        print(rem,end="")
    n=n//10


