# n=int(input())
# val=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")
    
#         else:
#             print(" ",end=" ")
#     val+=1  
#     if val>9:
#         val=1
#     print()


# n=int(input())
# val=n
# if val >9:
#     val=9
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")
    
#         else:
#             print(" ",end=" ")
#     val-=1  
#     if val<1:
#         val=9
#     print()



# n=int(input())
# val=n
# if n>9:
#     val=9
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<1:
#         val=9
#     print()


# n=int(input())
# val=1
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     if val>9:
#         val=1
#     print()


# n=int(input())
# val=65
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     if val>90:
#         val=65
#     print()


# n=int(input())
# val=90
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<65:
#         val=90
#     print()


# n=int(input())
# val=1
# for i in range(n):
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     if val>9:
#         val=1
#     print()


# n=int(input())
# val=n
# if n>9:
#     val=9
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<1:
#         val=9
#     print()


# n=int(input())
# for i in range(n):
#     val=1
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#             val+=1
#             if val>9:
#                 val=1
#         else:
#             print(" ",end=" ")
    
#     print()



# n=int(input())
# val=n
# if n>9:
#     val=9
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<1:
#         val=9
#     print()



# n=int(input())
# for i in range(n):
#     val=65
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#             val+=1
#             if val>90:
#                 val=65
#         else:
#             print(" ",end=" ")
#     print()



# n=int(input())
# for i in range(n):
#     val=65+n-1
#     if val>90:
#         val=90
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#             val-=1
#             if val<65:
#                 val=90
#         else:
#             print(" ",end=" ")
#     print()




# n=int(input())
# for i in range(n):
#     val=65
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#             val+=1
#             if val>90:
#                 val=65
#         else:
#             print(" ",end=" ")
#     print()



# n=int(input())
# val=65+n-1
# if val>90:
#     val=90
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<65:
#         val=90
#     print()


# n=int(input())
# val=65
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val+=1
#     if val>90:
#         val=65
#     print()



# n=int(input())

# for i in range(n):
#     val=65
#     for j in range(n):
#         if i+j<=n-1:
#             print(chr(val),end=" ")
#             val+=1
#             if val>90:
#                 val=65
#         else:
#             print(" ",end=" ")
    
#     print()



# n=int(input())
# val=90
# for i in range(n):
#     for  j in range(n):
#         if i+j==n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<65:
#         val=90
#     print()



# n=int(input())
# val=n
# if n>9:
#     val=9
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<1:
#         val=9
#     print()




# n=int(input())
# val=65

# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#             val+=1
#             if val>90:
#                 val=65
#         else:
#             print(" ",end=" ")
    
    
    
#     print()




# n=int(input())
# val=65+n-1
# if val>90:
#     val=val-26

# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<65:
#         val=90

#     print()


# n=int(input())
# val=90
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(chr(val),end="")
#         else:
#             print(" ",end=" ")
#     val-=1
#     if val<65:
#         val=90
#     print()




# n=int(input())
# val=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")
#             val+=1
#             if val>9:
#                 val=1
#         else:
#             print("*",end=" ")
#     print()




# n=int(input())
# for i in range(n):
#     val1=1
#     val2=1
#     for j in range(n):
#         if i>j :
#             print(val1,end=" ")
#             val1+=1
#             # print('1',end=" ")
#         elif i<j:
#             print(val2,end=" ")
#             val2+=1
#                 # print("2",end=" ")
#         else:
#             print("*",end=" ")
            
#     print()




# n=int(input())
# val=1
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             if i%2==0:
#                 print(val,end=" ")
#             else:
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     if i%2==0:    
#         val+=1
#         if val>9:
#             val=1
#     print()


# n=int(input())
# val=1
# p=True
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             if p:
#                 print(val,end=" ")
#                 val+=1
#                 if val>9:
#                     val=1
#                 p=False
#             else:
#                 print("*",end=" ")
#                 p=True
#         else:
#             print(" ",end=" ")
#     print()

    


# n=int(input())
# for i in range(2*n-1):
#     for j in range(n):
#         if j==n-1 or i+j==n-1 or i-j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# n=int(input())
# for i in range(2*n-1):
#     for j in range(n):
#         if j==0 or i==j or i+j==2*n-2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()




# n=int(input())
# val=ord('A')
# spc=n-1
# str=1
# for i in range(n):
#     for j in range(spc):
#         print(' ',end=" ")
#     for k in range(str):
#         print(chr(val),end=" ")
#     val+=1
#     if val>ord('Z'):
#         val=ord('A')
#     spc-=1
#     str+=2
#     print()



# n=int(input())
# val=1
# spc=n-1
# str=1
# for i in range(n):
#     for j in range(spc):
#         print(' ',end=" ")
#     for k in range(str):
#         print(val,end=" ")
#         val+=1
#         if val>9:
#             val=1
#     spc-=1
#     str+=2
#     print()




# n=int(input())
# val=n
# if val>9:
#     val=9
# spc=n-1
# str=1
# for i in range(n):
#     for j in range(spc):
#         print(' ',end=" ")
#     for k in range(str):
#         print(val,end=" ")
#     val-=1
#     if val<1:
#         val=9
#     spc-=1
#     str+=2
#     print()




# n=int(input())
# val=ord('A')+n-1
# if val>ord('Z'):
#     val=ord('Z')
# spc=n-1
# str=1
# for i in range(n):
#     for j in range(spc):
#         print(' ',end=" ")
#     for k in range(str):
#         print(chr(val),end=" ")
#     val-=1
#     if val<ord('A'):
#         val=ord('Z')
#     spc-=1
#     str+=2
#     print()



# n=int(input())
# spc=0
# str=2*n-1
# for i in range(n):
#     for j in range(spc):
#         print(' ',end=" ")
#     for k in range(str):
#         print('*',end=" ")
    
#     spc+=1
#     str-=2
#     print()



n=int(input())
spc=0
str=2*n-1
val=1
for i in range(n):
    for j in range(spc):
        print(' ',end=" ")
    for k in range(str):
        print(val,end=" ")
        val+=1
        if val>9:
            val=1
    
    spc+=1
    str-=2
    print()