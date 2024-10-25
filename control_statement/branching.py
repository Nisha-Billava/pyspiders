#1.if
n=int(input("n:"))
if n>50 and n<100:
    print("HELLO")

#2.if else
n1=int(input("n1:"))
if n1>=-9 and n1<=9:
    print(f"{n1} is sinle digit value")
else:
    print(f"{n1} is not a single digit value")
#________________________________________#

n2=int(input("n2:"))
if n2>=-99 and n2<=-9 or n2>=9 and n2<=99:
    print(f"{n2} is two digit value")
else:
    print(f"{n2} is not a two digit value")
#_________________________________________#

n3=int(input("n3:"))
if n3%2==0:
    print("Even number");
else: 
    print("Odd number");
#__________________________________________#

ch1=input("ch1:")
if ch1 in ['a','e','i','o','u','A','E','I','O','U']:
    print(f"{ch1} is a vowel")
else:
    print(f"{ch1} is not a vowel")
#___________________________________________#

ch2=input("ch2:")
if ch2>='A' and ch2<='Z' or ch2>='a' or ch2<='z':
    print(f"{ch2} is an alphabet")
else:
    print(f"{ch2} is not an alphabet")
#______________________________________________#

n4=int(input("n4:"))
if n4>0:
    print(f"{n4} is +ve")
else:
    print(f"{n4} is not positive")



#3.if elif

n5=int(input("n5:"))
if n5>0:
    print(f"{n5} is +ve")
elif n5==0:
    print("ZERO")
else:
    print(f"{n5} is negative")
#_______________________________#

ch4=input("ch4:")
if ch4>='A' and ch4<='Z':
    print("Uppercase")
elif ch4>='a' and ch4<='z':
    print("lowercase")
elif ch4>='0' and ch4<='9':
    print("numeric string")
else:
    print("Special character")
#________________________________#


#4.Nested if
ch5=input("ch5:")
if ch5>='A' and ch5>='Z' or ch5>='a' and ch5<='z':
    if ch5 in ['A','E','I','O','U','a','e','i','o','u']:
        print(f"{ch5} is vowel")
    else:
        print("consonant")
else:
    print("Not alphabet")


#5.Match case
while True:
    op=input("op:")
    match op:
        case '+':
            a=int(input('a:'))
            b=int(input('b:'))
            print(a+b)
        case '-':
            a=int(input('a:'))
            b=int(input('b:'))
            print(a-b)
        case '*':
            a=int(input('a:'))
            b=int(input('b:'))
            print(a*b)
        case '/':
            a=int(input('a:'))
            b=int(input('b:'))
            print(a/b)
        case _:
            print("Invalid operation")

#________________________________________#


n=int(input("n: "))
if n>0:
    if n%2==0:
        print("positive even number")
    else:
        print("positive odd number")
elif n == 0:
    print("zero")
else:
    print("negative number")                 
    