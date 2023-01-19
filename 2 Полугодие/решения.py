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
    spisok=[]
    for num in range(2,1000):
      n=0
      for delit in range (2,100):
        if num%delit==0 and x<i: n+=1

      if n==0:spisok.append(num)

    flag=False
    for i in spisok:
        for y in range (100):
            if y*4+117==i and flag==False:
                print(y, i)
                flag=True
