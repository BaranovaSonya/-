def a ():
    A = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    a = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')  
    Morze = list([".-","-...",".--","--.","-..",".","...-","--..","..",".---","-.-",".-..","--","-","---",".--.",".-.","...","-","..-","..-.","....","-.-.","---.","----","--.-",".--.-","-.--","-..-","..-..","..--",".-.-"])
    InpS = input('Введите исходную строку: ')
    OutS = str('')
    for i in range(1, (len(InpS)+1)):
        for j in range (1, 32):
            if (InpS[i-1] == str(A[j-1])) or (InpS[i-1] == str(a[j-1])):
                OutS = OutS + str(Morze[j-1]) + ' '
    print('Ваша строка, перекодированная на азбуку Морзе: ' +OutS)


def b ():
    N10=int(input("введите число"))
    Np=int(0)
    k=int(1)
    p=int(input("введите число"))
    print("N10=")
    print("p=")
    while N10!=0:
        Np=Np+(N10%p)*k
        k=k*10
        N10=N10//p
    print('N',p,'=',Np)

def c():
    p=int()
    p=int(input(f"{p}-ичная таблица умножения"))
    for x in range(1,p):
        for y in range(1,p):
            z=(x*y//p)*10+(x*y)%p
            print(z,end=' ')
        print()


def d ():
    a='0123456789'
    nums=list(a)
    print(nums)
     
    b='0000000 0001111 0010110 0011001 000101 0101010 0110011 0111100 1000011 1001100'
    hem=b.split()
    print(hem)
    for i in range(len(hem)):
        hem[i]=int(hem[i])
    print(hem)
     

    def distance(x,y):
        k=7
        for i in range(7):
            if x%10==y%10:
                k=k-1
                x=x//10
                y=y//10
            return k
     
    cod=int(input("код"))
     
    min=distance(cod,hem[0])
    imin=0
    for i in range(10):
        D=distance(cod,hem[i])
        if D:
            if min==0:
                print(f"код верный: символ {nums[imin]}")
        elif min==1:
            print(f"код исправлен: символ {nums[imin]}")
        else:print("Код неверный")

        
def f():
    p = int(input('Введите основание СС исходного числа: p = '))
    valid = False
    while valid == False:
        Np = (input(f'Введите исходное число: N{p} = '))
        for i in range(1, len(Np)):
            if int(Np[i]) >= p:
                print('Недопустимое число!')
                valid = False
                break
            else:
                valid = True
                Np = int(Np)
    k = int(1)
    N10 = int(0)
    while not Np == 0:
        N10 = N10+(Np%10)*k
        k = k*p
        Np = Np//10
    print(f'N10 = {N10}')

a()
b()
c()
d()
f()
