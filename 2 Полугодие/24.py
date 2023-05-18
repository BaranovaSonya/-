with open('24-241.txt') as f:
        a = f.readline()
        b = a.split('E')
        mini = 999999999
        for i in b:
            y = 0
            if i.count('B')>=2 and i.count('A')>5:
                y = i
                c = i.split('B')
                sp = []
                p = 0
                for x in c:
                    if x.count('A')>5:
                        p = len(i)+2
                        mini = min(p,mini)
                    
print(mini)

