print("Какую задачу нужно решить: a,b,c")
a = "a) кодирование информации"
b = "b) кодирование звука"
c = "c) кодирование изображения"
print(a)
print(b)
print(c)
bukva = input("Выберите вид задачи")
print("вид задачи")
if bukva == "a":
    print("выбор неизвестного: I,N,i,K")
    a = "I) информационный объем"
    b = "N) мощность алфавита(кол-во символовв алфавите)"
    c = "i) вес одного символа"
    d = "K) число знаков в тексте"
    print(a)
    print(b)
    print(c)
    print(d)
    neizvestnoe = input()
    
    if neizvestnoe == "I":
        print("Введите i")
        i = int(input())
        print("Введите K")
        K = int(input())
        I = K*i
        print(I)
    elif neizvestnoe == "N":
        print("Введите i")
        i= int(input())
        N = 2**i
        print(N)
    elif neizvestnoe == "i":
        print("Введите I")
        I = int(input())
        print("Введите K")
        K = int(input())
        i = I/K
        print(i)
    elif neizvestnoe == "K":
        print("Введите I")
        I = int(input())
        print("Введите i")
        i = int(input())
        K = I/i
        print(K)
elif bukva == "b":
    print("выбор неизвестного:I, H, t, b, K ")
    a = "I) объем звуковой информации"
    b = "H) частота дискрети зации"
    c = "t) время записи звука"
    d = "b) разрядность квантования"
    e = "e) кол-во уровней квантования"
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    neizvestnoe = input()
    
    if neizvestnoe == "I":
        print("Введите H")
        H = int(input())
        print("Введите t")
        t = int(input())
        print("Введите b")
        b = int(input())
        I = H*t*b
        print(I)
    elif neizvestnoe == "H":
        print("Введите I")
        I = int(input())
        print("Введите t")
        t = int(input())
        print("Введите b")
        b = int(input())
        H = I/t*b
        print(H)
    elif neizvestnoe == "t":
        print("Введите I")
        I = int(input())
        print("Введите t")
        t = int(input())
        print("Введите b")
        b = int(input())
        t = I/H*b
        print(t)
    elif neizvestnoe == "b":
        print("Введите I")
        I = int(input())
        print("Введите H")
        H = int(input())
        print("Введите t")
        t = int(input())
        b = I/H*t
        print(b)
    elif neizvestnoe == "K":
        print("Введите b")
        b = int(input())
        K = 2**b
        print(K)
elif bukva == "c":
    print("выбор неизвестного:K, b ")
    a = "K) кол-во оттенков"
    b = "b) глубина цвета"
    print(a)
    print(b)
    neizvestnoe = input()
    

    if neizvestnoe == "K":
        print("Введите b")
        b = int(input())
        K = 2**b
        print(K)
    elif neizvestnoe == "b":
        print("Введите K")
        K = input(int())
        b = 1
        while 2**b != (int(K)):
            b = b + 1 
        print(b)


