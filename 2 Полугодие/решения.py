def f5():
    for N in range(516):
        b = f'{N:b}'
        if N % 2 == 0: 
            b +='10'
        else:
            b = '1' + b + '01'
        if int(b, 2) > 516:
            print (N)
            break     
   
def f6():
 from turtle import *
 left(90)
 for i in range(7):
    forward(300)
    right(120)
    pu()
    for x in range(1,9):
        for y in range(1,10):
            goto(x*30,y*30)
            dot(5)
    done()

def f8():
    from itertools import product
    nums=product('01234567',repeat=5)
    k=0
    n='16 36 56 76 61 63 65 67'
    nn=n.split()
    for n in nums:
        numb=''.join(n)
        sp=[]
        if numb.count('6')==1 and numb[0]!='0':
            for x in nn:
                if x in numb:
                    sp.append(x)
            if not sp: 
                k+=1
    print(k)
    

def f12():
    sp = []
    for i in range(2,1000):
      n=0
      for y in range (2,i):
        if i%y==0 : n+=1

      if n==0:sp.append(i)
        print (sp)
        for i in sp:
        for y in range (100):
            if y*4+105==i:
                print(y)
  sp = []
  for num in range(2,1000):
    for x in range(2, (num - 1):
                    if all((num%x!=0)for x in range(2, (num - 1)):
                           sp.append(num)

def f14():
    alf = '0123456789abcde'
    for x in alf:
        f = int(f'123{x}5', 15)+int(f'1{x}233', 15)
        if f%14 == 0:
            print (x, f//14)
            break
            
            
def f15():   
    sp = []
    if all(sp):
        print ('есть')

    for a in range (1,1000):
        if all (((x%2==0) <= (x%3!=0)) or (x+a>=100) for x in range(1,1000)):
                   print(a)
                   break


from itertools import product
def f23(x,y,z):
    count=0
    for i in range(1,z):
        nums=product('12',repeat=i)
        for numb in nums:
            #numb=''.join(n)
            a=x
            if x==10 and numb.count('2')>1:continue
            for ii in numb:
                if a==17: break 
                if ii=='1':a+=1
                elif ii=='2' :a*=2

            if a==y: count+=1
    return count
                
print(f23(1,10,10)*f23(10,35,25))
дадада                           
from itertools import product
for i in range(2,6):
    b = product ('12',repeat = i)
    for n in b:
        a = 5
        for x in n:
            if x == '1':a -=1
            else:
                a = a * 4
        if a == 62:
            print(n)             
