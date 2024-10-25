#Based on number of operands
# 1.unary
# 2.binary
# 3.ternary



#Based on operation
a=10
b=2
c=2.5
d=1+2j
e="don"

#1.Arithmetic operators
#+
r1=a+b
print(r1,type(r1))
r2=a+c
print(r2,type(r2))
r3=a+d
print(r3,type(r3))
r4=d+d 
print(r4,type(r4))
r5=c+d
print(r5,type(r5))
#if one operand is string then TYPEERROR
r6=e+e
print(r6,type(r6))

#-
r1=a-b
print(r1,type(r1))
r2=a-c
print(r2,type(r2))
r3=a-d
print(r3,type(r3))
r4=d-d 
print(r4,type(r4))
r5=c-d
print(r5,type(r5))
#if one operand is string then TYPEERROR


#*
r1=a*b
print(r1,type(r1))
r2=a*c
print(r2,type(r2))
r3=a*d
print(r3,type(r3))
r4=d*d 
print(r4,type(r4))
r5=c*d
print(r5,type(r5))
#if one operand is string then TYPEERROR
r6=e*b
print(r6,type(r6))

#/
r1=a/b
print(r1,type(r1))
r2=a/c
print(r2,type(r2))
r3=a/d
print(r3,type(r3))
r4=d/d 
print(r4,type(r4))
r5=c/d
print(r5,type(r5))
#if one operand is string then TYPEERROR

#%
r1=a%b
print(r1,type(r1))
r2=a%c
print(r2,type(r2))
#if one operand is complex or string then TYPEERROR

#//
r1=a//b
print(r1,type(r1))
r2=a//c
print(r2,type(r2))
#if one operand is complex or string then TYPEERROR

#**
r1=a**b
print(r1,type(r1))
r2=a**c
print(r2,type(r2))
r3=a**d
print(r3,type(r3))
r4=c**d
print(r4,type(r4))
r5=d**d
print(r5,type(r5))
#if one operand is string then TYPEERROR




#2.relational operator
a,b,c=10,20,10
print(a==b)
print(a==c)
print(a!=b)
print(a!=c)
print(a>b)
print(a>=c)
print(a<b)
print(a<=c)
# if any one operand is complex/string->TypeError
#if both operands are string ->boolean
print("a">"A")



#3.logical operators(and,or,not)
print(a==b and a==c)
print(a==b or a==c)
print(not a==c)
print(a==c and not a==b or not a*2==c-10 or not a<b and b+10==c)



#4.bitwise operators
print(16&8)
print(10&12)
print(10|12)
print(10^12)
print(32^16)
print(10<<2)
print(12>>3)
print(~10)


#5.Assignment operators
#short-hand
x=10
print(x)
x+=5
print(x)



#special operators
#1.membership(in,not in)
name="Iron man"
print('I' in name)
print('k' in name)
print('n' not in name)
print('q' not in name)

#2.Identity Operator(is,is not)
a,b,c=10,20,10
print(a is b)
print(a is c)
print(a is not b)
print(a is not c)