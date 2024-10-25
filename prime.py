def prime(n):
    if n<2:
        return False
    elif n==2:
            return True
    else:
            for i in range(2,n//2+1):
               if n%i==0:
                  return False
               return True
        

n=int(input("n:"))
if prime(n):
    print(f"{n} is prime")   
else:
    print(f"{n} is not prime") 