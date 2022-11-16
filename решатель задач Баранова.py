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
    a = "I) информацинный объем"
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
                   
        
   

     
            

