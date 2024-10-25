# n=int(input("n:"))
# if n%2==0:
#     for i in range(1,n+1):
#         for j in range(1,3):
#             print(i,end=" ")
# else:
#     for i in range(1,n+1):
#         for j in range(1,4):
#             print(i,end=" ")

# n=int(input("n:"))
# for i in range(1,n+1):
#     if i%2==0:
#         for j in range(1,3):
#             print(i,end=" ")
#     else:
#         for j in range(1,4):
#             print(i,end=" ")

# n=int(input("n:"))
# if n>=-9 and n<=9:
#     print("One")
# elif n>=-99 and n<=99:
#     print("two")
# elif n>=-999 and n<=999:
#     print("three")
# else:
#     print("multi")
# l1=[10,20,30]
# l2=l1[::-1]
# print(l1)
# print(l2)
# l1.reverse()
# print(l1)
# t1=(10,20,30,40,50)
# l1=[10,20,20,10,30]
# l1.remove(10)
#  print(l1)
# s1={"nisha",10,10.5}
# l1=[10,"nisha",96.1]
# t1=(2.5,"nisha",100.05)
# s1={10,20,30,10,20}
# s2={50,40,30,20}
# s3=set()
# s3=s1.symmetric_difference(s2)
# for i in s1:
#     if i in s2 and i not in s3:
#         s3.add(i)



# print(s3)
# l=['10','20','30','40']
# l1=["n","i","s",'h','a']
# # print(l1)
# # l1.insert(-2,50)
# # print(l1)
# print(":".join(l))
# s="the house"
# print(s.istitle())
# s1=" a      b    "
# print(s1.strip())
# print("Hello".center(12,'*'))
# print("Hello?".isascii())
# x=0
# for i in range(5):
#     x+=i
#     if i%2==0:
#         x+=1
# print(x)
# def func(a,c,d,b=0,*args,**kargs):
#     print(a,args,b,c,d,kargs)
# func(10,c=50,d=60,x=10,y=20)
n=int(input('n:'))
a=0
b=1
for i in range(n):
    # if i==0 or i==1:
    #     print(i,end=" ")
    # else:
        print(a,end=" ")
        c=a+b
        a=b
        b=c
       