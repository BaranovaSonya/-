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
