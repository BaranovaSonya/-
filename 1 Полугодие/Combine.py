def menu():
    a= input('Какую программу хотите использовать?\n1-Азбука морзе,\n2- код Хемминга\n3- перевод из десятичной СС в указанную\n4-перевод из указанной СС в десятичную\n5- таблица умножения в СС с основанием p (2<p<=10)\n')
    if a=='1': Morze()
    elif a=='2': Hamming()
    elif a=='3': CC1()
    elif a=='4': CC2()
    elif a=='5': CC3()
    else:
        print('Вы ввели не существующее значение! Попробуйте снова')
        menu()
menu()
def Morze():
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
    ch= input('Хотите воспользоваться еще чем-нибудь?\n1- в меню\n2- выйти\n ')
    if ch=='1':
        menu()
    elif ch=='2':
        exit()
    else:
        print('Вы ввели несуществующее значение, попробуйте ещё раз!')
        exit()
Morze()

def Hamming():
    Tabl = [[n for n in range(0,10)], ['0000000','0001111','0010110','0011001','0100101','0101010','0110011','0111100','1000011','1001100']]
    Code = '' 
    def Distance(A, B):
        K = int(7)
        for i in range(1,8):
            if (int(A)%10) == (int(B)%10):
                K = K-1
            A = A[0:len(A)-1]
            B = B[0:len(B)-1]
        return(K)
    while not len(Code) == 7:
        Code = input('Код = ')
    minD = Distance(Code, Tabl[1][0])
    Num = 0 
    for j in range(1,10):
        D = Distance(Code, Tabl[1][j])
        if D<minD:
            minD = D
            Num = j 
    if minD == 0:
        print(f'Код верный: символ {Tabl[0][Num]}')
    elif minD == 1:
        print(f'Код исправлен: символ {Tabl[0][Num]}')    
    else: print('Код неверный.')
    ch1=input('Хотите воспользоваться еще чем-нибудь?\n1- в меню\n2- выйти\n ')
    if ch1=='1':
        menu()
    elif ch1=='2':
        exit()
    else:
        print('Вы ввели несуществующее значение, попробуйте ещё раз!')
        exit()
Hamming()

def CC1():
    p = int(input('p='))
    Valid = p
    Np = int(input(f'N{p}='))
    k = int(1)
    N10= int(0)
    while not Np ==0:
        N10= N10 + (Np%10) * k
        k= k*p
        Np = Np//10
    print(f'N10 = {N10}=')
    ch2=input('Хотите воспользоваться еще чем-нибудь?\n1- в меню\n2- выйти\n ')
    if ch2=='1':
        menu()
    elif ch2=='2':
        exit()
    else:
        print('Вы ввели несуществующее значение, попробуйте ещё раз!')
        exit()
CC1()

def CC2():
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
    ch3=input('Хотите воспользоваться еще чем-нибудь?\n1- в меню\n2- выйти\n ')
    if ch3=='1':
        menu()
    elif ch3=='2':
        exit()
    else:
        print('Вы ввели несуществующее значение, попробуйте ещё раз!')
        exit()
CC2()

def CC3():
    p= input('Введите p (2<=p<= 10) основание системы:\n')
    if p.isdigit==True:
        p=int(p)
        if 2<=p<= 10:
            for i in range(1,p):
                for q in range(1,p):
                    z=(i*q)//p*10+(i*q)%p
                    print(f'{z:4}',end=' ')
            print()
        else:
            print('Вы ввели несуществующее значение, попробуйте еще раз')
            CC3()
    else:
        print('Вы ввели несуществующее значение, попробуйте еще раз')
        CC3()
    ch4=input('Хотите воспользоваться еще чем-нибудь?\n1- в меню\n2- выйти\n ')
    if ch4=='1':
        menu()
    elif ch4=='2':
        exit()
    else:
        print('Вы ввели несуществующее значение, попробуйте ещё раз!')
        exit()
CC3()        
